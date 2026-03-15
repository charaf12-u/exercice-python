import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# إعداد نافذة التطبيق
window = tk.Tk()
window.title("Calculator")

# إعداد واجهة المستخدم
display = tk.Entry(window, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# إعداد أزرار الأرقام والعمليات الحسابية
buttons = [
    (7, 1, 0, 1), (8, 1, 1, 1), (9, 1, 2, 1), ('/', 1, 3, 1),
    (4, 2, 0, 1), (5, 2, 1, 1), (6, 2, 2, 1), ('*', 2, 3, 1),
    (1, 3, 0, 1), (2, 3, 1, 1), (3, 3, 2, 1), ('-', 3, 3, 1),
    (0, 4, 0, 2), ('.', 4, 2, 1), ('+', 4, 3, 1)
]

for button in buttons:
    number, row, column, columnspan = button
    btn = tk.Button(window, text=number, padx=40, pady=20, command=lambda num=number: button_click(num))
    btn.grid(row=row, column=column, columnspan=columnspan)

# إعداد زر مسح الشاشة
btn_clear = tk.Button(window, text="Clear", padx=30, pady=20, command=button_clear)
btn_clear.grid(row=5, column=0, columnspan=2)

# إعداد زر النتيجة
btn_equal = tk.Button(window, text="=", padx=40, pady=20, command=button_equal)
btn_equal.grid(row=5, column=2, columnspan=2)

# تشغيل البرنامج
window.mainloop()