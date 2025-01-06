# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-sum.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 591, 831))
        self.frame.setStyleSheet(u"color: white;\n"
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
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 30, 501, 103))
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
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 140, 521, 171))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.sum = QLabel(self.frame_2)
        self.sum.setObjectName(u"sum")
        self.sum.setGeometry(QRect(-30, 40, 251, 91))
        self.sum.setFont(font)
        self.sum.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.sum.setScaledContents(False)
        self.sum.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sum.setWordWrap(False)
        self.rub = QLabel(self.frame_2)
        self.rub.setObjectName(u"rub")
        self.rub.setGeometry(QRect(180, 30, 101, 101))
        self.rub.setFont(font)
        self.rub.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.rub.setScaledContents(False)
        self.rub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rub.setWordWrap(False)
        self.nextButton = QPushButton(self.frame_2)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(290, 40, 201, 91))
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"                background-color:  rgba(255, 255, 255, 0.2); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"                border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 */\n"
"                color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"                padding: 20px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"                font-size: 22px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 330, 521, 321))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.time1 = QLabel(self.frame_3)
        self.time1.setObjectName(u"time1")
        self.time1.setGeometry(QRect(80, 10, 201, 91))
        self.time1.setFont(font)
        self.time1.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.time1.setScaledContents(False)
        self.time1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time1.setWordWrap(False)
        self.time2 = QLabel(self.frame_3)
        self.time2.setObjectName(u"time2")
        self.time2.setGeometry(QRect(80, 160, 201, 91))
        self.time2.setFont(font)
        self.time2.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.time2.setScaledContents(False)
        self.time2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time2.setWordWrap(False)
        self.el2 = QLabel(self.frame_3)
        self.el2.setObjectName(u"el2")
        self.el2.setGeometry(QRect(40, 80, 21, 141))
        self.el2.setStyleSheet(u"color: white;\n"
"background: white;\n"
"")
        self.el3 = QLabel(self.frame_3)
        self.el3.setObjectName(u"el3")
        self.el3.setGeometry(QRect(30, 200, 41, 41))
        self.el3.setStyleSheet(u"color: white;\n"
"background: white;\n"
"\n"
"border-radius: 20px;")
        self.el1 = QLabel(self.frame_3)
        self.el1.setObjectName(u"el1")
        self.el1.setGeometry(QRect(30, 60, 41, 41))
        self.el1.setStyleSheet(u"color: white;\n"
"background: white;\n"
"\n"
"border-radius: 20px;")
        self.date1 = QLabel(self.frame_3)
        self.date1.setObjectName(u"date1")
        self.date1.setGeometry(QRect(90, 80, 211, 81))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.date1.setFont(font1)
        self.date1.setStyleSheet(u"\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.date1.setScaledContents(False)
        self.date1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date1.setWordWrap(False)
        self.city1 = QLabel(self.frame_3)
        self.city1.setObjectName(u"city1")
        self.city1.setGeometry(QRect(250, 10, 251, 91))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.city1.setFont(font2)
        self.city1.setStyleSheet(u"\n"
"font-size: 25pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.city1.setScaledContents(False)
        self.city1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city1.setWordWrap(False)
        self.city2 = QLabel(self.frame_3)
        self.city2.setObjectName(u"city2")
        self.city2.setGeometry(QRect(260, 160, 251, 91))
        self.city2.setFont(font2)
        self.city2.setStyleSheet(u"\n"
"font-size: 25pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.city2.setScaledContents(False)
        self.city2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city2.setWordWrap(False)
        self.date2 = QLabel(self.frame_3)
        self.date2.setObjectName(u"date2")
        self.date2.setGeometry(QRect(90, 230, 211, 81))
        self.date2.setFont(font1)
        self.date2.setStyleSheet(u"\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.date2.setScaledContents(False)
        self.date2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date2.setWordWrap(False)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 670, 531, 141))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.booking_12 = QLabel(self.frame_4)
        self.booking_12.setObjectName(u"booking_12")
        self.booking_12.setGeometry(QRect(0, -20, 501, 101))
        self.booking_12.setFont(font)
        self.booking_12.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.booking_12.setScaledContents(False)
        self.booking_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.booking_12.setWordWrap(False)
        self.booking_13 = QLabel(self.frame_4)
        self.booking_13.setObjectName(u"booking_13")
        self.booking_13.setGeometry(QRect(50, 50, 211, 81))
        self.booking_13.setFont(font1)
        self.booking_13.setStyleSheet(u"\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.booking_13.setScaledContents(False)
        self.booking_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.booking_13.setWordWrap(False)
        self.booking_14 = QLabel(self.frame_4)
        self.booking_14.setObjectName(u"booking_14")
        self.booking_14.setGeometry(QRect(200, 50, 211, 91))
        self.booking_14.setFont(font1)
        self.booking_14.setStyleSheet(u"\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
" /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.booking_14.setScaledContents(False)
        self.booking_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.booking_14.setWordWrap(False)

        self.retranslateUi(Dialog)

        self.nextButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.sum.setText(QCoreApplication.translate("Dialog", u"10000", None))
        self.rub.setText(QCoreApplication.translate("Dialog", u"\u0440.", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.time1.setText(QCoreApplication.translate("Dialog", u"Time1", None))
        self.time2.setText(QCoreApplication.translate("Dialog", u"Time2", None))
        self.el2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.el3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.el1.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.date1.setText(QCoreApplication.translate("Dialog", u"Date1", None))
        self.city1.setText(QCoreApplication.translate("Dialog", u"City1", None))
        self.city2.setText(QCoreApplication.translate("Dialog", u"City2", None))
        self.date2.setText(QCoreApplication.translate("Dialog", u"Date2", None))
        self.booking_12.setText(QCoreApplication.translate("Dialog", u"City1 - City2", None))
        self.booking_13.setText(QCoreApplication.translate("Dialog", u"Time3 ", None))
        self.booking_14.setText(QCoreApplication.translate("Dialog", u"\u0432 \u043f\u0443\u0442\u0438", None))
    # retranslateUi

