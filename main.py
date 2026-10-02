import tkinter as tk
from tkinter import messagebox

def on_hello_click():
    messagebox.showinfo("Thông báo", "xin chào")

def on_goodbye_click():
    messagebox.showinfo("Thông báo", "tạm biệt")

# Khởi tạo cửa sổ ứng dụng
app = tk.Tk()
app.title("CPL26 Assignment 01")
app.geometry("300x200")

# Nút bấm 1
btn_hello = tk.Button(app, text="Nút 1", command=on_hello_click)
btn_hello.pack(pady=10)

# Nút bấm 2
btn_goodbye = tk.Button(app, text="Nút 2", command=on_goodbye_click)
btn_goodbye.pack(pady=10)

if __name__ == "__main__":
    app.mainloop()
