# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(721, 590)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(499, 300))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.actionOpen_log_folder = QAction(MainWindow)
        self.actionOpen_log_folder.setObjectName(u"actionOpen_log_folder")
        self.action_test = QAction(MainWindow)
        self.action_test.setObjectName(u"action_test")
        self.action_util = QAction(MainWindow)
        self.action_util.setObjectName(u"action_util")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_2 = QTabWidget(self.widget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.toolId = QLineEdit(self.groupBox)
        self.toolId.setObjectName(u"toolId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.toolId)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.procCd = QLineEdit(self.groupBox)
        self.procCd.setObjectName(u"procCd")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.procCd)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.carTyCombo = QComboBox(self.groupBox)
        self.carTyCombo.setObjectName(u"carTyCombo")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.carTyCombo)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.jobId = QLineEdit(self.groupBox)
        self.jobId.setObjectName(u"jobId")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.jobId)

        self.keeperToolId = QLineEdit(self.groupBox)
        self.keeperToolId.setObjectName(u"keeperToolId")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.keeperToolId)

        self.keeperJobId = QLineEdit(self.groupBox)
        self.keeperJobId.setObjectName(u"keeperJobId")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.keeperJobId)

        self.useYnCombo = QComboBox(self.groupBox)
        self.useYnCombo.setObjectName(u"useYnCombo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.useYnCombo)

        self.jobGrp1 = QLineEdit(self.groupBox)
        self.jobGrp1.setObjectName(u"jobGrp1")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.jobGrp1)

        self.jobGrp2 = QLineEdit(self.groupBox)
        self.jobGrp2.setObjectName(u"jobGrp2")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.jobGrp2)

        self.jobGrp3 = QLineEdit(self.groupBox)
        self.jobGrp3.setObjectName(u"jobGrp3")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.jobGrp3)

        self.jobGrp4 = QLineEdit(self.groupBox)
        self.jobGrp4.setObjectName(u"jobGrp4")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.jobGrp4)

        self.jobGrp5 = QLineEdit(self.groupBox)
        self.jobGrp5.setObjectName(u"jobGrp5")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.jobGrp5)

        self.jobGrp6 = QLineEdit(self.groupBox)
        self.jobGrp6.setObjectName(u"jobGrp6")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.jobGrp6)

        self.bt_create = QPushButton(self.groupBox)
        self.bt_create.setObjectName(u"bt_create")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.SpanningRole, self.bt_create)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.output = QTextEdit(self.tab)
        self.output.setObjectName(u"output")

        self.verticalLayout.addWidget(self.output)

        self.bt_clear = QPushButton(self.tab)
        self.bt_clear.setObjectName(u"bt_clear")

        self.verticalLayout.addWidget(self.bt_clear)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 721, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Socket settings", None))
        self.actionOpen_log_folder.setText(QCoreApplication.translate("MainWindow", u"Open log folder", None))
        self.action_test.setText(QCoreApplication.translate("MainWindow", u"Socket Test", None))
        self.action_util.setText(QCoreApplication.translate("MainWindow", u"Utility", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"INPUT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uad6c\uc544\uc774\ub514", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc815", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ucc28\uc885", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc7a1\uc544\uc774\ub514", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\ud37c\uc7a1 \uc544\uc774\ub514", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc5ec\ubd80", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\ud37c \ud234 \uc544\uc774\ub514", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\uc7a1 \uadf8\ub8f9 COLNO/VAL", None))
        self.jobGrp1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3/A,4/B,4/ \ub4f1\ub4f1 \uc27c\ud45c \uad6c\ubd84", None))
        self.bt_create.setText(QCoreApplication.translate("MainWindow", u"INSERT \uc0dd\uc131", None))
        self.bt_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc7a1\uc138\ud305", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\uc778\ub3c4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

