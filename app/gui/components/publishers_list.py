from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.publishers_data_adapter import PublishersDataAdapter


class PublishersListWidget(QWidget):

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
        self.title_label = QLabel("PUBLISHER Ratings")
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
        self.load_publishers_data()

    # =========================================================
    # Load PUBLISHER Data
    # =========================================================
    def load_publishers_data(self):

        self.list_widget.clear()

        try:
            publishers = PublishersDataAdapter.get_all()

            if not publishers:
                self.list_widget.addItem("No PUBLISHER ratings found")
                return

            for publisher in publishers:
                self.list_widget.addItem(publisher.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
