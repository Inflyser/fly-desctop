# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're-rev-tarif.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
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
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.frame)
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
"border: none;")
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(False)

        self.verticalLayout.addWidget(self.title)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u" \n"
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
"\n"
"")

        self.verticalLayout.addWidget(self.comboBox)

        self.info = QLabel(self.frame)
        self.info.setObjectName(u"info")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.info)

        self.nextButton = QPushButton(self.frame)
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
        self.title.setText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u0430\u043d\u043e\u0432\u044b\u0439 \u0442\u0430\u0440\u0438\u0444", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u042d\u043a\u043e\u043d\u043e\u043c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0444\u043e\u0440\u0442", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u0411\u0438\u0437\u043d\u0435\u0441", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u043a\u043b\u0430\u0441\u0441", None))

        self.info.setText(QCoreApplication.translate("Dialog", u"\n"
"\n"
"\u0412\u044b\u0431\u0438\u0440\u0430\u0439\u0442\u0435 \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \n"
"\u0441 \u0432\u0430\u0448\u0438\u043c\u0438 \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u043c\u0438.", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u" \u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

