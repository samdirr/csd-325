"""
Module 10 GUI ToDo assignment.
Sam Dirr
May 14,2026
"""

import tkinter as tk


class TodoApp:
    """A small scrollable Tkinter to-do list."""

    def __init__(self, root):
        self.root = root
        self.root.title("Dirr-ToDo")
        self.root.geometry("300x450")

        self.task_count = 0
        self.colors = ["#7AC943", "#FF5CAD"]

        self.build_menu()
        self.build_widgets()

    def build_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg="#7AC943",
            fg="black",
            activebackground="#FF5CAD",
            activeforeground="white",
        )
        file_menu.add_command(label="Exit", command=self.root.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def build_widgets(self):
        instructions = tk.Label(
            self.root,
            text="Enter a task below. Right-click an item in the list to delete it.",
            bg="#FF5CAD",
            fg="white",
            font=("Arial", 10, "bold"),
            wraplength=280,
            pady=8,
        )
        instructions.pack(fill=tk.X)

        list_area = tk.Frame(self.root)
        list_area.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(list_area, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(
            list_area,
            orient=tk.VERTICAL,
            command=self.canvas.yview,
        )
        self.task_frame = tk.Frame(self.canvas)
        self.task_window = self.canvas.create_window(
            (0, 0),
            window=self.task_frame,
            anchor="nw",
        )

        self.task_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfig(self.task_window, width=event.width),
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(side=tk.BOTTOM, fill=tk.X)
        self.entry.bind("<Return>", self.add_task)
        self.entry.focus()

    def add_task(self, event=None):
        task_text = self.entry.get().strip()

        if not task_text:
            return

        task_color = self.colors[self.task_count % len(self.colors)]
        task = tk.Label(
            self.task_frame,
            text=task_text,
            bg=task_color,
            fg="black" if task_color == "#7AC943" else "white",
            font=("Arial", 10),
            height=2,
            anchor="center",
        )
        task.pack(fill=tk.X)

        task.bind("<Button-3>", self.delete_task)
        task.bind("<Button-2>", self.delete_task)

        self.task_count += 1
        self.entry.delete(0, tk.END)

    def delete_task(self, event):
        event.widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    app = TodoApp(window)
    window.mainloop()
