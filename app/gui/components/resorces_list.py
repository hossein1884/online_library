from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.resources_data_adapter import ResourcesDataAdapter


class ResourcesListWidget(QWidget):

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
        self.title_label = QLabel("RESOURCE Ratings")
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
        self.load_resources_data()

    # =========================================================
    # Load RESOURCE Data
    # =========================================================
    def load_resources_data(self):

        self.list_widget.clear()

        try:
            resources = ResourcesDataAdapter.get_all()

            if not resources:
                self.list_widget.addItem("No RESOURCE ratings found")
                return

            for resource in resources:
                self.list_widget.addItem(resource.title)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
