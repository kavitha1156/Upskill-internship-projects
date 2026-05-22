import tkinter as tk
from tkinter import filedialog, messagebox
from organizer.organizer import organize_folder


# Create main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x300")
root.resizable(False, False)


selected_path = ""


# 🔹 Select Folder Function
def select_folder():
    global selected_path
    selected_path = filedialog.askdirectory()

    if selected_path:
        path_label.config(text=selected_path)


# 🔹 Organize Function
def organize_files():
    if not selected_path:
        messagebox.showwarning("Warning", "Please select a folder first!")
        return

    try:
        organize_folder(selected_path)
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# 🔹 UI Design

title_label = tk.Label(root, text="File Organizer", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

select_btn = tk.Button(root, text="Select Folder", command=select_folder, width=20)
select_btn.pack(pady=10)

path_label = tk.Label(root, text="No folder selected", wraplength=400)
path_label.pack(pady=10)

organize_btn = tk.Button(root, text="Organize Files", command=organize_files, width=20, bg="green", fg="white")
organize_btn.pack(pady=20)


# Run app
root.mainloop()