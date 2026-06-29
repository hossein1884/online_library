from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.books_data_adapter import BooksDataAdapter


class BooksListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.books = []

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
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search BOOK rating...")
        self.search_box.textChanged.connect(self.filter_list)

        layout.addWidget(self.search_box)

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
            self.books = BooksDataAdapter.get_all()

            if not self.books:
                self.list_widget.addItem("No BOOK ratings found")
                return

            for book in self.books:
                self.list_widget.addItem(book.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for book in self.books:
            if book.name.lower().startswith(text):
                self.list_widget.addItem(book.name)
