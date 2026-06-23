import sqlite3
import os

# پیدا کردن مسیر مطلق پوشه‌ای که همین فایل (db_manager.py) در آن قرار دارد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ساخت مسیر دقیق دیتابیس
DB_PATH = os.path.join(BASE_DIR, 'books.db')

# ایجاد اتصال (Connection) و نشانگر (Cursor)
# نکته: در برنامه‌های دارای رابط کاربری (GUI)، معمولاً نیاز داریم دیتابیس در ترد (Thread) های مختلف خوانده شود.
# آرگومان check_same_thread=False از خطاهای مربوط به این موضوع جلوگیری می‌کند.
cn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = cn.cursor()

# (اختیاری) روشن کردن پشتیبانی از کلیدهای خارجی در SQLite
cur.execute("PRAGMA foreign_keys = ON")
cn.commit()