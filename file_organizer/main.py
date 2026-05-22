import os
print(os.listdir())

from organizer.organizer import organize_folder


def main():
    print("File Organizer")
    print("----------------------")

    path = input("Enter folder path: ").strip()

    organize_folder(path)


if __name__ == "__main__":
    main()