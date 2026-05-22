import os

def get_category(file_name, file_types):
    ext = os.path.splitext(file_name)[1].lower()

    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    
    return "Others"


def create_folder(base_path, folder_name):
    folder_path = os.path.join(base_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def get_unique_name(destination):
    base, ext = os.path.splitext(destination)
    counter = 1

    while os.path.exists(destination):
        destination = f"{base}_{counter}{ext}"
        counter += 1

    return destination