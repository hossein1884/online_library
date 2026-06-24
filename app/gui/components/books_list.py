from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.books_data_adapter import BooksDataAdapter


class BooksListWidget(QWidget):

    def __init__(self):
        super().__init__()

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("BOOK Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.title_label)

        # =========================================================
        # List Widget
        # =========================================================
        self.list_widget = QListWidget()


        layout.addWidget(self.list_widget)

        # =========================================================
        # Load Data
        # =========================================================
        self.load_books_data()

    # =========================================================
    # Load BOOK Data
    # =========================================================
    def load_books_data(self):

        self.list_widget.clear()

        try:
            books = BooksDataAdapter.get_all()

            if not books:
                self.list_widget.addItem("No BOOK ratings found")
                return

            for book in books:
                self.list_widget.addItem(book.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
