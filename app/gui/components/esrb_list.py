from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import Qt

from app.api.adapters.esrbs_data_adapter import EsrbsDataAdapter


class EsrbsListWidget(QWidget):

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
        self.title_label = QLabel("ESRB Ratings")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.title_label.setStyleSheet("""
        font-size:15px;
        font-weight:600;
        color:#ffffff;
        padding-bottom:6px;
        border-bottom:1px solid #3c3c3c;
        """)

        layout.addWidget(self.title_label)

        # =========================================================
        # List Widget
        # =========================================================
        self.list_widget = QListWidget()

        self.list_widget.setStyleSheet("""
        QListWidget{
            background:transparent;
            border:none;
            color:#d4d4d4;
            outline:none;
        }

        QListWidget::item{
            padding:8px;
            border-radius:4px;
        }

        QListWidget::item:hover{
            background:#2a2d2e;
        }

        QListWidget::item:selected{
            background:#094771;
        }
        """)

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
            esrbs = EsrbsDataAdapter.get_all()

            if not esrbs:
                self.list_widget.addItem("No ESRB ratings found")
                return

            for esrb in esrbs:
                self.list_widget.addItem(esrb.name)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")
