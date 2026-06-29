from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.translators_data_adapter import TranslatorsDataAdapter


class TranslatorsListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.translators = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("TRANSLATOR Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search TRANSLATOR rating...")
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
        self.load_translators_data()

    # =========================================================
    # Load TRANSLATOR Data
    # =========================================================
    def load_translators_data(self):

        self.list_widget.clear()

        try:
            self.translators = TranslatorsDataAdapter.get_all()

            if not self.translators:
                self.list_widget.addItem("No TRANSLATOR ratings found")
                return

            for translator in self.translators:
                self.list_widget.addItem(translator.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for translator in self.translators:
            if translator.name.lower().startswith(text):
                self.list_widget.addItem(translator.name)
