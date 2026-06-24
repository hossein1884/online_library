from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from app.api.adapters.publisher_data_adapter import PublishersDataAdapter

class PublishersListWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # هدر پنل
        self.title_label = QLabel("Publishers List")
        self.title_label.setStyleSheet("font-weight: bold; font-size: 12px; color: #333333; margin-bottom: 5px;")
        layout.addWidget(self.title_label)
        
        # لیست ویجت برای نمایش نام 
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget { border: none; background-color: transparent; }
            QListWidget::item { padding: 6px; border-bottom: 1px solid #EAEAEA; }
            QListWidget::item:hover { background-color: #E5E5E5; }
        """)
        layout.addWidget(self.list_widget)
        
        # بارگذاری دیتای 
        self.load_publishers_data()
        
    def load_publishers_data(self):
        self.list_widget.clear()
        try:
            # فراخوانی تابع آداپتر که قبلا درستش کردیم
            all_publishers = PublishersDataAdapter.get_all()
            if not all_publishers:
                self.list_widget.addItem("No publishers found.")
                return
                
            for publisher in all_publishers:
               
                self.list_widget.addItem(publisher.name )
        except Exception as e:
            self.list_widget.addItem(f"Error loading: {str(e)}")