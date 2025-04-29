# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabExample.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_tabExample(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(767, 429)
        Form.setStyleSheet(u"QWidget\n"
"{\n"
"    background-color: rgb(211,211,211);\n"
"    color: rgb(88, 88, 90);\n"
"    selection-background-color: rgb(21, 165, 137);\n"
"    selection-color: rgb(245, 244, 244);\n"
"    \n"
"	font: 16pt\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"  background-color: rgb(211,211,211);\n"
"}\n"
"\n"
"QLabel#error_label\n"
"{\n"
"   color: rgb(220, 130, 30);\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    background-color: rgb(21, 165, 137);\n"
"    color: rgb(88, 88, 90);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.server = QLabel(Form)
        self.server.setObjectName(u"server")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.server)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.port = QLabel(Form)
        self.port.setObjectName(u"port")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.port)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.user = QLabel(Form)
        self.user.setObjectName(u"user")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.user)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.home = QLabel(Form)
        self.home.setObjectName(u"home")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.home)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"iRODS session information", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Server", None))
        self.server.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Port", None))
        self.port.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"User", None))
        self.user.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Home", None))
        self.home.setText("")
    # retranslateUi

