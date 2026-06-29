from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.esrbs_data_adapter import EsrbsDataAdapter


class EsrbsListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.esrbs = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("ESRB Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search ESRB rating...")
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
        self.load_esrbs_data()

    # =========================================================
    # Load ESRB Data
    # =========================================================
    def load_esrbs_data(self):

        self.list_widget.clear()

        try:
            self.esrbs = EsrbsDataAdapter.get_all()

            if not self.esrbs:
                self.list_widget.addItem("No ESRB ratings found")
                return

            for esrb in self.esrbs:
                self.list_widget.addItem(esrb.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for esrb in self.esrbs:
            if esrb.name.lower().startswith(text):
                self.list_widget.addItem(esrb.name)
