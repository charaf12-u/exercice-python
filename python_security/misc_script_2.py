import tkinter as tk
import hashlib


def hash_data():
    data = input_entry.get()  # استرجاع البيانات من حقل الإدخال
    hashed_data = hashlib.sha256(data.encode()).hexdigest()  # تنفيذ عملية التجزئة واسترجاع القيمة المشفرة
    result_label.config(text="Hashed Data: " + hashed_data)  # عرض البيانات المشفرة على التسمية


def verify_hash():
    data = input_entry.get()  # استرجاع البيانات من حقل الإدخال
    hashed_data = hashlib.sha256(data.encode()).hexdigest()  # تنفيذ عملية التجزئة واسترجاع القيمة المشفرة
    input_hash = input_hash_entry.get()  # استرجاع القيمة المشفرة من حقل الإدخال
    if hashed_data == input_hash:
        verification_label.config(text="التحقق: البيانات صحيحة")
    else:
        verification_label.config(text="التحقق: البيانات غير صحيحة")


# إنشاء نافذة البرنامج
root = tk.Tk()
root.title("تشفير البيانات باستخدام SHA256")

# إنشاء عنصر واجهة المستخدم لحقل الإدخال
input_entry = tk.Entry(root)
input_entry.pack()

# إنشاء عنصر واجهة المستخدم للزر "تشفير البيانات"
hash_button = tk.Button(root, text="تشفير البيانات", command=hash_data)
hash_button.pack()

# إنشاء عنصر واجهة المستخدم لعرض النتيجة
result_label = tk.Label(root, text="")
result_label.pack()

# إنشاء عنصر واجهة المستخدم لحقل الإدخال للبيانات المشفرة
input_hash_entry = tk.Entry(root)
input_hash_entry.pack()

# إنشاء عنصر واجهة المستخدم للزر "التحقق"
verify_button = tk.Button(root, text="التحقق", command=verify_hash)
verify_button.pack()

# إنشاء عنصر واجهة المستخدم لعرض نتيجة التحقق
verification_label = tk.Label(root, text="")
verification_label.pack()

# تشغيل البرنامج
root.mainloop()