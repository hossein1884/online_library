from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.authors_data_adapter import AuthorsDataAdapter


class AuthorsListWidget(QWidget):

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
        self.title_label = QLabel("AUTHOR Ratings")
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
        self.load_authors_data()

    # =========================================================
    # Load AUTHOR Data
    # =========================================================
    def load_authors_data(self):

        self.list_widget.clear()

        try:
            authors = AuthorsDataAdapter.get_all()

            if not authors:
                self.list_widget.addItem("No AUTHOR ratings found")
                return

            for author in authors:
                self.list_widget.addItem(author.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
