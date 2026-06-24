LIGHT_THEME = """/*
    NEW MODERN LIGHT THEME
    Focus: High Contrast, Clean Lists, No Inversion issues
*/

/* تنظیمات پایه برای کل اپلیکیشن */
QWidget {
    background-color: #FFFFFF;
    color: #202124;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}

/* منوبار بالا */
QMenuBar {
    background-color: #F8F9FA;
    border-bottom: 1px solid #E0E0E0;
    padding: 2px;
}
QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #E8F0FE; /* آبی بسیار ملایم گوگل */
}

/* نوار ابزار سمت چپ (Activity Bar) */
#activityBar {
    background-color: #F1F3F4;
    border-right: 1px solid #DADCE0;
}
#activityButton {
    background-color: transparent;
    border: none;
    border-radius: 5px;
    margin: 4px;
}
#activityButton:hover {
    background-color: #E8EAED;
}
#activityButton[active="true"] {
    background-color: #FFFFFF;
}
#activityIndicator[active="true"] {
    background-color: #1A73E8; /* آبی اصلی برند */
}

/* پنل میانی (Side Panel) */
#sidePanel {
    background-color: #F8F9FA;
    border-right: 1px solid #DADCE0;
}
#sideTitle {
    color: #5F6368;
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
    padding: 10px;
}

/* --- رفع مشکل اساسی لیست ESRB و سایر لیست‌ها --- */
QListWidget {
    background-color: #FFFFFF;
    border: none;
    outline: none; /* حذف خط تیره دور کل لیست */
}

QListWidget::item {
    padding: 12px 15px;
    border-bottom: 1px solid #F1F3F4;
    color: #3C4043;
}

/* حالت هاور: جایگزین شدن رنگ مشکی با خاکستری بسیار روشن */
QListWidget::item:hover {
    background-color: #F8F9FA;
    color: #202124;
}

/* حالت انتخاب شده: متن آبی روی پس‌زمینه آبی روشن */
QListWidget::item:selected {
    background-color: #E8F0FE;
    color: #1A73E8;
    font-weight: 500;
}

/* وقتی فوکوس از روی لیست برداشته می‌شود هم رنگ ثابت بماند */
QListWidget::item:selected:active, QListWidget::item:selected:!active {
    background-color: #E8F0FE;
    color: #1A73E8;
}

/* اسکرول‌بار مدرن و ظریف */
QScrollBar:vertical {
    background: transparent;
    width: 6px;
    margin: 0;
}
QScrollBar::handle:vertical {
    background: #DADCE0;
    border-radius: 3px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background: #BDC1C6;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

/* محیط محتوا (سمت راست) */
#contentPanel {
    background-color: #FFFFFF;
}
#contentTitle {
    color: #202124;
    font-size: 18px;
}
"""
