#app/gui/widgets/main_window

import os
import re

from PyQt6.QtCore import Qt, QSize, QByteArray
from PyQt6.QtGui import QAction, QIcon, QPixmap, QPainter, QColor, QImage
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,QSizePolicy

)

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

        # Store icons directory path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icons_dir = os.path.join(current_dir, "resources", "icons")

        # Track theme and current selected sidebar section
        self.current_theme = "dark"
        self.current_section = None

        # Keep references to sidebar buttons and indicators
        self.sidebar_buttons = {}

        self.setup_ui()
        self.setup_menu_bar()

        # Set default section and theme
        self.on_sidebar_clicked("book")
        self.apply_dark_theme()














    def setup_ui(self):
        """Build the main window layout."""
        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        self.main_layout = QVBoxLayout(central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

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
        """Create the top application menu bar."""
        self.menu_bar = self.menuBar()
        self.menu_bar.setObjectName("mainMenuBar")

        books_menu = self.menu_bar.addMenu("Books")
        for item in ["View All", "Add", "Edit", "Delete", "Search"]:
            books_menu.addAction(QAction(item, self))

        data_menu = self.menu_bar.addMenu("Data")
        for item in ["Author", "Genre", "Language", "Publisher", "Translator", "Resource", "Esrb"]:
            data_menu.addAction(QAction(item, self))

        rent_menu = self.menu_bar.addMenu("Rent")
        for item in ["Issue Book", "Return Book", "All Rentals", "Overdue"]:
            rent_menu.addAction(QAction(item, self))

        settings_menu = self.menu_bar.addMenu("Settings")
        appearance_menu = settings_menu.addMenu("Appearance")

        dark_action = QAction("Dark Theme", self)
        light_action = QAction("Light Theme", self)

        dark_action.triggered.connect(self.apply_dark_theme)
        light_action.triggered.connect(self.apply_light_theme)

        appearance_menu.addAction(dark_action)
        appearance_menu.addAction(light_action)

        help_menu = self.menu_bar.addMenu("Help")
        help_menu.addAction(QAction("Guide", self))


















    def setup_activity_bar(self):
        """Create the left sidebar with icon buttons."""
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
            {"id": "book", "tooltip": "Books", "icon": "book.svg"},
            {"id": "author", "tooltip": "Authors", "icon": "author.svg"},
            {"id": "translator", "tooltip": "Translators", "icon": "translator.svg"},
            {"id": "language", "tooltip": "Languages", "icon": "language.svg"},
            {"id": "publisher", "tooltip": "Publishers", "icon": "publisher.svg"},
            {"id": "genre", "tooltip": "Genres", "icon": "genre.svg"},
            {"id": "resource", "tooltip": "Resources", "icon": "resource.svg"},
            {"id": "esrb", "tooltip": "ESRB", "icon": "esrb.svg"},
        ]

        for item_data in items:
            self.create_sidebar_button(item_data)

        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.panels_layout.addWidget(self.activity_bar)



















    def create_sidebar_button(self, data):
        """Create a single sidebar button with its active indicator."""
        btn_id = data["id"]

        container = QWidget()
        container.setObjectName("activityButtonContainer")

        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        indicator = QWidget()
        indicator.setObjectName("activityIndicator")
        indicator.setFixedWidth(4)

        button = QPushButton()
        button.setObjectName("activityButton")
        button.setToolTip(data["tooltip"])
        button.setFixedSize(56, 44)
        button.setIconSize(QSize(24, 24))
        button.clicked.connect(lambda _, section_id=btn_id: self.on_sidebar_clicked(section_id))

        container_layout.addWidget(indicator)
        container_layout.addWidget(button)
        self.scroll_layout.addWidget(container)

        self.sidebar_buttons[btn_id] = {
            "button": button,
            "indicator": indicator,
            "icon_name": data["icon"],
        }















    def setup_side_panel(self):
        """Create the middle panel used for section lists."""
        self.side_panel = QWidget()
        self.side_panel.setObjectName("sidePanel")
        self.side_panel.setFixedWidth(260)

        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(12, 12, 12, 12)

        self.panels_layout.addWidget(self.side_panel)

















    def setup_content_area(self):
        """Create the main content area."""
        self.content_panel = QWidget()
        self.content_panel.setObjectName("contentPanel")

        self.content_layout = QVBoxLayout(self.content_panel)

        self.content_label = QLabel("Welcome")
        self.content_label.setObjectName("contentTitle")
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_layout.addWidget(self.content_label)
        self.panels_layout.addWidget(self.content_panel, stretch=1)





















    def on_sidebar_clicked(self, section):
        """Handle sidebar button selection and update the side panel."""
        self.current_section = section

        for btn_id, item in self.sidebar_buttons.items():
            is_active = btn_id == section

            item["indicator"].setProperty("active", is_active)
            item["button"].setProperty("active", is_active)

            item["indicator"].style().unpolish(item["indicator"])
            item["indicator"].style().polish(item["indicator"])

            item["button"].style().unpolish(item["button"])
            item["button"].style().polish(item["button"])

        self.clear_side_panel()

        title = QLabel(section.upper())
        title.setObjectName("sideTitle")
        self.side_layout.addWidget(title)

        if section == "esrb":
            widget=EsrbsListWidget()

        
        elif section == "author":
            widget=AuthorsListWidget()
        
        elif section == "book":
            widget=BooksListWidget()
        
        elif section == "genre":
            widget=GenresListWidget()

        
        elif section == "language":
            widget=LanguagesListWidget()
        
        elif section == "publisher":
            widget=PublishersListWidget()
        
        elif section == "resource":
            widget=ResourcesListWidget()

        
        elif section == "translator":
            widget=TranslatorsListWidget()
        
        else:
            widget=QLabel(f"List of {section}")
    
        self.side_layout.addWidget(widget)
        widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget.setMinimumWidth(0)

        self.content_label.setText(f"{section.title()} View")
        















    def clear_side_panel(self):
        """Remove all widgets from the side panel layout."""
        while self.side_layout.count():
            item = self.side_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()























    def refresh_styles(self):
        """Force all widgets to refresh after a theme change."""
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
















    def apply_dark_theme(self):
        """Apply the dark stylesheet and refresh sidebar icons."""
        self.current_theme = "dark"

        app = QApplication.instance()
        app.setStyleSheet("")
        app.setStyleSheet(DARK_THEME)

        self.update_sidebar_icons("#FFFFFF")
        self.refresh_styles()















    def apply_light_theme(self):
        """Apply the light stylesheet and refresh sidebar icons."""
        self.current_theme = "light"

        app = QApplication.instance()
        app.setStyleSheet("")
        app.setStyleSheet(LIGHT_THEME)

        self.update_sidebar_icons("#202124")
        self.refresh_styles()





















    def update_sidebar_icons(self, color):
        """Update all sidebar icons based on the active theme."""
        for item in self.sidebar_buttons.values():
            if item["icon_name"] == "esrb.svg" and self.current_theme == "light":
                icon = self.get_inverted_icon(item["icon_name"])
            else:
                icon = self.get_colored_icon(item["icon_name"], color)

            if icon:
                item["button"].setIcon(icon)






















    def get_inverted_icon(self, name):
        """Render an SVG icon and invert its visible colors."""
        path = os.path.join(self.icons_dir, name)
        if not os.path.exists(path):
            return None

        try:
            renderer = QSvgRenderer(path)
            if not renderer.isValid():
                return None

            pixmap = QPixmap(24, 24)
            pixmap.fill(Qt.GlobalColor.transparent)

            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()

            image = pixmap.toImage().convertToFormat(QImage.Format.Format_ARGB32)

            for y in range(image.height()):
                for x in range(image.width()):
                    pixel_color = QColor(image.pixelColor(x, y))

                    if pixel_color.alpha() == 0:
                        continue

                    inverted_color = QColor(
                        255 - pixel_color.red(),
                        255 - pixel_color.green(),
                        255 - pixel_color.blue(),
                        pixel_color.alpha(),
                    )
                    image.setPixelColor(x, y, inverted_color)

            return QIcon(QPixmap.fromImage(image))

        except Exception as error:
            print(f"Icon invert error for {name}: {error}")
            return None



















    def get_colored_icon(self, name, color):
        """Load an SVG icon and replace its fill/stroke colors."""
        path = os.path.join(self.icons_dir, name)
        if not os.path.exists(path):
            return None

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = file.read()

            data = re.sub(r'fill="[^"]+"', f'fill="{color}"', data)
            data = re.sub(r'stroke="[^"]+"', f'stroke="{color}"', data)
            data = data.replace("fill:#000000", f"fill:{color}")
            data = data.replace("stroke:#000000", f"stroke:{color}")
            data = re.sub(r'fill-opacity="[^"]+"', 'fill-opacity="1.0"', data)
            data = re.sub(r'opacity="[^"]+"', 'opacity="1.0"', data)

            renderer = QSvgRenderer(QByteArray(data.encode()))
            pixmap = QPixmap(24, 24)
            pixmap.fill(Qt.GlobalColor.transparent)

            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()

            return QIcon(pixmap)

        except Exception as error:
            print(f"Icon color error for {name}: {error}")
            return None
