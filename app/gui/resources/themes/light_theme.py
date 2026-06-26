LIGHT_THEME = """
/* ==========================================================================
   Global
   ========================================================================== */

QMainWindow {
    background-color: #f3f3f3;
    color: #202124;
}

#centralWidget {
    background-color: #f3f3f3;
    color: #202124;
}

QWidget {
    font-family: "Segoe UI";
    font-size: 10pt;
    color: #202124;
}


/* ==========================================================================
   Menu Bar
   ========================================================================== */

#mainMenuBar {
    background-color: #ffffff;
    color: #202124;
    border-bottom: 1px solid #dcdcdc;
}

#mainMenuBar::item {
    background-color: transparent;
    color: #202124;
    padding: 6px 14px;
}

#mainMenuBar::item:selected {
    background-color: #e8e8e8;
}

#mainMenuBar::item:pressed {
    background-color: #dcdcdc;
}

QMenu {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #dcdcdc;
    padding: 4px;
}

QMenu::item {
    padding: 7px 28px 7px 24px;
    background-color: transparent;
}

QMenu::item:selected {
    background-color: #e8f0fe;
    color: #1a73e8;
}

QMenu::separator {
    height: 1px;
    background-color: #dcdcdc;
    margin: 4px 8px;
}


/* ==========================================================================
   Activity Bar
   ========================================================================== */

#activityBar {
    background-color: #f8f9fa;
    border-right: 1px solid #dcdcdc;
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
    background-color: #1a73e8;
    border-radius: 1px;
}

#activityButton {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    padding: 0px;
}

#activityButton:hover {
    background-color: #e8e8e8;
}

#activityButton[active="true"] {
    background-color: #dadce0;
}


/* ==========================================================================
   Side Panel
   ========================================================================== */

#sidePanel {
    background-color: #ffffff;
    border-right: 1px solid #dcdcdc;
}

#sideTitle {
    color: #3c4043;
    font-size: 10pt;
    font-weight: 500;
    padding: 0px 0px 6px 0px;
}
#panelsContainer { background-color: #f3f3f3; }

#activityScrollArea, #activityScrollArea > QWidget {
    background-color: #f8f9fa;
    border: none;
}


/* ==========================================================================
   Middle List Buttons
   ========================================================================== */

#middleListButton {
    background-color: #f1f3f4;
    color: #3c4043;
    border: 1px solid #dadce0;
    border-radius: 4px;
    padding: 6px 10px;
    text-align: center;
}

#middleListButton:hover {
    background-color: #e8eaed;
    color: #202124;
    border: 1px solid #bdc1c6;
}

#middleListButton:pressed {
    background-color: #dadce0;
}

#middleListButton:disabled {
    background-color: #f8f9fa;
    color: #9aa0a6;
    border: 1px solid #e8eaed;
}


/* ==========================================================================
   Content Panel
   ========================================================================== */

#contentPanel {
    background-color: #f3f3f3;
    border: none;
}

#contentTitle {
    color: #202124;
    font-size: 10pt;
}

#contentWidget {
    background-color: #f3f3f3;
    color: #202124;
}


/* ==========================================================================
   General Controls
   ========================================================================== */

QLabel {
    color: #202124;
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
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #dadce0;
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
    border: 1px solid #1a73e8;
}

QTableWidget,
QTableView,
QTreeWidget,
QTreeView,
QListWidget,
QListView {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #dcdcdc;
    gridline-color: #dcdcdc;
    selection-background-color: #e8f0fe;
    selection-color: #1a73e8;
}

QHeaderView::section {
    background-color: #f8f9fa;
    color: #3c4043;
    border: 1px solid #dcdcdc;
    padding: 6px;
}

QScrollBar:vertical {
    background-color: #f3f3f3;
    width: 12px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #c1c1c1;
    min-height: 24px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #a8a8a8;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #f3f3f3;
    height: 12px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #c1c1c1;
    min-width: 24px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #a8a8a8;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}

#activityScrollContent {
    background-color: #f8f9fa;
}

#activityScrollArea QWidget#qt_scrollarea_viewport {
    background-color: #f8f9fa;
}

#sidePanel > QWidget {
    background-color: #ffffff;
}

"""
