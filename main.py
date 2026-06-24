import sys
from PyQt6.QtWidgets import QApplication

from app.gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
      
    # ساخت و نمایش پنجره اصلی
    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())