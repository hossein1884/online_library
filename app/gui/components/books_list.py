# app/gui/components/books_list.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from app.api.adapters.book_data_adapter import BooksDataAdapter

class BooksListWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # هدر پنل
        self.title_label = QLabel("Books List")
        self.title_label.setStyleSheet("font-weight: bold; font-size: 12px; color: #333333; margin-bottom: 5px;")
        layout.addWidget(self.title_label)
        
        # لیست ویجت برای نمایش نام کتاب‌ها
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget { border: none; background-color: transparent; }
            QListWidget::item { padding: 6px; border-bottom: 1px solid #EAEAEA; }
            QListWidget::item:hover { background-color: #E5E5E5; }
        """)
        layout.addWidget(self.list_widget)
        
        # بارگذاری دیتای کتاب‌ها
        self.load_books_data()
        
    def load_books_data(self):
        self.list_widget.clear()
        try:
            # فراخوانی تابع آداپتر که قبلا درستش کردیم
            all_books = BooksDataAdapter.get_all()
            if not all_books:
                self.list_widget.addItem("No books found.")
                return
                
            for book in all_books:
                # فرض می‌کنیم مشخصه نام کتاب book.name یا book.title است
                self.list_widget.addItem(book.name if book.name else book.title)
        except Exception as e:
            self.list_widget.addItem(f"Error loading: {str(e)}")