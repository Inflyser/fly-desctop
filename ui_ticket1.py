# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-ticket.ui'
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
import res_rc

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
        self.frame.setGeometry(QRect(0, 0, 611, 831))
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
        self.title.setGeometry(QRect(60, 110, 471, 231))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setStyleSheet(u"\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(False)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 360, 611, 361))
        self.frame_2.setStyleSheet(u"color: white;\n"
"background: white;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 611, 141))
        self.frame_3.setStyleSheet(u"color: #0088ff;\n"
"background: #0088ff;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.name_firm = QLabel(self.frame_3)
        self.name_firm.setObjectName(u"name_firm")
        self.name_firm.setGeometry(QRect(0, -10, 151, 71))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.name_firm.setFont(font1)
        self.name_firm.setStyleSheet(u"color: white;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.name_firm.setScaledContents(False)
        self.name_firm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_firm.setWordWrap(False)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, 50, 621, 281))
        self.frame_4.setStyleSheet(u"color: white;\n"
"background: white;\n"
"border-radius: 0px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.title_3 = QLabel(self.frame_4)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(20, -10, 171, 71))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.title_3.setFont(font2)
        self.title_3.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_3.setScaledContents(False)
        self.title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_3.setWordWrap(False)
        self.title_4 = QLabel(self.frame_4)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(150, -10, 171, 71))
        self.title_4.setFont(font2)
        self.title_4.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_4.setScaledContents(False)
        self.title_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_4.setWordWrap(False)
        self.title_5 = QLabel(self.frame_4)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setGeometry(QRect(270, -10, 171, 71))
        self.title_5.setFont(font2)
        self.title_5.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_5.setScaledContents(False)
        self.title_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_5.setWordWrap(False)
        self.title_6 = QLabel(self.frame_4)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setGeometry(QRect(430, -10, 191, 71))
        self.title_6.setFont(font2)
        self.title_6.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_6.setScaledContents(False)
        self.title_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_6.setWordWrap(False)
        self.number = QLabel(self.frame_4)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(160, 20, 151, 71))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.number.setFont(font3)
        self.number.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.number.setScaledContents(False)
        self.number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number.setWordWrap(False)
        self.date1 = QLabel(self.frame_4)
        self.date1.setObjectName(u"date1")
        self.date1.setGeometry(QRect(260, 10, 201, 101))
        self.date1.setFont(font3)
        self.date1.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.date1.setScaledContents(False)
        self.date1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date1.setWordWrap(False)
        self.time1 = QLabel(self.frame_4)
        self.time1.setObjectName(u"time1")
        self.time1.setGeometry(QRect(440, 20, 151, 71))
        self.time1.setFont(font3)
        self.time1.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.time1.setScaledContents(False)
        self.time1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time1.setWordWrap(False)
        self.title_11 = QLabel(self.frame_4)
        self.title_11.setObjectName(u"title_11")
        self.title_11.setGeometry(QRect(10, 80, 211, 71))
        self.title_11.setFont(font2)
        self.title_11.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_11.setScaledContents(False)
        self.title_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_11.setWordWrap(False)
        self.title_12 = QLabel(self.frame_4)
        self.title_12.setObjectName(u"title_12")
        self.title_12.setGeometry(QRect(170, 80, 211, 71))
        self.title_12.setFont(font2)
        self.title_12.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_12.setScaledContents(False)
        self.title_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_12.setWordWrap(False)
        self.title_13 = QLabel(self.frame_4)
        self.title_13.setObjectName(u"title_13")
        self.title_13.setGeometry(QRect(290, 80, 211, 71))
        self.title_13.setFont(font2)
        self.title_13.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_13.setScaledContents(False)
        self.title_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_13.setWordWrap(False)
        self.title_14 = QLabel(self.frame_4)
        self.title_14.setObjectName(u"title_14")
        self.title_14.setGeometry(QRect(430, 80, 211, 71))
        self.title_14.setFont(font2)
        self.title_14.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_14.setScaledContents(False)
        self.title_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_14.setWordWrap(False)
        self.city1 = QLabel(self.frame_4)
        self.city1.setObjectName(u"city1")
        self.city1.setGeometry(QRect(40, 100, 151, 111))
        self.city1.setFont(font3)
        self.city1.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.city1.setScaledContents(False)
        self.city1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.city1.setWordWrap(False)
        self.city2 = QLabel(self.frame_4)
        self.city2.setObjectName(u"city2")
        self.city2.setGeometry(QRect(200, 100, 151, 111))
        self.city2.setFont(font3)
        self.city2.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.city2.setScaledContents(False)
        self.city2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.city2.setWordWrap(False)
        self.image1 = QPushButton(self.frame_4)
        self.image1.setObjectName(u"image1")
        self.image1.setEnabled(True)
        self.image1.setGeometry(QRect(430, 40, 51, 41))
        font4 = QFont()
        self.image1.setFont(font4)
        self.image1.setToolTipDuration(-1)
        self.image1.setStyleSheet(u"QPashButton {\n"
"padding: 55px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"transform: rotate(90deg);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/fly.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.image1.setIcon(icon)
        self.image1.setIconSize(QSize(30, 30))
        self.image1.setCheckable(False)
        self.image1.setAutoRepeat(False)
        self.image1.setAutoDefault(False)
        self.image1.setFlat(True)
        self.code_exit = QLabel(self.frame_4)
        self.code_exit.setObjectName(u"code_exit")
        self.code_exit.setGeometry(QRect(320, 110, 151, 71))
        self.code_exit.setFont(font3)
        self.code_exit.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.code_exit.setScaledContents(False)
        self.code_exit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.code_exit.setWordWrap(False)
        self.time2 = QLabel(self.frame_4)
        self.time2.setObjectName(u"time2")
        self.time2.setGeometry(QRect(470, 90, 151, 111))
        self.time2.setFont(font1)
        self.time2.setStyleSheet(u"color: black;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.time2.setScaledContents(False)
        self.time2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.time2.setWordWrap(False)
        self.name = QLabel(self.frame_4)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(30, 20, 201, 101))
        self.name.setFont(font3)
        self.name.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.name.setScaledContents(False)
        self.name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.name.setWordWrap(False)
        self.title_22 = QLabel(self.frame_4)
        self.title_22.setObjectName(u"title_22")
        self.title_22.setGeometry(QRect(10, 170, 321, 71))
        self.title_22.setFont(font2)
        self.title_22.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_22.setScaledContents(False)
        self.title_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_22.setWordWrap(False)
        self.title_23 = QLabel(self.frame_4)
        self.title_23.setObjectName(u"title_23")
        self.title_23.setGeometry(QRect(30, 190, 171, 71))
        self.title_23.setFont(font3)
        self.title_23.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_23.setScaledContents(False)
        self.title_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_23.setWordWrap(False)
        self.title_16 = QLabel(self.frame_4)
        self.title_16.setObjectName(u"title_16")
        self.title_16.setGeometry(QRect(0, 210, 211, 71))
        self.title_16.setFont(font2)
        self.title_16.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_16.setScaledContents(False)
        self.title_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_16.setWordWrap(False)
        self.code_pnr = QLabel(self.frame_4)
        self.code_pnr.setObjectName(u"code_pnr")
        self.code_pnr.setGeometry(QRect(20, 230, 151, 71))
        self.code_pnr.setFont(font3)
        self.code_pnr.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.code_pnr.setScaledContents(False)
        self.code_pnr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.code_pnr.setWordWrap(False)
        self.title_19 = QLabel(self.frame_4)
        self.title_19.setObjectName(u"title_19")
        self.title_19.setGeometry(QRect(150, 210, 171, 71))
        self.title_19.setFont(font2)
        self.title_19.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_19.setScaledContents(False)
        self.title_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_19.setWordWrap(False)
        self.title_25 = QLabel(self.frame_4)
        self.title_25.setObjectName(u"title_25")
        self.title_25.setGeometry(QRect(160, 230, 151, 71))
        self.title_25.setFont(font3)
        self.title_25.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_25.setScaledContents(False)
        self.title_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_25.setWordWrap(False)
        self.title_26 = QLabel(self.frame_4)
        self.title_26.setObjectName(u"title_26")
        self.title_26.setGeometry(QRect(390, 180, 171, 71))
        self.title_26.setFont(font2)
        self.title_26.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_26.setScaledContents(False)
        self.title_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_26.setWordWrap(False)
        self.seat = QLabel(self.frame_4)
        self.seat.setObjectName(u"seat")
        self.seat.setGeometry(QRect(440, 190, 151, 111))
        self.seat.setFont(font1)
        self.seat.setStyleSheet(u"color: black;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.seat.setScaledContents(False)
        self.seat.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.seat.setWordWrap(False)
        self.title_28 = QLabel(self.frame_4)
        self.title_28.setObjectName(u"title_28")
        self.title_28.setGeometry(QRect(400, 230, 201, 71))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.title_28.setFont(font5)
        self.title_28.setStyleSheet(u"color: #007bb0;\n"
"font-size: 8pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_28.setScaledContents(False)
        self.title_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_28.setWordWrap(False)
        self.image2 = QPushButton(self.frame_4)
        self.image2.setObjectName(u"image2")
        self.image2.setEnabled(True)
        self.image2.setGeometry(QRect(10, 10, 16, 231))
        self.image2.setFont(font4)
        self.image2.setToolTipDuration(-1)
        self.image2.setStyleSheet(u"QPashButton {\n"
"padding: 55px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"transform: rotate(90deg);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/vsd.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.image2.setIcon(icon1)
        self.image2.setIconSize(QSize(80, 400))
        self.image2.setCheckable(False)
        self.image2.setAutoRepeat(False)
        self.image2.setAutoDefault(False)
        self.image2.setFlat(True)
        self.info = QLabel(self.frame)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(60, 660, 471, 231))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.info.setFont(font6)
        self.info.setStyleSheet(u"\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.info.setScaledContents(False)
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info.setWordWrap(False)
        self.nextButton_2 = QPushButton(self.frame)
        self.nextButton_2.setObjectName(u"nextButton_2")
        self.nextButton_2.setGeometry(QRect(130, 750, 331, 61))
        self.nextButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"                background-color:  rgba(255, 255, 255, 0.2); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"                border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 */\n"
"                color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"                padding: 20px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"                font-size: 20px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"\n"
"\n"
"\n"
"                border-radius: 15px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* \u0422\u0435\u043d\u044c */\n"
"                transition: background-color 0.3s, transform 0.3s; /* \u041f\u043b\u0430\u0432\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u0445\u043e\u0434 "
                        "*/\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgba(255, 255, 255, 0.2); /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"                transform: translateY(-2px); /* \u041f\u043e\u0434\u044a\u0435\u043c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgba(255, 255, 255, 0.1); /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"                transform: translateY(1px); /* \u042d\u0444\u0444\u0435\u043a\u0442 \u043d\u0430\u0436\u0430\u0442\u0438\u044f */\n"
"            }")
        self.nextButton_2.setAutoDefault(False)
        self.nextButton_2.setFlat(False)

        self.retranslateUi(Dialog)

        self.image1.setDefault(False)
        self.image2.setDefault(False)
        self.nextButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0431\u0438\u043b\u0435\u0442", None))
        self.name_firm.setText(QCoreApplication.translate("Dialog", u"Poleta", None))
        self.title_3.setText(QCoreApplication.translate("Dialog", u"Customer / \u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.title_4.setText(QCoreApplication.translate("Dialog", u"Flight / \u0420\u0435\u0439\u0441", None))
        self.title_5.setText(QCoreApplication.translate("Dialog", u"Date / \u0414\u0430\u0442\u0430", None))
        self.title_6.setText(QCoreApplication.translate("Dialog", u"Time / \u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043b\u0435\u0442\u0430", None))
        self.number.setText(QCoreApplication.translate("Dialog", u"Number", None))
        self.date1.setText(QCoreApplication.translate("Dialog", u"Number\n"
"MOTNH", None))
        self.time1.setText(QCoreApplication.translate("Dialog", u"00:00", None))
        self.title_11.setText(QCoreApplication.translate("Dialog", u"Departure / \u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.title_12.setText(QCoreApplication.translate("Dialog", u"Arrival / \u041f\u0440\u0438\u0431\u044b\u0442\u0438\u0435", None))
        self.title_13.setText(QCoreApplication.translate("Dialog", u"Gate / \u0412\u044b\u0445\u043e\u0434", None))
        self.title_14.setText(QCoreApplication.translate("Dialog", u"Gate closed / \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u0434\u043e", None))
        self.city1.setText(QCoreApplication.translate("Dialog", u"LED\n"
"City1", None))
        self.city2.setText(QCoreApplication.translate("Dialog", u"PEE\n"
"City2", None))
        self.image1.setText("")
        self.code_exit.setText(QCoreApplication.translate("Dialog", u"D06", None))
        self.time2.setText(QCoreApplication.translate("Dialog", u"00:00", None))
        self.name.setText(QCoreApplication.translate("Dialog", u"Surname\n"
"Name", None))
        self.title_22.setText(QCoreApplication.translate("Dialog", u"Boarding the plane / \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u043d\u0430 \u0441\u0430\u043c\u043e\u043b\u0435\u0442:", None))
        self.title_23.setText(QCoreApplication.translate("Dialog", u"REAR DOOR", None))
        self.title_16.setText(QCoreApplication.translate("Dialog", u"Pnr / \u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.code_pnr.setText(QCoreApplication.translate("Dialog", u"MPHIFX", None))
        self.title_19.setText(QCoreApplication.translate("Dialog", u"Seq / \u041d\u043e\u043c\u0435\u0440", None))
        self.title_25.setText(QCoreApplication.translate("Dialog", u"28", None))
        self.title_26.setText(QCoreApplication.translate("Dialog", u"Seat / \u041c\u0435\u0441\u0442\u043e", None))
        self.seat.setText(QCoreApplication.translate("Dialog", u"20F", None))
        self.title_28.setText(QCoreApplication.translate("Dialog", u"\u043f\u0435\u0440\u0435\u0441\u0430\u0434\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430", None))
        self.image2.setText("")
        self.info.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u044f\u0442\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u0435\u0442\u0430!", None))
        self.nextButton_2.setText("")
    # retranslateUi

