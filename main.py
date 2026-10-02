import tkinter as tk
from tkinter import messagebox

def on_hello_click():
    messagebox.showinfo("Thông báo", "xin chào")

# Khởi tạo cửa sổ ứng dụng
app = tk.Tk()
app.title("CPL26 Assignment 01")
app.geometry("300x200")

# Nút bấm hiển thị "xin chào"
btn_hello = tk.Button(app, text="Nút 1", command=on_hello_click)
btn_hello.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
