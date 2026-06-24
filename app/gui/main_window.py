import sys
import os
import re

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QMenuBar, QSizePolicy
)
from PyQt6.QtGui import QAction, QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import Qt, QSize, QByteArray


from app.gui.components.esrbs_list import EsrbsListWidget
from app.gui.components.authors_list import AuthorsListWidget
from app.gui.components.books_list import BooksListWidget
from app.gui.components.genres_list import GenresListWidget
from app.gui.components.languages_list import LanguagesListWidget
from app.gui.components.publishers_list import PublishersListWidget
from app.gui.components.resorces_list import ResourcesListWidget
from app.gui.components.translators_list import TranslatorsListWidget

from app.gui.resources.themes.dark_theme import DARK_THEME
from app.gui.resources.themes.light_theme import LIGHT_THEME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Manager")
        self.resize(1200, 720)

        # Path setup
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icons_dir = os.path.join(current_dir, "resources", "icons")

        # Theme state
        self.current_theme = "dark"
        self.sidebar_buttons = {}

        # UI Initialization
        self.setup_ui()
        self.setup_menu_bar()
        
        # Default selection
        self.on_sidebar_clicked("book")
        
        # Apply theme
        self.apply_dark_theme()

    def setup_ui(self):
        """Main UI Layout Construction."""
        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        self.main_layout = QVBoxLayout(central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Panels Container
        self.panels_container = QWidget()
        self.panels_container.setObjectName("panelsContainer")
        self.panels_layout = QHBoxLayout(self.panels_container)
        self.panels_layout.setContentsMargins(0, 0, 0, 0)
        self.panels_layout.setSpacing(0)

        self.setup_activity_bar()
        self.setup_side_panel()
        self.setup_content_area()

        self.main_layout.addWidget(self.panels_container, stretch=1)

    def setup_menu_bar(self):
        """Configure the top menu bar."""
        # استفاده از منوبار پیش‌فرض QMainWindow برای پایداری بیشتر
        self.menu_bar = self.menuBar()
        self.menu_bar.setObjectName("mainMenuBar")

        # Books Menu
        books_menu = self.menu_bar.addMenu("Books")
        for item in ["View All", "Add", "Edit", "Delete", "Search"]:
            books_menu.addAction(QAction(item, self))

        # Data Menu
        data_menu = self.menu_bar.addMenu("Data")
        for item in ["Author", "Genre", "Language", "Publisher", "Translator", "Resource", "Esrb"]:
            data_menu.addAction(QAction(item, self))

        # Rent Menu
        rent_menu = self.menu_bar.addMenu("Rent")
        for item in ["Issue Book", "Return Book", "All Rentals", "Overdue"]:
            rent_menu.addAction(QAction(item, self))

        # Settings Menu
        settings_menu = self.menu_bar.addMenu("Settings")
        appearance_menu = settings_menu.addMenu("Appearance")
        
        dark_action = QAction("Dark Theme", self)
        light_action = QAction("Light Theme", self)
        dark_action.triggered.connect(self.apply_dark_theme)
        light_action.triggered.connect(self.apply_light_theme)
        
        appearance_menu.addAction(dark_action)
        appearance_menu.addAction(light_action)

        # Help Menu
        help_menu = self.menu_bar.addMenu("Help")
        help_menu.addAction(QAction("Guide", self))

    def setup_activity_bar(self):
        """Left vertical bar with icons."""
        self.activity_bar = QWidget()
        self.activity_bar.setObjectName("activityBar")
        self.activity_bar.setFixedWidth(60)

        layout = QVBoxLayout(self.activity_bar)
        layout.setContentsMargins(0, 10, 0, 10)
        layout.setSpacing(0)

        scroll = QScrollArea()
        scroll.setObjectName("activityScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)

        content = QWidget()
        content.setObjectName("activityScrollContent")
        self.scroll_layout = QVBoxLayout(content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(8)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        items = [
            {"id": "book", "tooltip": "Books", "icon": "book.svg", "fallback": "BO"},
            {"id": "author", "tooltip": "Authors", "icon": "author.svg", "fallback": "AU"},
            {"id": "translator", "tooltip": "Translators", "icon": "translator.svg", "fallback": "TR"},
            {"id": "language", "tooltip": "Languages", "icon": "language.svg", "fallback": "LA"},
            {"id": "publisher", "tooltip": "Publishers", "icon": "publisher.svg", "fallback": "PU"},
            {"id": "genre", "tooltip": "Genres", "icon": "genre.svg", "fallback": "GE"},
            {"id": "resource", "tooltip": "Resources", "icon": "resource.svg", "fallback": "RE"},
            {"id": "esrb", "tooltip": "ESRB", "icon": "esrb.svg", "fallback": "ES"},
        ]

        for data in items:
            self.create_sidebar_button(data)

        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.panels_layout.addWidget(self.activity_bar)

    def create_sidebar_button(self, data):
        """Helper to create sidebar button with indicator."""
        btn_id = data["id"]
        container = QWidget()
        container.setObjectName("activityButtonContainer")
        c_layout = QHBoxLayout(container)
        c_layout.setContentsMargins(0, 0, 0, 0)
        c_layout.setSpacing(0)

        indicator = QWidget()
        indicator.setObjectName("activityIndicator")
        indicator.setFixedWidth(4)

        btn = QPushButton()
        btn.setObjectName("activityButton")
        btn.setToolTip(data["tooltip"])
        btn.setFixedSize(56, 44)
        btn.setIconSize(QSize(24, 24))
        btn.clicked.connect(lambda _, b_id=btn_id: self.on_sidebar_clicked(b_id))

        c_layout.addWidget(indicator)
        c_layout.addWidget(btn)
        self.scroll_layout.addWidget(container)

        self.sidebar_buttons[btn_id] = {
            "button": btn, "indicator": indicator, "icon_name": data["icon"], "fallback": data["fallback"]
        }

    def setup_side_panel(self):
        """Middle list panel."""
        self.side_panel = QWidget()
        self.side_panel.setObjectName("sidePanel")
        self.side_panel.setFixedWidth(260)
        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(12, 12, 12, 12)
        self.panels_layout.addWidget(self.side_panel)

    def setup_content_area(self):
        """Main viewing area."""
        self.content_panel = QWidget()
        self.content_panel.setObjectName("contentPanel")
        self.content_layout = QVBoxLayout(self.content_panel)
        self.content_label = QLabel("Welcome")
        self.content_label.setObjectName("contentTitle")
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(self.content_label)
        self.panels_layout.addWidget(self.content_panel, stretch=1)

    # --- Sidebar Logic ---
    def on_sidebar_clicked(self, section):
        for btn_id, item in self.sidebar_buttons.items():
            active = (btn_id == section)
            item["indicator"].setProperty("active", active)
            item["button"].setProperty("active", active)
            item["indicator"].style().unpolish(item["indicator"])
            item["indicator"].style().polish(item["indicator"])
            item["button"].style().unpolish(item["button"])
            item["button"].style().polish(item["button"])

        self.clear_side_panel()
        title = QLabel(section.upper())
        title.setObjectName("sideTitle")
        self.side_layout.addWidget(title)

        
        if section == "esrb" and EsrbsListWidget:
            self.side_layout.addWidget(EsrbsListWidget())
        
        elif section == "author" and AuthorsListWidget:
            self.side_layout.addWidget(AuthorsListWidget())
        
        elif section == "book" and BooksListWidget:
            self.side_layout.addWidget(BooksListWidget())
        
        elif section == "genre" and GenresListWidget:
            self.side_layout.addWidget(GenresListWidget())
        
        elif section == "language" and LanguagesListWidget:
            self.side_layout.addWidget(LanguagesListWidget())
        
        elif section == "publisher" and PublishersListWidget:
            self.side_layout.addWidget(PublishersListWidget())
        
        elif section == "resource" and ResourcesListWidget:
            self.side_layout.addWidget(ResourcesListWidget())

        elif section == "translator" and TranslatorsListWidget:
            self.side_layout.addWidget(TranslatorsListWidget())
        
        else:
            self.side_layout.addWidget(QLabel(f"List of {section}"))

        self.side_layout.addStretch()
        self.content_label.setText(f"{section.title()} View")

    def clear_side_panel(self):
        while self.side_layout.count():
            item = self.side_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

    # --- Theme Handlers ---
    def apply_dark_theme(self):
        self.current_theme = "dark"
        self.setStyleSheet(DARK_THEME)
        self.update_sidebar_icons("#FFFFFF")

    def apply_light_theme(self):
        self.current_theme = "light"
        self.setStyleSheet(LIGHT_THEME)
        self.update_sidebar_icons("#202124")

    def update_sidebar_icons(self, color):
        for btn_id, item in self.sidebar_buttons.items():
            icon = self.get_colored_icon(item["icon_name"], color)
            if icon: item["button"].setIcon(icon)

    def get_colored_icon(self, name, color):
        path = os.path.join(self.icons_dir, name)
        if not os.path.exists(path): return None
        try:
            with open(path, 'r') as f:
                data = f.read()
            
            # ۱. جایگزینی تمام رنگ‌های هاردکد شده (مشکی یا هر رنگ دیگر) با رنگ تم
            data = re.sub(r'fill="[^"]+"', f'fill="{color}"', data)
            data = re.sub(r'stroke="[^"]+"', f'stroke="{color}"', data)
            
            # ۲. اگر SVG استایل داخلی داشت (برای آیکون‌های پیچیده مثل ESRB)
            data = data.replace('fill:#000000', f'fill:{color}')
            data = data.replace('stroke:#000000', f'stroke:{color}')

            # ۳. حذف هرگونه شفافیت که باعث محو شدن می‌شود
            data = re.sub(r'fill-opacity="[^"]+"', 'fill-opacity="1.0"', data)
            data = re.sub(r'opacity="[^"]+"', 'opacity="1.0"', data)
            
            renderer = QSvgRenderer(QByteArray(data.encode()))
            pixmap = QPixmap(24, 24)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            return QIcon(pixmap)
        except:
            return None


