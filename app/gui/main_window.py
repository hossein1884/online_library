import sys
import os

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QMenuBar
)

from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import QByteArray, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPainter

from app.gui.components.esrb_list import EsrbsListWidget
from app.gui.resources.themes.dark_theme import DARK_THEME
from app.gui.resources.themes.light_theme import LIGHT_THEME


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Manager")
        self.resize(1200, 700)

        # مسیر آیکون‌ها
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.icons_dir = os.path.join(current_dir, "resources", "icons")

        # =========================================================
        # Choose Theme
        # =========================================================

        self.current_theme = "dark"

        # =========================================================
        # Central Widget
        # =========================================================

        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =========================================================
        # Menu Bar
        # =========================================================

        self.menu_bar = QMenuBar()
        self.menu_bar.setObjectName("mainMenuBar")
        main_layout.addWidget(self.menu_bar)

        books_menu = self.menu_bar.addMenu("Books")
        for item in ["View All", "Add", "Edit", "Delete", "Search"]:
            books_menu.addAction(QAction(item, self))

        data_menu = self.menu_bar.addMenu("Data")
        for item in [
            "Author",
            "Genre",
            "Language",
            "Publisher",
            "Translator",
            "Resource",
            "Esrb"
        ]:
            data_menu.addAction(QAction(item, self))

        rent_menu = self.menu_bar.addMenu("Rent")
        for item in ["Issue Book", "Return Book", "All Rentals", "Overdue"]:
            rent_menu.addAction(QAction(item, self))

        settings_menu = self.menu_bar.addMenu("Settings")

        home_action = QAction("Home", self)
        options_action = QAction("Options", self)

        settings_menu.addAction(home_action)
        settings_menu.addAction(options_action)
        settings_menu.addSeparator()

        appearance_menu = settings_menu.addMenu("Appearance")

        dark_action = QAction("Dark Theme", self)
        light_action = QAction("Light Theme", self)

        appearance_menu.addAction(dark_action)
        appearance_menu.addAction(light_action)

        dark_action.triggered.connect(self.apply_dark_theme)
        light_action.triggered.connect(self.apply_light_theme)

        help_menu = self.menu_bar.addMenu("Help")
        for item in ["Guide", "About", "Exit"]:
            help_menu.addAction(QAction(item, self))

        # =========================================================
        # Panels Container
        # =========================================================

        panels = QWidget()
        panels.setObjectName("panelsContainer")

        panels_layout = QHBoxLayout(panels)
        panels_layout.setContentsMargins(0, 0, 0, 0)
        panels_layout.setSpacing(0)

        main_layout.addWidget(panels, stretch=1)

        # =========================================================
        # Panel 1 — Activity Bar
        # =========================================================

        self.activity_bar = QWidget()
        self.activity_bar.setObjectName("activityBar")
        self.activity_bar.setFixedWidth(60)

        activity_layout = QVBoxLayout(self.activity_bar)
        activity_layout.setContentsMargins(6, 10, 6, 10)
        activity_layout.setSpacing(0)

        scroll = QScrollArea()
        scroll.setObjectName("activityScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        scroll_content = QWidget()
        scroll_content.setObjectName("activityScrollContent")

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(8)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Sidebar buttons definition
        sidebar_buttons = [
            {
                "id": "book",
                "tooltip": "Books",
                "icon": "book.svg",
                "fallback": "BO"
            },
            {
                "id": "author",
                "tooltip": "Authors",
                "icon": "author.svg",
                "fallback": "AU"
            },
            {
                "id": "translator",
                "tooltip": "Translators",
                "icon": "translator.svg",
                "fallback": "TR"
            },
            {
                "id": "language",
                "tooltip": "Languages",
                "icon": "language.svg",
                "fallback": "LA"
            },
            {
                "id": "publisher",
                "tooltip": "Publishers",
                "icon": "publisher.svg",
                "fallback": "PU"
            },
            {
                "id": "genre",
                "tooltip": "Genres",
                "icon": "genre.svg",
                "fallback": "GE"
            },
            {
                "id": "resource",
                "tooltip": "Resources",
                "icon": "resource.svg",
                "fallback": "RE"
            },
            {
                "id": "esrb",
                "tooltip": "ESRB",
                "icon": "esrb.svg",
                "fallback": "ES"
            },
        ]

        self.sidebar_buttons = {}

        for btn_data in sidebar_buttons:

            btn_id = btn_data["id"]

            container = QWidget()
            container.setObjectName("activityButtonContainer")

            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setSpacing(0)

            # indicator
            indicator = QWidget()
            indicator.setObjectName("activityIndicator")
            indicator.setFixedWidth(4)

            btn = QPushButton()
            btn.setObjectName("activityButton")
            btn.setToolTip(btn_data["tooltip"])
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

            # بسیار مهم برای اینکه دکمه از کادر بیرون نزند
            btn.setFixedSize(44, 44)
            btn.setIconSize(QSize(24, 24))

            icon_path = os.path.join(self.icons_dir, btn_data["icon"])

            if os.path.exists(icon_path):
                btn.setIcon(QIcon(icon_path))
                btn.setText("")
            else:
                btn.setText(btn_data["fallback"])
                print(f"⚠️ پیدا نشد: {icon_path}")

            btn.clicked.connect(
                lambda checked, b_id=btn_id: self.on_sidebar_clicked(b_id)
            )

            container_layout.addWidget(indicator)
            container_layout.addWidget(btn)

                
            # ... (داخل حلقه for btn_data in sidebar_buttons) ...
            self.sidebar_buttons[btn_id] = {
                    "button": btn,
                    "indicator": indicator,
                    "container": container,
                    "icon_name": btn_data["icon"]  # نام آیکون را ذخیره کنید تا راحت‌تر دسترسی داشته باشید
                }
            


            scroll_layout.addWidget(container)

        scroll_layout.addStretch()

        scroll.setWidget(scroll_content)
        activity_layout.addWidget(scroll)

        # =========================================================
        # Panel 2 — Sidebar List
        # =========================================================

        self.side_panel = QWidget()
        self.side_panel.setObjectName("sidePanel")
        self.side_panel.setFixedWidth(260)

        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(12, 12, 12, 12)
        self.side_layout.setSpacing(8)

        self.side_placeholder = QLabel("Select a section")
        self.side_placeholder.setObjectName("sidePlaceholder")
        self.side_placeholder.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.side_layout.addWidget(self.side_placeholder)
        self.side_layout.addStretch()

        # =========================================================
        # Panel 3 — Content Area
        # =========================================================

        self.content_panel = QWidget()
        self.content_panel.setObjectName("contentPanel")

        content_layout = QVBoxLayout(self.content_panel)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(10)

        self.content_label = QLabel("Content Area")
        self.content_label.setObjectName("contentTitle")
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(self.content_label)

        # =========================================================
        # Add Panels
        # =========================================================

        panels_layout.addWidget(self.activity_bar)
        panels_layout.addWidget(self.side_panel)
        panels_layout.addWidget(self.content_panel, stretch=1)

        # =========================================================
        # Apply Default Theme
        # =========================================================

        self.apply_dark_theme()

    # =========================================================
    # Sidebar Click Logic
    # =========================================================

    def on_sidebar_clicked(self, section):

        # reset indicators
        for item in self.sidebar_buttons.values():
            item["indicator"].setProperty("active", False)
            item["button"].setProperty("active", False)

            item["indicator"].style().unpolish(item["indicator"])
            item["indicator"].style().polish(item["indicator"])

            item["button"].style().unpolish(item["button"])
            item["button"].style().polish(item["button"])

        # activate selected indicator
        selected = self.sidebar_buttons.get(section)

        if selected:
            selected["indicator"].setProperty("active", True)
            selected["button"].setProperty("active", True)

            selected["indicator"].style().unpolish(selected["indicator"])
            selected["indicator"].style().polish(selected["indicator"])

            selected["button"].style().unpolish(selected["button"])
            selected["button"].style().polish(selected["button"])

        # clear side panel
        self.clear_side_panel()

        # title
        title = QLabel(self.get_section_title(section))
        title.setObjectName("sideTitle")
        self.side_layout.addWidget(title)

        # Load proper widget in middle panel
        if section == "esrb":
            widget = EsrbsListWidget()
            widget.setObjectName("middleListWidget")
            self.side_layout.addWidget(widget)

        elif section == "book":
            self.add_middle_button("View All Books", "books")
            self.add_middle_button("Add Book", "add book")
            self.add_middle_button("Edit Book", "edit book")
            self.add_middle_button("Delete Book", "delete book")
            self.add_middle_button("Search Book", "search book")

        elif section == "author":
            self.add_middle_button("View All Authors", "authors")
            self.add_middle_button("Add Author", "add author")
            self.add_middle_button("Edit Author", "edit author")
            self.add_middle_button("Delete Author", "delete author")
            self.add_middle_button("Search Author", "search author")

        elif section == "genre":
            self.add_middle_button("View All Genres", "genres")
            self.add_middle_button("Add Genre", "add genre")
            self.add_middle_button("Edit Genre", "edit genre")
            self.add_middle_button("Delete Genre", "delete genre")
            self.add_middle_button("Search Genre", "search genre")

        elif section == "language":
            self.add_middle_button("View All Languages", "languages")
            self.add_middle_button("Add Language", "add language")
            self.add_middle_button("Edit Language", "edit language")
            self.add_middle_button("Delete Language", "delete language")
            self.add_middle_button("Search Language", "search language")

        elif section == "publisher":
            self.add_middle_button("View All Publishers", "publishers")
            self.add_middle_button("Add Publisher", "add publisher")
            self.add_middle_button("Edit Publisher", "edit publisher")
            self.add_middle_button("Delete Publisher", "delete publisher")
            self.add_middle_button("Search Publisher", "search publisher")

        elif section == "translator":
            self.add_middle_button("View All Translators", "translators")
            self.add_middle_button("Add Translator", "add translator")
            self.add_middle_button("Edit Translator", "edit translator")
            self.add_middle_button("Delete Translator", "delete translator")
            self.add_middle_button("Search Translator", "search translator")

        elif section == "resource":
            self.add_middle_button("View All Resources", "resources")
            self.add_middle_button("Add Resource", "add resource")
            self.add_middle_button("Edit Resource", "edit resource")
            self.add_middle_button("Delete Resource", "delete resource")
            self.add_middle_button("Search Resource", "search resource")

        else:
            coming_soon = QLabel("Coming soon...")
            coming_soon.setObjectName("sidePlaceholder")
            self.side_layout.addWidget(coming_soon)

        self.side_layout.addStretch()

        # update content panel title
        self.change_content(section)

    # =========================================================
    # Side Panel Helpers
    # =========================================================

    def clear_side_panel(self):
        while self.side_layout.count():
            item = self.side_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    def add_middle_button(self, title, content_key):
        btn = QPushButton(title)
        btn.setObjectName("middleListButton")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)

        btn.clicked.connect(
            lambda checked, text=content_key: self.change_content(text)
        )

        self.side_layout.addWidget(btn)

    def get_section_title(self, section):
        titles = {
            "book": "Books",
            "author": "Authors",
            "translator": "Translators",
            "language": "Languages",
            "publisher": "Publishers",
            "genre": "Genres",
            "resource": "Resources",
            "esrb": "ESRB Ratings",
        }

        return titles.get(section, section.capitalize())

    # =========================================================
    # Content Change
    # =========================================================

    def change_content(self, text):
        self.content_label.setText(f"{text.title()} View")

    # =========================================================
    # Theme Handlers
    # =========================================================

    def apply_dark_theme(self):
        self.current_theme = "dark"
        self.setStyleSheet(DARK_THEME)
        self.update_sidebar_icons() # آیکون‌ها سفید می‌شوند
        self.refresh_dynamic_styles()

    def apply_light_theme(self):
        self.current_theme = "light"
        self.setStyleSheet(LIGHT_THEME)
        self.update_sidebar_icons() # آیکون‌ها مشکی می‌شوند
        self.refresh_dynamic_styles()

    def refresh_dynamic_styles(self):
        """
        وقتی property هایی مثل active تغییر می‌کنند،
        برای اعمال دوباره stylesheet باید polish/unpolish انجام شود.
        """

        for item in self.sidebar_buttons.values():

            indicator = item["indicator"]
            button = item["button"]

            indicator.style().unpolish(indicator)
            indicator.style().polish(indicator)

            button.style().unpolish(button)
            button.style().polish(button)

    # =========================================================
    # Icons Handlers
    # =========================================================

    # ۳. اصلاح متد رنگ‌آمیزی SVG (برای جلوگیری از خطای رندرینگ):
    def get_colored_icon(self, icon_name, color_hex):
        icon_path = os.path.join(self.icons_dir, icon_name)
        if not os.path.exists(icon_path):
            return None

        try:
            with open(icon_path, 'r', encoding='utf-8') as f:
                svg_data = f.read()

            import re
            # جایگزینی هوشمندانه رنگ‌ها
            if 'fill=' in svg_data:
                svg_data = re.sub(r'fill="[^"]+"', f'fill="{color_hex}"', svg_data)
            else:
                svg_data = svg_data.replace('<svg ', f'<svg fill="{color_hex}" ')

            if 'stroke=' in svg_data:
                svg_data = re.sub(r'stroke="[^"]+"', f'stroke="{color_hex}"', svg_data)

            renderer = QSvgRenderer(QByteArray(svg_data.encode('utf-8')))
            pixmap = QPixmap(QSize(24, 24))
            pixmap.fill(Qt.GlobalColor.transparent)
            

            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            
            return QIcon(pixmap)
        except Exception as e:
            print(f"Error coloring icon {icon_name}: {e}")
            return None

    
    def update_sidebar_icons(self):
        icon_color = "#FFFFFF" if self.current_theme == "dark" else "#000000"
        
        for btn_id, item in self.sidebar_buttons.items():
            btn_obj = item["button"]      # دسترسی درست به شیء دکمه
            icon_file = item["icon_name"] # دسترسی به نام فایل آیکون
            
            new_icon = self.get_colored_icon(icon_file, icon_color)
            
            if new_icon:
                btn_obj.setIcon(new_icon)
                btn_obj.setText("")
            else:
                # پیدا کردن فالبک از لیست اولیه یا استفاده از دو حرف اول
                btn_obj.setText(btn_id[:2].upper())


# =========================================================
# Application Start
# =========================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
