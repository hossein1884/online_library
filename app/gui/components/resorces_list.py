from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt

from app.api.adapters.resources_data_adapter import ResourcesDataAdapter


class ResourcesListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.resources = []

        # =========================================================
        # Main Layout
        # =========================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # =========================================================
        # Title
        # =========================================================
        self.title_label = QLabel("RESOURCE Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        # =========================================================
        # Search Box
        # =========================================================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search RESOURCE rating...")
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
        self.load_resources_data()

    # =========================================================
    # Load RESOURCE Data
    # =========================================================
    def load_resources_data(self):

        self.list_widget.clear()

        try:
            self.resources = ResourcesDataAdapter.get_all()

            if not self.resources:
                self.list_widget.addItem("No RESOURCE ratings found")
                return

            for resource in self.resources:
                self.list_widget.addItem(resource.title)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    # =========================================================
    # Filter List
    # =========================================================
    def filter_list(self, text):

        self.list_widget.clear()

        text = text.lower()

        for resource in self.resources:
            if resource.name.lower().startswith(text):
                self.list_widget.addItem(resource.title)
