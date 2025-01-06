# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-edit-last.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1234, 590)
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
        self.frame.setGeometry(QRect(0, 0, 1241, 681))
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
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 200, 611, 371))
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
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.name_firm.setFont(font)
        self.name_firm.setStyleSheet(u"color: white;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.name_firm.setScaledContents(False)
        self.name_firm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_firm.setWordWrap(False)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, 50, 621, 291))
        self.frame_4.setStyleSheet(u"color: white;\n"
"background: white;\n"
"border-radius: 0px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.title_3 = QLabel(self.frame_4)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(20, -10, 171, 71))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_3.setScaledContents(False)
        self.title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_3.setWordWrap(False)
        self.title_5 = QLabel(self.frame_4)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setGeometry(QRect(150, -10, 171, 71))
        self.title_5.setFont(font1)
        self.title_5.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_5.setScaledContents(False)
        self.title_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_5.setWordWrap(False)
        self.title_7 = QLabel(self.frame_4)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setGeometry(QRect(270, -10, 171, 71))
        self.title_7.setFont(font1)
        self.title_7.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_7.setScaledContents(False)
        self.title_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_7.setWordWrap(False)
        self.title_8 = QLabel(self.frame_4)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setGeometry(QRect(430, -10, 191, 71))
        self.title_8.setFont(font1)
        self.title_8.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_8.setScaledContents(False)
        self.title_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_8.setWordWrap(False)
        self.number = QLabel(self.frame_4)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(160, 20, 151, 71))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.number.setFont(font2)
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
        self.date1.setFont(font2)
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
        self.time1.setFont(font2)
        self.time1.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.time1.setScaledContents(False)
        self.time1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time1.setWordWrap(False)
        self.title_15 = QLabel(self.frame_4)
        self.title_15.setObjectName(u"title_15")
        self.title_15.setGeometry(QRect(10, 80, 211, 71))
        self.title_15.setFont(font1)
        self.title_15.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_15.setScaledContents(False)
        self.title_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_15.setWordWrap(False)
        self.title_17 = QLabel(self.frame_4)
        self.title_17.setObjectName(u"title_17")
        self.title_17.setGeometry(QRect(170, 80, 211, 71))
        self.title_17.setFont(font1)
        self.title_17.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_17.setScaledContents(False)
        self.title_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_17.setWordWrap(False)
        self.title_18 = QLabel(self.frame_4)
        self.title_18.setObjectName(u"title_18")
        self.title_18.setGeometry(QRect(290, 80, 211, 71))
        self.title_18.setFont(font1)
        self.title_18.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_18.setScaledContents(False)
        self.title_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_18.setWordWrap(False)
        self.title_19 = QLabel(self.frame_4)
        self.title_19.setObjectName(u"title_19")
        self.title_19.setGeometry(QRect(430, 80, 211, 71))
        self.title_19.setFont(font1)
        self.title_19.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_19.setScaledContents(False)
        self.title_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_19.setWordWrap(False)
        self.city1 = QLabel(self.frame_4)
        self.city1.setObjectName(u"city1")
        self.city1.setGeometry(QRect(50, 100, 151, 111))
        self.city1.setFont(font2)
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
        self.city2.setFont(font2)
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
        font3 = QFont()
        self.image1.setFont(font3)
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
        self.code_exit.setFont(font2)
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
        self.time2.setFont(font)
        self.time2.setStyleSheet(u"color: black;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.time2.setScaledContents(False)
        self.time2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.time2.setWordWrap(False)
        self.name = QLabel(self.frame_4)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(30, 10, 201, 101))
        self.name.setFont(font2)
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
        self.title_22.setFont(font1)
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
        self.title_23.setFont(font2)
        self.title_23.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_23.setScaledContents(False)
        self.title_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_23.setWordWrap(False)
        self.title_20 = QLabel(self.frame_4)
        self.title_20.setObjectName(u"title_20")
        self.title_20.setGeometry(QRect(0, 220, 211, 71))
        self.title_20.setFont(font1)
        self.title_20.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_20.setScaledContents(False)
        self.title_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_20.setWordWrap(False)
        self.code_pnr = QLabel(self.frame_4)
        self.code_pnr.setObjectName(u"code_pnr")
        self.code_pnr.setGeometry(QRect(30, 240, 151, 71))
        self.code_pnr.setFont(font2)
        self.code_pnr.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.code_pnr.setScaledContents(False)
        self.code_pnr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.code_pnr.setWordWrap(False)
        self.title_21 = QLabel(self.frame_4)
        self.title_21.setObjectName(u"title_21")
        self.title_21.setGeometry(QRect(150, 210, 171, 71))
        self.title_21.setFont(font1)
        self.title_21.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_21.setScaledContents(False)
        self.title_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_21.setWordWrap(False)
        self.title_25 = QLabel(self.frame_4)
        self.title_25.setObjectName(u"title_25")
        self.title_25.setGeometry(QRect(160, 230, 151, 71))
        self.title_25.setFont(font2)
        self.title_25.setStyleSheet(u"color: black;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_25.setScaledContents(False)
        self.title_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_25.setWordWrap(False)
        self.title_27 = QLabel(self.frame_4)
        self.title_27.setObjectName(u"title_27")
        self.title_27.setGeometry(QRect(400, 180, 171, 71))
        self.title_27.setFont(font1)
        self.title_27.setStyleSheet(u"color: black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.title_27.setScaledContents(False)
        self.title_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_27.setWordWrap(False)
        self.seat = QLabel(self.frame_4)
        self.seat.setObjectName(u"seat")
        self.seat.setGeometry(QRect(440, 190, 151, 111))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.seat.setFont(font4)
        self.seat.setStyleSheet(u"color: black;\n"
"font-size: 20pt;\n"
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
        self.image2.setFont(font3)
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
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 100, 201, 71))
        self.lineEdit.setFont(font3)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 100, 141, 71))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(370, 100, 141, 71))
        self.lineEdit_3.setFont(font3)
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(520, 100, 211, 71))
        self.lineEdit_4.setFont(font3)
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(1000, 100, 221, 71))
        self.lineEdit_6.setFont(font3)
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(980, 270, 241, 71))
        self.lineEdit_7.setFont(font3)
        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(770, 270, 201, 71))
        self.lineEdit_8.setFont(font3)
        self.lineEdit_9 = QLineEdit(self.frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(980, 440, 241, 71))
        self.lineEdit_9.setFont(font3)
        self.lineEdit_10 = QLineEdit(self.frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(740, 100, 251, 71))
        self.lineEdit_10.setFont(font3)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 201, 71))
        font6 = QFont()
        font6.setBold(True)
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 20, 141, 71))
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 20, 141, 71))
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 20, 211, 71))
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(740, 20, 251, 71))
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1000, 20, 221, 71))
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(980, 190, 241, 71))
        self.label_10.setFont(font6)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(770, 190, 201, 71))
        self.label_11.setFont(font6)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(650, 370, 321, 201))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.nextButton_5 = QPushButton(self.frame_5)
        self.nextButton_5.setObjectName(u"nextButton_5")
        self.nextButton_5.setGeometry(QRect(10, 110, 181, 61))
        self.nextButton_5.setFont(font6)
        self.nextButton_5.setStyleSheet(u"\n"
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
        self.nextButton_5.setAutoDefault(False)
        self.nextButton_5.setFlat(False)
        self.nextButton_4 = QPushButton(self.frame_5)
        self.nextButton_4.setObjectName(u"nextButton_4")
        self.nextButton_4.setGeometry(QRect(10, 30, 181, 61))
        self.nextButton_4.setFont(font6)
        self.nextButton_4.setStyleSheet(u"\n"
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
        self.nextButton_4.setAutoDefault(False)
        self.nextButton_4.setFlat(False)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 70, 111, 71))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(980, 360, 241, 71))
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        self.image1.setDefault(False)
        self.image2.setDefault(False)
        self.nextButton_5.setDefault(False)
        self.nextButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.name_firm.setText(QCoreApplication.translate("Dialog", u"Poleta", None))
        self.title_3.setText(QCoreApplication.translate("Dialog", u"Customer / \u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.title_5.setText(QCoreApplication.translate("Dialog", u"Flight / \u0420\u0435\u0439\u0441", None))
        self.title_7.setText(QCoreApplication.translate("Dialog", u"Date / \u0414\u0430\u0442\u0430", None))
        self.title_8.setText(QCoreApplication.translate("Dialog", u"Time / \u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043b\u0435\u0442\u0430", None))
        self.number.setText(QCoreApplication.translate("Dialog", u"Number", None))
        self.date1.setText(QCoreApplication.translate("Dialog", u"Number\n"
"MOTNH", None))
        self.time1.setText(QCoreApplication.translate("Dialog", u"00:00", None))
        self.title_15.setText(QCoreApplication.translate("Dialog", u"Departure / \u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.title_17.setText(QCoreApplication.translate("Dialog", u"Arrival / \u041f\u0440\u0438\u0431\u044b\u0442\u0438\u0435", None))
        self.title_18.setText(QCoreApplication.translate("Dialog", u"Gate / \u0412\u044b\u0445\u043e\u0434", None))
        self.title_19.setText(QCoreApplication.translate("Dialog", u"Gate closed / \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u0434\u043e", None))
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
        self.title_20.setText(QCoreApplication.translate("Dialog", u"Pnr / \u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.code_pnr.setText(QCoreApplication.translate("Dialog", u"MPHIFX", None))
        self.title_21.setText(QCoreApplication.translate("Dialog", u"Seq / \u041d\u043e\u043c\u0435\u0440", None))
        self.title_25.setText(QCoreApplication.translate("Dialog", u"28", None))
        self.title_27.setText(QCoreApplication.translate("Dialog", u"Seat / \u041c\u0435\u0441\u0442\u043e", None))
        self.seat.setText(QCoreApplication.translate("Dialog", u"20F", None))
        self.title_28.setText(QCoreApplication.translate("Dialog", u"\u043f\u0435\u0440\u0435\u0441\u0430\u0434\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430", None))
        self.image2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Customer / \u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Date / \u0414\u0430\u0442\u0430", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Flight / \u0420\u0435\u0439\u0441", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"Time", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"City2", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Dialog", u"Time", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Dialog", u"Pnr", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Dialog", u"Seat", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("Dialog", u"City1", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Customer/\u041a\u043b\u0438\u0435\u043d\u0442  ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"  Date /\u0414\u0430\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Flight/\u0420\u0435\u0439\u0441", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u" Time /\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043b\u0435\u0442\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Departure/\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Arrival/\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Gate closed/\u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u0434\u043e ", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Pnr/\u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.nextButton_5.setText(QCoreApplication.translate("Dialog", u"EXIT", None))
        self.nextButton_4.setText(QCoreApplication.translate("Dialog", u"SAVE", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Seat/\u041c\u0435\u0441\u0442\u043e", None))
    # retranslateUi

