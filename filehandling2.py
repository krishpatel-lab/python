
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from pathlib import Path
import os
import shutil


# ---------------- COLORS ----------------

BG = "#F4F7FB"
SIDEBAR = "#172554"
BLUE = "#3B82F6"
GREEN = "#10B981"
PURPLE = "#8B5CF6"
RED = "#EF4444"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
GREY = "#64748B"


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("File Manager Pro")
root.geometry("1100x700")
root.configure(bg=BG)
root.minsize(950, 620)


# ---------------- FUNCTIONS ----------------

def status(message):
    status_label.config(text="●  " + message)


def create_folder():
    parent = filedialog.askdirectory(title="Choose Location")

    if not parent:
        return

    name = simpledialog.askstring("Create Folder", "Enter folder name:")

    if not name or name in (".", "..") or "/" in name or "\\" in name:
        if name:
            messagebox.showerror("Error", "Enter a valid folder name.")
        return

    p = Path(parent) / name

    if p.exists():
        messagebox.showerror("Error", "Folder already exists!")
        return

    p.mkdir()
    status("Folder created successfully")


def read_folder():
    folder = filedialog.askdirectory(title="Select Folder")

    if not folder:
        return

    tree.delete(*tree.get_children())

    for item in sorted(Path(folder).iterdir()):
        kind = "Folder" if item.is_dir() else "File"
        tree.insert("", "end", values=(item.name, kind, str(item)))

    status("Folder contents loaded")


def update_folder():
    folder = filedialog.askdirectory(title="Select Folder")

    if not folder:
        return

    old = Path(folder)

    new_name = simpledialog.askstring(
        "Rename Folder",
        "Enter new folder name:"
    )

    if not new_name or new_name in (".", "..") or "/" in new_name or "\\" in new_name:
        if new_name:
            messagebox.showerror("Error", "Enter a valid folder name.")
        return

    new = old.with_name(new_name)

    if new.exists():
        messagebox.showerror("Error", "Name already exists!")
        return

    old.rename(new)
    status("Folder renamed successfully")


def delete_folder():
    folder = filedialog.askdirectory(title="Select Folder")

    if not folder:
        return

    confirm = messagebox.askyesno(
        "Delete Folder",
        "This will permanently delete the folder and everything inside it. Continue?"
    )

    if confirm:
        shutil.rmtree(folder)
        status("Folder deleted successfully")


def create_file():
    file_path = filedialog.asksaveasfilename(
        title="Create File",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        return

    p = Path(file_path)

    if p.exists():
        messagebox.showerror("Error", "File already exists!")
        return

    data = simpledialog.askstring(
        "Create File",
        "Enter file content:"
    )

    if data is None:
        return

    with open(p, "x") as file:
        file.write(data)

    status("File created successfully")


def read_file():
    file_path = filedialog.askopenfilename(title="Select File")

    if not file_path:
        return

    p = Path(file_path)

    try:
        data = p.read_text(encoding="utf-8")

        window = tk.Toplevel(root)
        window.title("File Content")
        window.geometry("650x450")
        window.configure(bg=BG)

        tk.Label(
            window,
            text=p.name,
            font=("Arial", 17, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(pady=15)

        box = tk.Text(
            window,
            font=("Consolas", 12),
            bg=WHITE,
            fg=TEXT,
            wrap="word",
            padx=15,
            pady=15
        )
        box.pack(fill="both", expand=True, padx=20, pady=10)
        box.insert("1.0", data)
        box.config(state="disabled")

        status("File opened successfully")

    except (OSError, UnicodeError) as e:
        messagebox.showerror("Error", str(e))


def update_file():
    file_path = filedialog.askopenfilename(title="Select File")

    if not file_path:
        return

    p = Path(file_path)

    choice = simpledialog.askinteger(
        "Update File",
        "1. Rename File\n2. Overwrite File\n3. Append Content\n\nEnter your choice:"
    )

    if choice == 1:
        name = simpledialog.askstring(
            "Rename File",
            "Enter new file name:"
        )

        if not name or name in (".", "..") or "/" in name or "\\" in name:
            if name:
                messagebox.showerror("Error", "Enter a valid file name.")
            return

        new = p.with_name(name)

        if new.exists():
            messagebox.showerror("Error", "File already exists!")
            return

        p.rename(new)
        status("File renamed successfully")

    elif choice in (2, 3):
        data = simpledialog.askstring(
            "File Content",
            "Enter content:"
        )

        if data is None:
            return

        mode = "w" if choice == 2 else "a"

        with open(p, mode, encoding="utf-8") as file:
            if choice == 3:
                file.write("\n")
            file.write(data)

        status("File updated successfully")

    elif choice is not None:
        messagebox.showwarning("Invalid Choice", "Select 1, 2 or 3")


def delete_file():
    file_path = filedialog.askopenfilename(title="Select File")

    if not file_path:
        return

    confirm = messagebox.askyesno(
        "Delete File",
        "Are you sure you want to delete this file?"
    )

    if confirm:
        os.remove(file_path)
        status("File deleted successfully")


# ---------------- SIDEBAR ----------------

sidebar = tk.Frame(root, bg=SIDEBAR, width=230)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="✦ FILE MANAGER",
    font=("Arial", 18, "bold"),
    bg=SIDEBAR,
    fg=WHITE
).pack(pady=(35, 8))

tk.Label(
    sidebar,
    text="MANAGEMENT SYSTEM",
    font=("Arial", 9),
    bg=SIDEBAR,
    fg="#93C5FD"
).pack(pady=(0, 40))


def sidebar_button(name, command):
    tk.Button(
        sidebar,
        text=name,
        command=command,
        font=("Arial", 11),
        bg=SIDEBAR,
        fg=WHITE,
        activebackground="#334C80",
        activeforeground=WHITE,
        relief="flat",
        anchor="w",
        padx=25,
        pady=13,
        cursor="hand2"
    ).pack(fill="x", padx=10, pady=3)


sidebar_button("⌂   Dashboard", lambda: status("Dashboard selected"))
sidebar_button("▣   Create Folder", create_folder)
sidebar_button("▤   Browse Folder", read_folder)
sidebar_button("✎   Update Folder", update_folder)
sidebar_button("✕   Delete Folder", delete_folder)

tk.Frame(sidebar, bg="#334155", height=1).pack(
    fill="x", padx=20, pady=15
)

sidebar_button("＋   Create File", create_file)
sidebar_button("▤   Read File", read_file)
sidebar_button("✎   Update File", update_file)
sidebar_button("✕   Delete File", delete_file)

tk.Button(
    sidebar,
    text="⏻   Exit Application",
    command=root.destroy,
    font=("Arial", 11, "bold"),
    bg="#991B1B",
    fg=WHITE,
    relief="flat",
    cursor="hand2"
).pack(side="bottom", fill="x", padx=15, pady=25)


# ---------------- MAIN DASHBOARD ----------------

content = tk.Frame(root, bg=BG)
content.pack(side="left", fill="both", expand=True, padx=30, pady=25)


# Header

tk.Label(
    content,
    text="Dashboard",
    font=("Arial", 26, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w")

tk.Label(
    content,
    text="Manage your files and folders from one place.",
    font=("Arial", 11),
    bg=BG,
    fg=GREY
).pack(anchor="w", pady=(5, 25))


# Information cards

cards = tk.Frame(content, bg=BG)
cards.pack(fill="x", pady=5)


def create_card(parent, title, description, color, command):
    card = tk.Frame(
        parent,
        bg=WHITE,
        padx=15,
        pady=15,
        highlightbackground="#E2E8F0",
        highlightthickness=1
    )

    tk.Label(
        card,
        text=title,
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=color
    ).pack(anchor="w")

    tk.Label(
        card,
        text=description,
        font=("Arial", 10),
        bg=WHITE,
        fg=GREY
    ).pack(anchor="w", pady=8)

    tk.Button(
        card,
        text="Open  →",
        command=command,
        bg=color,
        fg=WHITE,
        relief="flat",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        padx=12,
        pady=6
    ).pack(anchor="w", pady=(5, 0))

    return card


card_data = [
    ("📁  Folder", "Create a new folder", BLUE, create_folder),
    ("📄  File", "Create a new file", GREEN, create_file),
    ("✎  Update", "Modify files and folders", PURPLE, update_file),
    ("🗑  Delete", "Remove files and folders", RED, delete_file)
]

for col, (title, desc, color, command) in enumerate(card_data):
    card = create_card(cards, title, desc, color, command)
    card.grid(row=0, column=col, padx=6, sticky="nsew")
    cards.columnconfigure(col, weight=1)


# Explorer section

tk.Label(
    content,
    text="File Explorer",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w", pady=(30, 12))


explorer = tk.Frame(content, bg=WHITE)
explorer.pack(fill="both", expand=True)

tree = ttk.Treeview(
    explorer,
    columns=("Name", "Type", "Location"),
    show="headings"
)

tree.heading("Name", text="NAME")
tree.heading("Type", text="TYPE")
tree.heading("Location", text="LOCATION")

tree.column("Name", width=160)
tree.column("Type", width=90)
tree.column("Location", width=300)

tree.pack(fill="both", expand=True, padx=12, pady=12)


# Refresh button

tk.Button(
    content,
    text="↻  Browse Folder",
    command=read_folder,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=8
).pack(anchor="e", pady=12)


# Status bar

status_label = tk.Label(
    root,
    text="●  Welcome to File Manager Pro",
    font=("Arial", 10),
    bg="#E2E8F0",
    fg=GREEN,
    anchor="w",
    padx=15,
    pady=10
)
status_label.pack(side="bottom", fill="x")


# Run application

root.mainloop()
