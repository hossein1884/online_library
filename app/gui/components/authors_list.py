#app/gui/components/authors_list

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit, QSizePolicy
from PyQt6.QtCore import Qt

from app.api.adapters.authors_data_adapter import AuthorsDataAdapter


class AuthorsListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.authors = []

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
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search AUTHOR rating...")
        self.search_box.textChanged.connect(self.filter_list)

        layout.addWidget(self.search_box)

        # =========================================================
        # List Widget
        # =========================================================
        self.list_widget = QListWidget()
        self.list_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
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
            self.authors = AuthorsDataAdapter.get_all()

            if not self.authors:
                self.list_widget.addItem("No AUTHOR ratings found")
                return

            for author in self.authors:
                self.list_widget.addItem(author.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for author in self.authors:
            if author.name.lower().startswith(text):
                self.list_widget.addItem(author.name)
