# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_h_ctrlbox = QHBoxLayout()
        self.layout_h_ctrlbox.setObjectName(u"layout_h_ctrlbox")
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy)
        self.btn_create.setMaximumSize(QSize(80, 16777215))

        self.layout_h_ctrlbox.addWidget(self.btn_create)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(80, 16777215))

        self.layout_h_ctrlbox.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_h_ctrlbox.addItem(self.horizontalSpacer)

        self.btn_recvclear = QPushButton(self.centralwidget)
        self.btn_recvclear.setObjectName(u"btn_recvclear")

        self.layout_h_ctrlbox.addWidget(self.btn_recvclear)

        self.label_s_fontsize = QLabel(self.centralwidget)
        self.label_s_fontsize.setObjectName(u"label_s_fontsize")

        self.layout_h_ctrlbox.addWidget(self.label_s_fontsize)

        self.spinbox_fontsize = QSpinBox(self.centralwidget)
        self.spinbox_fontsize.setObjectName(u"spinbox_fontsize")
        self.spinbox_fontsize.setMinimumSize(QSize(30, 0))
        self.spinbox_fontsize.setMinimum(9)
        self.spinbox_fontsize.setValue(9)

        self.layout_h_ctrlbox.addWidget(self.spinbox_fontsize)


        self.verticalLayout.addLayout(self.layout_h_ctrlbox)

        self.layout_h_mainbox = QHBoxLayout()
        self.layout_h_mainbox.setObjectName(u"layout_h_mainbox")
        self.tree_main = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.tree_main.setHeaderItem(__qtreewidgetitem)
        self.tree_main.setObjectName(u"tree_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree_main.sizePolicy().hasHeightForWidth())
        self.tree_main.setSizePolicy(sizePolicy1)
        self.tree_main.setMinimumSize(QSize(300, 0))
        self.tree_main.setMaximumSize(QSize(400, 16777215))
        self.tree_main.setColumnCount(2)
        self.tree_main.header().setDefaultSectionSize(200)

        self.layout_h_mainbox.addWidget(self.tree_main)

        self.layout_v_infobox = QVBoxLayout()
        self.layout_v_infobox.setObjectName(u"layout_v_infobox")
        self.groupbox_status = QGroupBox(self.centralwidget)
        self.groupbox_status.setObjectName(u"groupbox_status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupbox_status.sizePolicy().hasHeightForWidth())
        self.groupbox_status.setSizePolicy(sizePolicy2)
        self.groupbox_status.setMinimumSize(QSize(0, 80))

        self.layout_v_infobox.addWidget(self.groupbox_status)

        self.groupbox_datarecv = QGroupBox(self.centralwidget)
        self.groupbox_datarecv.setObjectName(u"groupbox_datarecv")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupbox_datarecv.sizePolicy().hasHeightForWidth())
        self.groupbox_datarecv.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupbox_datarecv)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_recv = QPlainTextEdit(self.groupbox_datarecv)
        self.text_recv.setObjectName(u"text_recv")

        self.gridLayout.addWidget(self.text_recv, 0, 0, 1, 1)


        self.layout_v_infobox.addWidget(self.groupbox_datarecv)

        self.groupbox_datasend = QGroupBox(self.centralwidget)
        self.groupbox_datasend.setObjectName(u"groupbox_datasend")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_datasend)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_send = QPlainTextEdit(self.groupbox_datasend)
        self.text_send.setObjectName(u"text_send")

        self.verticalLayout_2.addWidget(self.text_send)

        self.layout_h_datasendopition = QHBoxLayout()
        self.layout_h_datasendopition.setObjectName(u"layout_h_datasendopition")
        self.btn_send = QPushButton(self.groupbox_datasend)
        self.btn_send.setObjectName(u"btn_send")

        self.layout_h_datasendopition.addWidget(self.btn_send)

        self.btn_templatesave = QPushButton(self.groupbox_datasend)
        self.btn_templatesave.setObjectName(u"btn_templatesave")

        self.layout_h_datasendopition.addWidget(self.btn_templatesave)

        self.btn_templateread = QPushButton(self.groupbox_datasend)
        self.btn_templateread.setObjectName(u"btn_templateread")

        self.layout_h_datasendopition.addWidget(self.btn_templateread)

        self.btn_sendclear = QPushButton(self.groupbox_datasend)
        self.btn_sendclear.setObjectName(u"btn_sendclear")

        self.layout_h_datasendopition.addWidget(self.btn_sendclear)

        self.btn_textformat = QPushButton(self.groupbox_datasend)
        self.btn_textformat.setObjectName(u"btn_textformat")

        self.layout_h_datasendopition.addWidget(self.btn_textformat)


        self.verticalLayout_2.addLayout(self.layout_h_datasendopition)


        self.layout_v_infobox.addWidget(self.groupbox_datasend)


        self.layout_h_mainbox.addLayout(self.layout_v_infobox)


        self.verticalLayout.addLayout(self.layout_h_mainbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ServerTool Beta", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_recvclear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_s_fontsize.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.groupbox_status.setTitle(QCoreApplication.translate("MainWindow", u"Socket \u72b6\u6001", None))
        self.groupbox_datarecv.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u63a5\u6536", None))
        self.groupbox_datasend.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53d1\u9001", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.btn_templatesave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6a21\u677f", None))
        self.btn_templateread.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6a21\u677f", None))
        self.btn_sendclear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.btn_textformat.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u5316", None))
    # retranslateUi

