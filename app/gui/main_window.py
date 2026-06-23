import sys
import os

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QScrollArea, QMenuBar
)

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from app.gui.components.esrb_list import EsrbsListWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Manager")
        self.resize(1200, 700)

        # =========================================================
        # Choose Theme
        # =========================================================

        
        
        # =========================================================
        # Central Widget
        # =========================================================

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # =========================================================
        # Menu Bar
        # =========================================================

        self.menu_bar = QMenuBar()
        main_layout.addWidget(self.menu_bar)

        books_menu = self.menu_bar.addMenu("Books")
        for i in ["View All","Add","Edit","Delete","Search"]:
            books_menu.addAction(QAction(i,self))

        data_menu = self.menu_bar.addMenu("Data")
        for i in ["Author","Genre","Language","Publisher","Translator","Resource","Esrb"]:
            data_menu.addAction(QAction(i,self))

        rent_menu = self.menu_bar.addMenu("Rent")
        for i in ["Issue Book","Return Book","All Rentals","Overdue"]:
            rent_menu.addAction(QAction(i,self))

        settings_menu = self.menu_bar.addMenu("Settings")
        for i in ["Home","Options"]:
            settings_menu.addAction(QAction(i,self))
        # appearance_menu = settings_menu.addMenu("Appearance")

        # dark_action = appearance_menu.addAction("Dark Theme")
        # light_action = appearance_menu.addAction("Light Theme")

        # dark_action.triggered.connect(self.apply_dark_theme)
        # light_action.triggered.connect(self.apply_light_theme)
        help_menu = self.menu_bar.addMenu("Help")
        for i in ["Guide","About","Exit"]:
            help_menu.addAction(QAction(i,self))

        # =========================================================
        # Panels Container
        # =========================================================

        panels = QWidget()
        panels_layout = QHBoxLayout(panels)

        panels_layout.setContentsMargins(0,0,0,0)
        panels_layout.setSpacing(0)

        main_layout.addWidget(panels)

        # =========================================================
        # Panel 1 — Activity Bar
        # =========================================================

        self.activity_bar = QWidget()
        self.activity_bar.setFixedWidth(60)

        self.activity_bar.setStyleSheet("""
        background:#333333;
        border-right:1px solid #3c3c3c;
        """)

        activity_layout = QVBoxLayout(self.activity_bar)
        activity_layout.setContentsMargins(0,10,0,10)
        activity_layout.setSpacing(6)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Sidebar buttons definition
        sidebar_buttons = [
            ("book","Books"),
            ("author","Authors"),
            ("translator","Translators"),
            ("language","Languages"),
            ("publisher","Publishers"),
            ("genre","Genres"),
            ("resource","Resources"),
            ("esrb","ESRB")
        ]

        self.sidebar_buttons = {}

        for btn_id, tooltip in sidebar_buttons:

            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0,0,0,0)
            container_layout.setSpacing(0)

            # indicator
            indicator = QWidget()
            indicator.setFixedWidth(4)
            indicator.setStyleSheet("background:transparent;")

            btn = QPushButton(btn_id[:2].upper())
            btn.setMinimumHeight(42)

            btn.setStyleSheet("""
            QPushButton{
                background:transparent;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#3c3c3c;
            }
            """)

            btn.clicked.connect(lambda checked,b=btn_id:self.on_sidebar_clicked(b))

            container_layout.addWidget(indicator)
            container_layout.addWidget(btn)

            self.sidebar_buttons[btn_id] = indicator

            scroll_layout.addWidget(container)

        scroll_layout.addStretch()

        scroll.setWidget(scroll_content)

        activity_layout.addWidget(scroll)

        # =========================================================
        # Panel 2 — Sidebar List
        # =========================================================

        self.side_panel = QWidget()
        self.side_panel.setFixedWidth(260)

        self.side_panel.setStyleSheet("""
        background:#252526;
        border-right:1px solid #3c3c3c;
        """)

        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(10,10,10,10)

        label = QLabel("Select a section")
        label.setStyleSheet("color:#9da5b4;font-size:14px")

        self.side_layout.addWidget(label)

        # =========================================================
        # Panel 3 — Content Area
        # =========================================================

        self.content_panel = QWidget()
        self.content_panel.setStyleSheet("""
        background:#1e1e1e;
        """)

        content_layout = QVBoxLayout(self.content_panel)

        self.content_label = QLabel("Content Area")
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_label.setStyleSheet("""
        font-size:22px;
        color:#cccccc;
        """)

        content_layout.addWidget(self.content_label)

        # =========================================================
        # Add Panels
        # =========================================================

        panels_layout.addWidget(self.activity_bar)
        panels_layout.addWidget(self.side_panel)
        panels_layout.addWidget(self.content_panel, stretch=1)

    # =========================================================
    # Sidebar Click Logic
    # =========================================================

    def on_sidebar_clicked(self, section):

        # reset indicators
        for ind in self.sidebar_buttons.values():
            ind.setStyleSheet("background:transparent;")

        # activate indicator
        self.sidebar_buttons[section].setStyleSheet("background:#007acc;")

        # clear side panel
        while self.side_layout.count():
            item = self.side_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        # title
        title = QLabel(section.capitalize())
        title.setStyleSheet("""
        font-size:16px;
        color:#ffffff;
        font-weight:bold;
        padding-bottom:6px;
        """)

        self.side_layout.addWidget(title)

        # dummy items
        # for i in range(1,6):

        #     btn = QPushButton(f"{section} item {i}")

        #     btn.setStyleSheet("""
        #     QPushButton{
        #         background:#2d2d2d;
        #         border:1px solid #3c3c3c;
        #         padding:6px;
        #         text-align:left;
        #         border-radius:4px;
        #     }

        #     QPushButton:hover{
        #         background:#094771;
        #     }
        #     """)

        #     btn.clicked.connect(lambda _,t=section:self.change_content(t))

        #     self.side_layout.addWidget(btn)
        if section == "esrb":
            widget = EsrbsListWidget()
            self.side_layout.addWidget(widget)

        self.side_layout.addStretch()

    # =========================================================
    # Content Change
    # =========================================================

    def change_content(self, text):

        self.content_label.setText(f"{text.capitalize()} View")

    # =========================================================
    # Themes
    # =========================================================

    def apply_light_theme(self):

        self.setStyleSheet("""

        QMainWindow{
            background:#f5f6f8;
        }

        /* ===== Menu Bar ===== */

        QMenuBar{
            background:#ffffff;
            color:#222;
            border-bottom:1px solid #dcdcdc;
        }

        QMenuBar::item{
            padding:6px 12px;
            background:transparent;
        }

        QMenuBar::item:selected{
            background:#e8f0fe;
        }

        QMenu{
            background:#ffffff;
            color:#222;
            border:1px solid #dcdcdc;
        }

        QMenu::item:selected{
            background:#e8f0fe;
        }

        /* ===== Activity Bar ===== */

        #activityBar{
            background:#f3f3f3;
            border-right:1px solid #dcdcdc;
        }

        QPushButton{
            border:none;
            padding:8px;
        }

        QPushButton:hover{
            background:#e6e6e6;
        }

        /* ===== Side Panel ===== */

        #sidePanel{
            background:#ffffff;
            border-right:1px solid #dcdcdc;
        }

        /* ===== Content Panel ===== */

        #contentPanel{
            background:#fafafa;
        }

        QLabel{
            color:#222;
        }

        QListWidget{
            background:transparent;
            border:none;
            color:#333;
        }

        QListWidget::item{
            padding:8px;
            border-radius:4px;
        }

        QListWidget::item:hover{
            background:#e8f0fe;
        }

        QListWidget::item:selected{
            background:#c2dbff;
        }

        """)

    def apply_dark_theme(self):

        self.setStyleSheet("""

        QMainWindow{
            background:#1e1e1e;
        }

        QMenuBar{
            background:#2d2d2d;
            color:#ffffff;
            border-bottom:1px solid #3c3c3c;
        }

        QMenuBar::item:selected{
            background:#094771;
        }

        QMenu{
            background:#2d2d2d;
            color:#ffffff;
            border:1px solid #3c3c3c;
        }

        QMenu::item:selected{
            background:#094771;
        }

        #activityBar{
            background:#333333;
        }

        #sidePanel{
            background:#252526;
            border-right:1px solid #3c3c3c;
        }

        #contentPanel{
            background:#1e1e1e;
        }

        QLabel{
            color:#d4d4d4;
        }

        """)

# =========================================================
# Application Start
# =========================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
