from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.genres_data_adapter import GenresDataAdapter


class GenresListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.genres = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("GENRE Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search GENRE rating...")
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
        self.load_genres_data()

    # =========================================================
    # Load GENRE Data
    # =========================================================
    def load_genres_data(self):

        self.list_widget.clear()

        try:
            self.genres = GenresDataAdapter.get_all()

            if not self.genres:
                self.list_widget.addItem("No GENRE ratings found")
                return

            for genre in self.genres:
                self.list_widget.addItem(genre.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for genre in self.genres:
            if text in genre.name.lower():
                self.list_widget.addItem(genre.name)
