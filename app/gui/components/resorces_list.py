from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from app.api.adapters.resource_data_adapter import ResourcesDataAdapter

class ResourcesListWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # هدر پنل
        self.title_label = QLabel("Resources List")
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
        self.load_resources_data()
        
    def load_resources_data(self):
        self.list_widget.clear()
        try:
            # فراخوانی تابع آداپتر که قبلا درستش کردیم
            all_resources = ResourcesDataAdapter.get_all()
            if not all_resources:
                self.list_widget.addItem("No resources found.")
                return
                
            for resource in all_resources:
               
                self.list_widget.addItem(resource.title)
        except Exception as e:
            self.list_widget.addItem(f"Error loading: {str(e)}")
            print(e)