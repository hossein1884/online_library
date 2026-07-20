#app/gui/components/languages_list
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit, QSizePolicy
from PyQt6.QtCore import Qt

from app.api.adapters.languages_data_adapter import LanguagesDataAdapter


class LanguagesListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.languages = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("LANGUAGE Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search LANGUAGE rating...")
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
        self.load_languages_data()

    # =========================================================
    # Load LANGUAGE Data
    # =========================================================
    def load_languages_data(self):

        self.list_widget.clear()

        try:
            self.languages = LanguagesDataAdapter.get_all()

            if not self.languages:
                self.list_widget.addItem("No LANGUAGE ratings found")
                return

            for language in self.languages:
                self.list_widget.addItem(language.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for language in self.languages:
            if language.name.lower().startswith(text):
                self.list_widget.addItem(language.name)
