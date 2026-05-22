import tkinter as tk
from tkinter import messagebox
from manager.manager_logic import *

class App:
    def __init__(self, root):
        root.title("Password Manager")
        root.geometry("400x350")

        tk.Label(root, text="Site").pack()
        self.site = tk.Entry(root)
        self.site.pack()

        tk.Label(root, text="Username").pack()
        self.user = tk.Entry(root)
        self.user.pack()

        tk.Label(root, text="Password").pack()
        self.pwd = tk.Entry(root, show="*")
        self.pwd.pack()

        tk.Button(root, text="Save", command=self.save).pack(pady=5)
        tk.Button(root, text="Get", command=self.get).pack(pady=5)
        tk.Button(root, text="Delete", command=self.delete).pack(pady=5)
        tk.Button(root, text="List", command=self.list_all).pack(pady=5)

        self.output = tk.Label(root, text="", fg="blue")
        self.output.pack()

    def save(self):
        if not self.site.get() or not self.user.get():
            messagebox.showwarning("Error", "Fill required fields")
            return

        pwd = add_password(self.site.get(), self.user.get(), self.pwd.get() or None)
        self.output.config(text=f"Saved! Password: {pwd}")

    def get(self):
        user, pwd = get_password(self.site.get())
        self.output.config(text=f"{user} | {pwd}" if user else "Not found")

    def delete(self):
        self.output.config(text="Deleted" if delete_password(self.site.get()) else "Not found")

    def list_all(self):
        self.output.config(text="\n".join(list_sites()) or "No data")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()