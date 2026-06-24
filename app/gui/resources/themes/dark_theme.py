DARK_THEME = """
/* ==========================================================================
   Global
   ========================================================================== */

QMainWindow {
    background-color: #1e1e1e;
    color: #d4d4d4;
}

#centralWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
}

QWidget {
    font-family: "Segoe UI";
    font-size: 10pt;
    color: #d4d4d4;
}


/* ==========================================================================
   Menu Bar
   ========================================================================== */

#mainMenuBar {
    background-color: #2d2d30;
    color: #ffffff;
    border-bottom: 1px solid #3c3c3c;
}

#mainMenuBar::item {
    background-color: transparent;
    color: #ffffff;
    padding: 6px 14px;
}

#mainMenuBar::item:selected {
    background-color: #3e3e42;
}

#mainMenuBar::item:pressed {
    background-color: #505050;
}

QMenu {
    background-color: #252526;
    color: #ffffff;
    border: 1px solid #3c3c3c;
    padding: 4px;
}

QMenu::item {
    padding: 7px 28px 7px 24px;
    background-color: transparent;
}

QMenu::item:selected {
    background-color: #094771;
}

QMenu::separator {
    height: 1px;
    background-color: #3c3c3c;
    margin: 4px 8px;
}


/* ==========================================================================
   Activity Bar
   ========================================================================== */

#activityBar {
    background-color: #1b1b1c;
    border-right: 1px solid #333333;
}

#activityButtonContainer {
    background-color: transparent;
    border: none;
}

#activityButtonContainer[active="true"] {
    background-color: transparent;
}

#activityIndicator {
    background-color: transparent;
    border: none;
}

#activityIndicator[active="true"] {
    background-color: #ffffff;
    border-radius: 1px;
}

#activityButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    padding: 0px;
}

#activityButton:hover {
    background-color: #2a2a2c;
}

#activityButton[active="true"] {
    background-color: #333337;
}


/* ==========================================================================
   Side Panel
   ========================================================================== */

#sidePanel {
    background-color: #252526;
    border-right: 1px solid #3c3c3c;
}

#sideTitle {
    color: #eeeeee;
    font-size: 10pt;
    font-weight: 500;
    padding: 0px 0px 6px 0px;
}


/* ==========================================================================
   Middle List Buttons
   ========================================================================== */

#middleListButton {
    background-color: #303030;
    color: #dddddd;
    border: 1px solid #3f3f46;
    border-radius: 4px;
    padding: 6px 10px;
    text-align: center;
}

#middleListButton:hover {
    background-color: #3a3a3a;
    color: #ffffff;
    border: 1px solid #555555;
}

#middleListButton:pressed {
    background-color: #454545;
}

#middleListButton:disabled {
    background-color: #2a2a2a;
    color: #777777;
    border: 1px solid #333333;
}


/* ==========================================================================
   Content Panel
   ========================================================================== */

#contentPanel {
    background-color: #1e1e1e;
    border: none;
}

#contentTitle {
    color: #d4d4d4;
    font-size: 10pt;
}

#contentWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
}


/* ==========================================================================
   General Controls
   ========================================================================== */

QLabel {
    color: #d4d4d4;
}

QPushButton {
    outline: none;
}

QLineEdit,
QTextEdit,
QPlainTextEdit,
QComboBox,
QSpinBox,
QDoubleSpinBox,
QDateEdit {
    background-color: #2d2d30;
    color: #ffffff;
    border: 1px solid #3f3f46;
    border-radius: 4px;
    padding: 5px 8px;
}

QLineEdit:focus,
QTextEdit:focus,
QPlainTextEdit:focus,
QComboBox:focus,
QSpinBox:focus,
QDoubleSpinBox:focus,
QDateEdit:focus {
    border: 1px solid #007acc;
}

QTableWidget,
QTableView,
QTreeWidget,
QTreeView,
QListWidget,
QListView {
    background-color: #1e1e1e;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    gridline-color: #3c3c3c;
    selection-background-color: #094771;
    selection-color: #ffffff;
}

QHeaderView::section {
    background-color: #2d2d30;
    color: #ffffff;
    border: 1px solid #3c3c3c;
    padding: 6px;
}

QScrollBar:vertical {
    background-color: #1e1e1e;
    width: 12px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #424242;
    min-height: 24px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #555555;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #1e1e1e;
    height: 12px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #424242;
    min-width: 24px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #555555;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}
"""
