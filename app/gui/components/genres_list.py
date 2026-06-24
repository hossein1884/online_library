from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from app.api.adapters.genre_data_adapter import GenresDataAdapter

class GenresListWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # هدر پنل
        self.title_label = QLabel("Genres List")
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
        self.load_genres_data()
        
    def load_genres_data(self):
        self.list_widget.clear()
        try:
            # فراخوانی تابع آداپتر که قبلا درستش کردیم
            all_genres = GenresDataAdapter.get_all()
            if not all_genres:
                self.list_widget.addItem("No genres found.")
                return
                
            for genre in all_genres:
               
                self.list_widget.addItem(genre.name)
        except Exception as e:
            self.list_widget.addItem(f"Error loading: {str(e)}")