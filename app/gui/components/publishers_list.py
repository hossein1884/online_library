from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.publishers_data_adapter import PublishersDataAdapter


class PublishersListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.publishers = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("PUBLISHER Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search PUBLISHER rating...")
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
        self.load_publishers_data()

    # =========================================================
    # Load PUBLISHER Data
    # =========================================================
    def load_publishers_data(self):

        self.list_widget.clear()

        try:
            self.publishers = PublishersDataAdapter.get_all()

            if not self.publishers:
                self.list_widget.addItem("No PUBLISHER ratings found")
                return

            for publisher in self.publishers:
                self.list_widget.addItem(publisher.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for publisher in self.publishers:
            if publisher.name.lower().startswith(text):
                self.list_widget.addItem(publisher.name)
