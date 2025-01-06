# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_new_window_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 835)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread: pad,\n"
"    x1: 1, y1: 1,\n"
"    x2: 0, y2: 0,\n"
"    stop: 0 rgba(0, 191, 255, 255), /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"    stop: 0.5 rgba(0, 0, 255, 255), /* \u0421\u0438\u043d\u0438\u0439 */\n"
"    stop: 1 rgba(0, 191, 255, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
");\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 591, 811))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.part1 = QFrame(self.layoutWidget)
        self.part1.setObjectName(u"part1")
        self.part1.setStyleSheet(u"padding: 35px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.verticalLayout = QVBoxLayout(self.part1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.booking = QLabel(self.part1)
        self.booking.setObjectName(u"booking")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.booking.setFont(font)
        self.booking.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.booking.setScaledContents(False)
        self.booking.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.booking.setWordWrap(False)

        self.verticalLayout.addWidget(self.booking)

        self.where2 = QComboBox(self.part1)
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.addItem("")
        self.where2.setObjectName(u"where2")
        self.where2.setAutoFillBackground(False)
        self.where2.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #D3D3D3; /* \u0420\u0430\u043c\u043a\u0430 \u0441 \u0446\u0432\u0435\u0442\u043e\u043c */\n"
"    border-radius: 15px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    background-color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 15px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"    font-size: 20px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0440\u0430\u043c\u043a\u0443 \u0443 \u043a\u043d\u043e\u043f\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
" \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: "
                        "#333333; /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    background-color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    background-color: #D3D3D3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"    color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"}\n"
"\n"
"")
        self.where2.setFrame(True)

        self.verticalLayout.addWidget(self.where2)

        self.image1 = QPushButton(self.part1)
        self.image1.setObjectName(u"image1")
        self.image1.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(30)
        self.image1.setFont(font1)
        self.image1.setStyleSheet(u"QPashButton {\n"
"padding: 55px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/Icon/flying.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.image1.setIcon(icon)
        self.image1.setIconSize(QSize(60, 60))
        self.image1.setCheckable(False)
        self.image1.setAutoRepeat(False)
        self.image1.setAutoDefault(False)
        self.image1.setFlat(True)

        self.verticalLayout.addWidget(self.image1)

        self.where1 = QComboBox(self.part1)
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.addItem("")
        self.where1.setObjectName(u"where1")
        self.where1.setStyleSheet(u" \n"
"\n"
"QComboBox {\n"
"    border: 2px solid #D3D3D3; /* \u0420\u0430\u043c\u043a\u0430 \u0441 \u0446\u0432\u0435\u0442\u043e\u043c */\n"
"    border-radius: 15px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    background-color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 15px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"    font-size: 20px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0440\u0430\u043c\u043a\u0443 \u0443 \u043a\u043d\u043e\u043f\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
" \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"   "
                        " border-color: #333333; /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    background-color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"}\n"
"\n"
"QComboBox:item:selected {\n"
"    background-color: #D3D3D3; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"    color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.where1)


        self.verticalLayout_2.addWidget(self.part1)

        self.part2 = QFrame(self.layoutWidget)
        self.part2.setObjectName(u"part2")
        self.part2.setStyleSheet(u"color: white;\n"
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
        self.horizontalLayout = QHBoxLayout(self.part2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.road = QLabel(self.part2)
        self.road.setObjectName(u"road")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.road.setFont(font2)
        self.road.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.road.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.road)

        self.round = QLabel(self.part2)
        self.round.setObjectName(u"round")
        self.round.setFont(font2)
        self.round.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.round.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.round)

        self.km = QLabel(self.part2)
        self.km.setObjectName(u"km")
        self.km.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.km.sizePolicy().hasHeightForWidth())
        self.km.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setKerning(True)
        self.km.setFont(font3)
        self.km.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.km.setAcceptDrops(False)
        self.km.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.km.setAutoFillBackground(False)
        self.km.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding: 50px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */")
        self.km.setFrameShape(QFrame.Shape.NoFrame)
        self.km.setFrameShadow(QFrame.Shadow.Plain)
        self.km.setLineWidth(0)
        self.km.setScaledContents(False)
        self.km.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.km.setWordWrap(False)
        self.km.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.km)


        self.verticalLayout_2.addWidget(self.part2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_5)

        self.Button_next = QPushButton(self.layoutWidget)
        self.Button_next.setObjectName(u"Button_next")
        self.Button_next.setStyleSheet(u"QPushButton {\n"
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
        self.Button_next.setAutoDefault(False)
        self.Button_next.setFlat(False)

        self.verticalLayout_2.addWidget(self.Button_next)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.image1.setDefault(False)
        self.Button_next.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aviopay", None))
        self.booking.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.where2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0434\u0430", None))
        self.where2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u043c\u0441\u0442\u0435\u0440\u0434\u0430\u043c", None))
        self.where2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0441\u0435\u043b\u043e\u043d\u0430", None))
        self.where2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u0433\u043a\u043e\u043a", None))
        self.where2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u043b\u0438\u043d", None))
        self.where2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0430\u043f\u0435\u0448\u0442", None))
        self.where2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0431\u0430\u0439", None))
        self.where2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u041a\u0435\u0439\u043f\u0442\u0430\u0443\u043d", None))
        self.where2.setItemText(8, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434", None))
        self.where2.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0441\u0430\u0431\u043e\u043d", None))
        self.where2.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043d\u0434\u043e\u043d", None))
        self.where2.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0441-\u0410\u043d\u0434\u0436\u0435\u043b\u0435\u0441", None))
        self.where2.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0434\u0440\u0438\u0434", None))
        self.where2.setItemText(13, QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043b\u0430\u043d", None))
        self.where2.setItemText(14, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.where2.setItemText(15, QCoreApplication.translate("MainWindow", u"\u041c\u044e\u043d\u0445\u0435\u043d", None))
        self.where2.setItemText(16, QCoreApplication.translate("MainWindow", u"\u041d\u044c\u044e-\u0419\u043e\u0440\u043a", None))
        self.where2.setItemText(17, QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0430\u043a\u0430", None))
        self.where2.setItemText(18, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0438\u0436", None))
        self.where2.setItemText(19, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u044c\u043c\u0430-\u0434\u0435-\u041c\u0430\u0439\u043e\u0440\u043a\u0430", None))
        self.where2.setItemText(20, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0433\u0430", None))
        self.where2.setItemText(21, QCoreApplication.translate("MainWindow", u"\u0420\u0438\u043c", None))
        self.where2.setItemText(22, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0432\u0438\u043b\u044c\u044f", None))
        self.where2.setItemText(23, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0434\u043d\u0435\u0439", None))
        self.where2.setItemText(24, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0433\u0430\u043f\u0443\u0440", None))
        self.where2.setItemText(25, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0443\u043b", None))
        self.where2.setItemText(26, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0438\u043e", None))
        self.where2.setItemText(27, QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0431\u044d\u0439", None))
        self.where2.setItemText(28, QCoreApplication.translate("MainWindow", u"\u0427\u0438\u043a\u0430\u0433\u043e", None))
        self.where2.setItemText(29, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043d\u0430", None))
        self.where2.setItemText(30, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0440\u0430\u043a\u0435\u0448", None))

        self.image1.setText("")
        self.where1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0443\u0434\u0430", None))
        self.where1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u043c\u0441\u0442\u0435\u0440\u0434\u0430\u043c", None))
        self.where1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0441\u0435\u043b\u043e\u043d\u0430", None))
        self.where1.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u0433\u043a\u043e\u043a", None))
        self.where1.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u043b\u0438\u043d", None))
        self.where1.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0430\u043f\u0435\u0448\u0442", None))
        self.where1.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0431\u0430\u0439", None))
        self.where1.setItemText(7, QCoreApplication.translate("MainWindow", u"\u041a\u0435\u0439\u043f\u0442\u0430\u0443\u043d", None))
        self.where1.setItemText(8, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434", None))
        self.where1.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0441\u0430\u0431\u043e\u043d", None))
        self.where1.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043d\u0434\u043e\u043d", None))
        self.where1.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0441-\u0410\u043d\u0434\u0436\u0435\u043b\u0435\u0441", None))
        self.where1.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0434\u0440\u0438\u0434", None))
        self.where1.setItemText(13, QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043b\u0430\u043d", None))
        self.where1.setItemText(14, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.where1.setItemText(15, QCoreApplication.translate("MainWindow", u"\u041c\u044e\u043d\u0445\u0435\u043d", None))
        self.where1.setItemText(16, QCoreApplication.translate("MainWindow", u"\u041d\u044c\u044e-\u0419\u043e\u0440\u043a", None))
        self.where1.setItemText(17, QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0430\u043a\u0430", None))
        self.where1.setItemText(18, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0438\u0436", None))
        self.where1.setItemText(19, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u044c\u043c\u0430-\u0434\u0435-\u041c\u0430\u0439\u043e\u0440\u043a\u0430", None))
        self.where1.setItemText(20, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0433\u0430", None))
        self.where1.setItemText(21, QCoreApplication.translate("MainWindow", u"\u0420\u0438\u043c", None))
        self.where1.setItemText(22, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0432\u0438\u043b\u044c\u044f", None))
        self.where1.setItemText(23, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0434\u043d\u0435\u0439", None))
        self.where1.setItemText(24, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0433\u0430\u043f\u0443\u0440", None))
        self.where1.setItemText(25, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0443\u043b", None))
        self.where1.setItemText(26, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0438\u043e", None))
        self.where1.setItemText(27, QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0431\u044d\u0439", None))
        self.where1.setItemText(28, QCoreApplication.translate("MainWindow", u"\u0427\u0438\u043a\u0430\u0433\u043e", None))
        self.where1.setItemText(29, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043d\u0430", None))
        self.where1.setItemText(30, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0440\u0430\u043a\u0435\u0448", None))

        self.road.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0430\u0448 \u043f\u0443\u0442\u044c \u0441\u043e\u0441\u0442\u0430\u0432\u0438\u0442", None))
        self.round.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.km.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043c", None))
        self.label_5.setText("")
        self.Button_next.setText(QCoreApplication.translate("MainWindow", u" \u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

