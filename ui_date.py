# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-date.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 835)
        Dialog.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread: pad,\n"
"    x1: 1, y1: 1,\n"
"    x2: 0, y2: 0,\n"
"    stop: 0 rgba(0, 191, 255, 255), /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"    stop: 0.5 rgba(0, 0, 255, 255), /* \u0421\u0438\u043d\u0438\u0439 */\n"
"    stop: 1 rgba(0, 191, 255, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
");\n"
"")
        self.frame1 = QFrame(Dialog)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(10, 0, 591, 831))
        self.frame1.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"\n"
"\n"
" background-color:  rgba(255, 255, 255, 0.2); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"                border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 */\n"
"                color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"                padding: 20px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"                font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"                border-radius: 30px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"padding: 25px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.frame1)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding: 25px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(False)

        self.verticalLayout.addWidget(self.title)

        self.calendarWidget = QCalendarWidget(self.frame1)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QAbstractItemView {\n"
"    font-size: 25px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u043c\u0435\u0441\u044f\u0446\u0435\u0432 \u0441 \u0438\u043a\u043e\u043d\u043a\u0430\u043c\u0438 */\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth,\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    icon-size: 0px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u043a\u043e\u043d\u043e\u043a */\n"
"	\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.calendarWidget)

        self.info = QLabel(self.frame1)
        self.info.setObjectName(u"info")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding: 25px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.info)

        self.nextButton = QPushButton(self.frame1)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"                background-color:  rgba(255, 255, 255, 0.2); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"                border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 */\n"
"                color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"                padding: 20px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"                font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"                border-radius: 15px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* \u0422\u0435\u043d\u044c */\n"
"                transition: background-color 0.3s, transform 0.3s; /* \u041f\u043b\u0430\u0432\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u0445\u043e\u0434 */\n"
"            }"
                        "\n"
"            QPushButton:hover {\n"
"                background-color: rgba(255, 255, 255, 0.2); /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"                transform: translateY(-2px); /* \u041f\u043e\u0434\u044a\u0435\u043c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgba(255, 255, 255, 0.1); /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"                transform: translateY(1px); /* \u042d\u0444\u0444\u0435\u043a\u0442 \u043d\u0430\u0436\u0430\u0442\u0438\u044f */\n"
"            }")
        self.nextButton.setAutoDefault(False)
        self.nextButton.setFlat(False)

        self.verticalLayout.addWidget(self.nextButton)


        self.retranslateUi(Dialog)

        self.nextButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.info.setText(QCoreApplication.translate("Dialog", u"\u0427\u0435\u043c \u0440\u0430\u043d\u044c\u0448\u0435 \u0432\u044b \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u043b\u0438 \u0431\u0438\u043b\u0435\u0442, \n"
" \u0442\u0435\u043c \u0434\u0435\u0448\u0435\u0432\u043b\u0435 \u043e\u043d \u043e\u0431\u043e\u0439\u0434\u0435\u0442\u0441\u044f \u0432 \u0446\u0435\u043d\u0435.", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u" \u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

