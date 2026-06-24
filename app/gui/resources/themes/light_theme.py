LIGHT_THEME = """
/* ==========================================================================
   Global
   ========================================================================== */

QMainWindow {
    background-color: #ffffff;
    color: #202124;
}

#centralWidget {
    background-color: #ffffff;
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
    background-color: #eeeeee;
}

#mainMenuBar::item:pressed {
    background-color: #e0e0e0;
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
    color: #202124;
}

QMenu::item:selected {
    background-color: #e8f0fe;
    color: #174ea6;
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
    background-color: #f1f1f1;
    border-right: 1px solid #d0d0d0;
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
    background-color: #e0e0e0;
}

#activityButton[active="true"] {
    background-color: #dcdcdc;
}


/* ==========================================================================
   Side Panel
   ========================================================================== */

#sidePanel {
    background-color: #f7f7f7;
    border-right: 1px solid #dcdcdc;
}

#sideTitle {
    color: #202124;
    font-size: 10pt;
    font-weight: 500;
    padding: 0px 0px 6px 0px;
}


/* ==========================================================================
   Middle List Buttons
   ========================================================================== */

#middleListButton {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    padding: 6px 10px;
    text-align: center;
}

#middleListButton:hover {
    background-color: #e8f0fe;
    color: #174ea6;
    border: 1px solid #1a73e8;
}

#middleListButton:pressed {
    background-color: #d2e3fc;
}

#middleListButton:disabled {
    background-color: #eeeeee;
    color: #999999;
    border: 1px solid #dddddd;
}


/* ==========================================================================
   Content Panel
   ========================================================================== */

#contentPanel {
    background-color: #ffffff;
    border: none;
}

#contentTitle {
    color: #202124;
    font-size: 10pt;
}

#contentWidget {
    background-color: #ffffff;
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
QDateE"""