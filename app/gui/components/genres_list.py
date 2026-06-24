from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.genres_data_adapter import GenresDataAdapter


class GenresListWidget(QWidget):

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
        self.title_label = QLabel("GENRE Ratings")
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
        self.load_genres_data()

    # =========================================================
    # Load GENRE Data
    # =========================================================
    def load_genres_data(self):

        self.list_widget.clear()

        try:
            genres = GenresDataAdapter.get_all()

            if not genres:
                self.list_widget.addItem("No GENRE ratings found")
                return

            for genre in genres:
                self.list_widget.addItem(genre.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
