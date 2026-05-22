import os
import shutil
from organizer.utils import get_category, create_folder, get_unique_name
from organizer.file_types import FILE_TYPES


def organize_folder(path):
    # 🔹 Check if path exists
    if not os.path.exists(path):
        print("Invalid path!")
        return

    print("\nOrganizing files...\n")

    files = os.listdir(path)
    summary = {}

    for file in files:
        full_path = os.path.join(path, file)

        # 🔹 Process only files (skip folders)
        if not os.path.isfile(full_path):
            continue

        # 🔹 Skip hidden & system files
        if file.startswith(".") or file.upper() in [
            "NTUSER.DAT", "NTUSER.DAT.LOG1", "NTUSER.DAT.LOG2"
        ]:
            print(f"Skipped system/hidden file: {file}")
            continue

        try:
            # 🔹 Get category
            category = get_category(file, FILE_TYPES)

            # 🔹 Create folder
            folder_path = create_folder(path, category)

            # 🔹 Destination path
            destination = os.path.join(folder_path, file)

            # 🔹 Handle duplicate names
            destination = get_unique_name(destination)

            # 🔹 Move file
            shutil.move(full_path, destination)

            print(f"Moved: {file} -> {category}")

            # 🔹 Update summary
            summary[category] = summary.get(category, 0) + 1

        except PermissionError:
            print(f"Permission denied: {file}")

        except Exception as e:
            print(f"Error moving {file}: {e}")

    # 🔹 Print summary
    print("\nSummary:")
    print("------------------")
    for category, count in summary.items():
        print(f"{category}: {count} files")

    print("\nDone organizing!\n")