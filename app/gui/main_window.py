import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QAction, QPushButton, QLineEdit, QMenu
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Layout Task")
        self.resize(1000, 600)

        # -----------------------------
        # Menu bar
        # -----------------------------
        menubar = self.menuBar()

        books_menu = menubar.addMenu("Books")
        for i in ["add view","serach","add","edit","delete"]:
            books_menu.addAction(i)

        data_menu = menubar.addMenu("Data")
        for i in ["author","esrb","genre","language","publisher","resource","translator"]:
            data_menu.addAction(i)

        rent_menu = menubar.addMenu("Rent")
        for i in ["issue book","return book","all rental","over due","new"]:
            rent_menu.addAction(i)

        setting_menu = menubar.addMenu("Setting")
        for i in [""]:
            setting_menu.addAction(i)

        help_menu = menubar.addMenu("Help")
        for i in ["guide","exit"]:
            help_menu.addAction(i)


        # -----------------------------
        # Central widget
        # -----------------------------
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =========================================================
        # 1) Left narrow white strip
        # =========================================================
        self.left_bar = QWidget()
        self.left_bar.setFixedWidth(65)
        self.left_bar.setStyleSheet("background-color: white;")

        left_bar_layout = QVBoxLayout(self.left_bar)
        left_bar_layout.setContentsMargins(5, 10, 5, 10)
        left_bar_layout.setSpacing(6)
        left_bar_layout.setAlignment(Qt.AlignTop)
        for i in ["A","B","C"]:
            left_bar_btn=QPushButton(i)
            left_bar_btn.setFixedSize(50, 32)
            left_bar_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid #444;
                background-color: #f5f5f5;
                font-size: 12px;
            }
        """)
            left_bar_layout.addWidget(left_bar_btn)

        # =========================================================
        # 2) Middle light blue panel
        # =========================================================
        self.middle_panel = QWidget()
        self.middle_panel.setFixedWidth(200)
        self.middle_panel.setStyleSheet("background-color: #B8D7EA;")

        middle_layout = QVBoxLayout(self.middle_panel)
        middle_layout.setContentsMargins(20, 35, 20, 20)
        middle_layout.setSpacing(12)
        middle_layout.setAlignment(Qt.AlignTop)

        self.btn_books = QPushButton("Books")
        self.btn_authors = QPushButton("Authors")

        for btn in (self.btn_books, self.btn_authors):
            btn.setFixedHeight(30)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #D7E7F2;
                    border: 1px solid #4A6572;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #C9DDEA;
                }
            """)

        middle_layout.addWidget(self.btn_books)
        middle_layout.addWidget(self.btn_authors)

        # =========================================================
        # 3) Right pink panel with form
        # =========================================================
        self.right_panel = QWidget()
        self.right_panel.setStyleSheet("background-color: #F6C4BC;")

        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(120, 80, 120, 20)
        right_layout.setSpacing(14)
        right_layout.setAlignment(Qt.AlignTop)

        # Title row
        title_row = QHBoxLayout()
        lbl_title = QLabel("Title:")
        edit_title = QLineEdit()
        edit_title.setFixedHeight(28)

        lbl_title.setFixedWidth(75)
        title_row.addWidget(lbl_title)
        title_row.addWidget(edit_title)

        # Publisher row
        publisher_row = QHBoxLayout()
        lbl_publisher = QLabel("Publisher:")
        edit_publisher = QLineEdit()
        edit_publisher.setFixedHeight(28)

        lbl_publisher.setFixedWidth(75)
        publisher_row.addWidget(lbl_publisher)
        publisher_row.addWidget(edit_publisher)

        # OK button
        btn_ok = QPushButton("OK")
        btn_ok.setFixedSize(90, 28)
        btn_ok.setStyleSheet("""
            QPushButton {
                background-color: #E8D2D0;
                border: 1px solid #7A5A5A;
                font-size: 12px;
            }
        """)

        right_layout.addLayout(title_row)
        right_layout.addLayout(publisher_row)
        right_layout.addWidget(btn_ok, alignment=Qt.AlignLeft)

        # -----------------------------
        # Add panels to main layout
        # -----------------------------
        main_layout.addWidget(self.left_bar)
        main_layout.addWidget(self.middle_panel)
        main_layout.addWidget(self.right_panel, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
