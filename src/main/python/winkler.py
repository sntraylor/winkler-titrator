# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\main\python\winkler.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1419, 991)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_upper = QtWidgets.QHBoxLayout()
        self.horizontalLayout_upper.setObjectName("horizontalLayout_upper")
        self.widget_MPL = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget_MPL.sizePolicy().hasHeightForWidth())
        self.widget_MPL.setSizePolicy(sizePolicy)
        self.widget_MPL.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_MPL.setBaseSize(QtCore.QSize(4, 0))
        self.widget_MPL.setObjectName("widget_MPL")
        self.layoutWidget = QtWidgets.QWidget(self.widget_MPL)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 698, 661))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lcdNumber_dispensed = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_dispensed.sizePolicy().hasHeightForWidth())
        self.lcdNumber_dispensed.setSizePolicy(sizePolicy)
        self.lcdNumber_dispensed.setMinimumSize(QtCore.QSize(160, 80))
        self.lcdNumber_dispensed.setBaseSize(QtCore.QSize(160, 100))
        self.lcdNumber_dispensed.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(0, 255, 0);")
        self.lcdNumber_dispensed.setDigitCount(6)
        self.lcdNumber_dispensed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_dispensed.setProperty("value", 0.0)
        self.lcdNumber_dispensed.setObjectName("lcdNumber_dispensed")
        self.verticalLayout_2.addWidget(self.lcdNumber_dispensed, 0, QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lcdNumber_endpoint = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_endpoint.sizePolicy().hasHeightForWidth())
        self.lcdNumber_endpoint.setSizePolicy(sizePolicy)
        self.lcdNumber_endpoint.setMinimumSize(QtCore.QSize(160, 80))
        self.lcdNumber_endpoint.setStyleSheet("color:rgb(0, 255, 0);\n"
"background-color: rgb(40, 40, 40);\n"
"border-color: rgb(0, 116, 0);")
        self.lcdNumber_endpoint.setSmallDecimalPoint(False)
        self.lcdNumber_endpoint.setDigitCount(6)
        self.lcdNumber_endpoint.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_endpoint.setProperty("value", 0.0)
        self.lcdNumber_endpoint.setProperty("intValue", 0)
        self.lcdNumber_endpoint.setObjectName("lcdNumber_endpoint")
        self.verticalLayout_2.addWidget(self.lcdNumber_endpoint, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_upper.addWidget(self.widget_MPL)
        self.verticalLayout.addLayout(self.horizontalLayout_upper)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setMinimumSize(QtCore.QSize(0, 261))
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setUsesScrollButtons(True)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setObjectName("tabs")
        self.tab_Settings = QtWidgets.QWidget()
        self.tab_Settings.setObjectName("tab_Settings")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_Settings)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.tab_Settings)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.pushButton_reload = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_reload.setFont(font)
        self.pushButton_reload.setObjectName("pushButton_reload")
        self.verticalLayout_4.addWidget(self.pushButton_reload)
        self.label_5 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.comboBox_meter = QtWidgets.QComboBox(self.horizontalGroupBox_2)
        self.comboBox_meter.setCurrentText("")
        self.comboBox_meter.setFrame(False)
        self.comboBox_meter.setObjectName("comboBox_meter")
        self.verticalLayout_4.addWidget(self.comboBox_meter)
        self.label_6 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.comboBox_pump = QtWidgets.QComboBox(self.horizontalGroupBox_2)
        self.comboBox_pump.setObjectName("comboBox_pump")
        self.verticalLayout_4.addWidget(self.comboBox_pump)
        self.label_7 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.comboBox_standard = QtWidgets.QComboBox(self.horizontalGroupBox_2)
        self.comboBox_standard.setObjectName("comboBox_standard")
        self.verticalLayout_4.addWidget(self.comboBox_standard)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_connect = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.pushButton_connect.setMinimumSize(QtCore.QSize(160, 100))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.verticalLayout_5.addWidget(self.pushButton_connect, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.frame = QtWidgets.QFrame(self.horizontalGroupBox_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_flask = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.pushButton_flask.setMinimumSize(QtCore.QSize(160, 100))
        self.pushButton_flask.setBaseSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_flask.setFont(font)
        self.pushButton_flask.setObjectName("pushButton_flask")
        self.horizontalLayout_2.addWidget(self.pushButton_flask, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.horizontalGroupBox_2)
        self.tabs.addTab(self.tab_Settings, "")
        self.tab_Sample = QtWidgets.QWidget()
        self.tab_Sample.setObjectName("tab_Sample")
        self.horizontalLayout_lower = QtWidgets.QHBoxLayout(self.tab_Sample)
        self.horizontalLayout_lower.setObjectName("horizontalLayout_lower")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.pushButton_1uL = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_1uL.setObjectName("pushButton_1uL")
        self.verticalLayout_6.addWidget(self.pushButton_1uL)
        self.pushButton_10uL = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_10uL.setObjectName("pushButton_10uL")
        self.verticalLayout_6.addWidget(self.pushButton_10uL)
        self.pushButton_100uL = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_100uL.setObjectName("pushButton_100uL")
        self.verticalLayout_6.addWidget(self.pushButton_100uL)
        self.pushButton_1000uL = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_1000uL.setObjectName("pushButton_1000uL")
        self.verticalLayout_6.addWidget(self.pushButton_1000uL)
        self.pushButton_5000uL = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_5000uL.setObjectName("pushButton_5000uL")
        self.verticalLayout_6.addWidget(self.pushButton_5000uL)
        self.horizontalLayout_lower.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_lower.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(10, 10))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.spinBox_guess = QtWidgets.QSpinBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_guess.setFont(font)
        self.spinBox_guess.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_guess.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_guess.setMaximum(2000)
        self.spinBox_guess.setSingleStep(100)
        self.spinBox_guess.setProperty("value", 500)
        self.spinBox_guess.setObjectName("spinBox_guess")
        self.verticalLayout_7.addWidget(self.spinBox_guess)
        self.checkBox_zoom = QtWidgets.QCheckBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_zoom.setFont(font)
        self.checkBox_zoom.setObjectName("checkBox_zoom")
        self.verticalLayout_7.addWidget(self.checkBox_zoom)
        self.checkBox_rapid = QtWidgets.QCheckBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_rapid.setFont(font)
        self.checkBox_rapid.setChecked(True)
        self.checkBox_rapid.setObjectName("checkBox_rapid")
        self.verticalLayout_7.addWidget(self.checkBox_rapid)
        self.checkBox_gran = QtWidgets.QCheckBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_gran.setFont(font)
        self.checkBox_gran.setObjectName("checkBox_gran")
        self.verticalLayout_7.addWidget(self.checkBox_gran)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.lineEdit_id = QtWidgets.QLineEdit(self.tab_Sample)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_8.addWidget(self.lineEdit_id)
        self.label_13 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.doubleSpinBox_thio_t = QtWidgets.QDoubleSpinBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_thio_t.setFont(font)
        self.doubleSpinBox_thio_t.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_thio_t.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_thio_t.setProperty("value", 21.0)
        self.doubleSpinBox_thio_t.setObjectName("doubleSpinBox_thio_t")
        self.verticalLayout_8.addWidget(self.doubleSpinBox_thio_t)
        self.label_14 = QtWidgets.QLabel(self.tab_Sample)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.doubleSpinBox_kio3_temp = QtWidgets.QDoubleSpinBox(self.tab_Sample)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_kio3_temp.setFont(font)
        self.doubleSpinBox_kio3_temp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_kio3_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_kio3_temp.setProperty("value", 21.0)
        self.doubleSpinBox_kio3_temp.setObjectName("doubleSpinBox_kio3_temp")
        self.verticalLayout_8.addWidget(self.doubleSpinBox_kio3_temp)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.comboBox_flasks = QtWidgets.QComboBox(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_flasks.sizePolicy().hasHeightForWidth())
        self.comboBox_flasks.setSizePolicy(sizePolicy)
        self.comboBox_flasks.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBox_flasks.setBaseSize(QtCore.QSize(2, 0))
        self.comboBox_flasks.setObjectName("comboBox_flasks")
        self.verticalLayout_10.addWidget(self.comboBox_flasks)
        self.label_8 = QtWidgets.QLabel(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(-2)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.pushButton_sample_type = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_sample_type.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_sample_type.setStyleSheet("")
        self.pushButton_sample_type.setCheckable(True)
        self.pushButton_sample_type.setChecked(True)
        self.pushButton_sample_type.setAutoExclusive(True)
        self.pushButton_sample_type.setObjectName("pushButton_sample_type")
        self.verticalLayout_10.addWidget(self.pushButton_sample_type)
        self.pushButton_standard_type = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_standard_type.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_standard_type.setStyleSheet("")
        self.pushButton_standard_type.setCheckable(True)
        self.pushButton_standard_type.setAutoExclusive(True)
        self.pushButton_standard_type.setObjectName("pushButton_standard_type")
        self.verticalLayout_10.addWidget(self.pushButton_standard_type)
        self.pushButton_sea_water_blank_type = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_sea_water_blank_type.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_sea_water_blank_type.setToolTip("")
        self.pushButton_sea_water_blank_type.setStyleSheet("")
        self.pushButton_sea_water_blank_type.setCheckable(True)
        self.pushButton_sea_water_blank_type.setAutoExclusive(True)
        self.pushButton_sea_water_blank_type.setObjectName("pushButton_sea_water_blank_type")
        self.verticalLayout_10.addWidget(self.pushButton_sea_water_blank_type)
        self.pushButton_di_water_blank_type = QtWidgets.QPushButton(self.tab_Sample)
        self.pushButton_di_water_blank_type.setToolTip("")
        self.pushButton_di_water_blank_type.setCheckable(True)
        self.pushButton_di_water_blank_type.setAutoExclusive(True)
        self.pushButton_di_water_blank_type.setObjectName("pushButton_di_water_blank_type")
        self.verticalLayout_10.addWidget(self.pushButton_di_water_blank_type)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_titrate = QtWidgets.QPushButton(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_titrate.sizePolicy().hasHeightForWidth())
        self.pushButton_titrate.setSizePolicy(sizePolicy)
        self.pushButton_titrate.setMinimumSize(QtCore.QSize(160, 50))
        self.pushButton_titrate.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_titrate.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_titrate.setFont(font)
        self.pushButton_titrate.setStyleSheet("background-color: rgb(18, 173, 28);")
        self.pushButton_titrate.setFlat(False)
        self.pushButton_titrate.setObjectName("pushButton_titrate")
        self.horizontalLayout_5.addWidget(self.pushButton_titrate)
        self.pushButton_stop_titration = QtWidgets.QPushButton(self.tab_Sample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop_titration.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_titration.setSizePolicy(sizePolicy)
        self.pushButton_stop_titration.setMinimumSize(QtCore.QSize(160, 50))
        self.pushButton_stop_titration.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_titration.setFont(font)
        self.pushButton_stop_titration.setAutoFillBackground(False)
        self.pushButton_stop_titration.setStyleSheet("background-color: rgb(255, 43, 39);")
        self.pushButton_stop_titration.setObjectName("pushButton_stop_titration")
        self.horizontalLayout_5.addWidget(self.pushButton_stop_titration)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_lower.addLayout(self.verticalLayout_3)
        self.tabs.addTab(self.tab_Sample, "")
        self.tab_PumpControl = QtWidgets.QWidget()
        self.tab_PumpControl.setObjectName("tab_PumpControl")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_PumpControl)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, -20, 1332, 243))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_loadStandard = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_loadStandard.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_loadStandard.setFont(font)
        self.pushButton_loadStandard.setObjectName("pushButton_loadStandard")
        self.horizontalLayout_3.addWidget(self.pushButton_loadStandard)
        self.spinBox_standard = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_standard.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_standard.setFont(font)
        self.spinBox_standard.setFrame(True)
        self.spinBox_standard.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_standard.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox_standard.setMaximum(10000)
        self.spinBox_standard.setSingleStep(1000)
        self.spinBox_standard.setProperty("value", 10000)
        self.spinBox_standard.setObjectName("spinBox_standard")
        self.horizontalLayout_3.addWidget(self.spinBox_standard)
        self.pushButton_dispenseStandard = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_dispenseStandard.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dispenseStandard.setFont(font)
        self.pushButton_dispenseStandard.setObjectName("pushButton_dispenseStandard")
        self.horizontalLayout_3.addWidget(self.pushButton_dispenseStandard)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_fillStandard = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_fillStandard.setFont(font)
        self.pushButton_fillStandard.setObjectName("pushButton_fillStandard")
        self.verticalLayout_9.addWidget(self.pushButton_fillStandard)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.pushButton_emptyStandard = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_emptyStandard.setFont(font)
        self.pushButton_emptyStandard.setObjectName("pushButton_emptyStandard")
        self.verticalLayout_9.addWidget(self.pushButton_emptyStandard)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_loadThios = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_loadThios.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_loadThios.setFont(font)
        self.pushButton_loadThios.setObjectName("pushButton_loadThios")
        self.horizontalLayout_3.addWidget(self.pushButton_loadThios)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.label_10)
        self.spinBox_thios = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_thios.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_thios.setFont(font)
        self.spinBox_thios.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_thios.setMaximum(1000)
        self.spinBox_thios.setSingleStep(100)
        self.spinBox_thios.setProperty("value", 1000)
        self.spinBox_thios.setObjectName("spinBox_thios")
        self.verticalLayout_12.addWidget(self.spinBox_thios)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.pushButton_dispenseThios = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_dispenseThios.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dispenseThios.setFont(font)
        self.pushButton_dispenseThios.setObjectName("pushButton_dispenseThios")
        self.horizontalLayout_3.addWidget(self.pushButton_dispenseThios)
        self.tabs.addTab(self.tab_PumpControl, "")
        self.verticalLayout.addWidget(self.tabs)
        self.verticalLayout.setStretch(0, 3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1419, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoad = QtWidgets.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        self.comboBox_meter.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Winkler Titrator"))
        self.label.setText(_translate("MainWindow", "Volume Dispensed"))
        self.label_2.setText(_translate("MainWindow", "Estimated Endpoint"))
        self.label_12.setText(_translate("MainWindow", "COM Port Selection"))
        self.pushButton_reload.setText(_translate("MainWindow", "Reload Ports"))
        self.label_5.setText(_translate("MainWindow", "Select COM port for meter"))
        self.label_6.setText(_translate("MainWindow", "Select COM port for titrator pump"))
        self.label_7.setText(_translate("MainWindow", "Select COM port for standard pump"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_flask.setText(_translate("MainWindow", "Load Flask Calibration"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_Settings), _translate("MainWindow", "Settings"))
        self.label_11.setText(_translate("MainWindow", "Manual Titration"))
        self.pushButton_1uL.setText(_translate("MainWindow", "+ 1 uL"))
        self.pushButton_10uL.setText(_translate("MainWindow", "+ 10 uL"))
        self.pushButton_100uL.setText(_translate("MainWindow", "+ 100 uL"))
        self.pushButton_1000uL.setText(_translate("MainWindow", "+ 1000 uL"))
        self.pushButton_5000uL.setText(_translate("MainWindow", "+ 5000 uL"))
        self.label_4.setText(_translate("MainWindow", "Initial Guess (uL)"))
        self.checkBox_zoom.setText(_translate("MainWindow", "Zoom View"))
        self.checkBox_rapid.setText(_translate("MainWindow", "Rapid Mode"))
        self.checkBox_gran.setText(_translate("MainWindow", "Gran View"))
        self.label_15.setText(_translate("MainWindow", "ID"))
        self.label_13.setText(_translate("MainWindow", "Thiosulfate\n"
"Temperature (degC)"))
        self.label_14.setText(_translate("MainWindow", "KIO3\n"
"Temperature (degC)"))
        self.label_3.setText(_translate("MainWindow", "Select Flask"))
        self.label_8.setText(_translate("MainWindow", "Select Sample Type"))
        self.pushButton_sample_type.setText(_translate("MainWindow", "Sample"))
        self.pushButton_standard_type.setText(_translate("MainWindow", "Standard"))
        self.pushButton_sea_water_blank_type.setText(_translate("MainWindow", "Sea Water Blank"))
        self.pushButton_di_water_blank_type.setText(_translate("MainWindow", "DI Water Blank"))
        self.pushButton_titrate.setText(_translate("MainWindow", "Run\n"
"Titration"))
        self.pushButton_stop_titration.setToolTip(_translate("MainWindow", "Stop Titration and save results"))
        self.pushButton_stop_titration.setText(_translate("MainWindow", "STOP\n"
"Titration"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_Sample), _translate("MainWindow", "Titrate"))
        self.pushButton_loadStandard.setText(_translate("MainWindow", "Load\n"
"Standard"))
        self.pushButton_dispenseStandard.setText(_translate("MainWindow", "Dispense\n"
"Standard"))
        self.pushButton_fillStandard.setText(_translate("MainWindow", "Fill"))
        self.label_9.setText(_translate("MainWindow", "KIO3 Standard (uL)"))
        self.pushButton_emptyStandard.setText(_translate("MainWindow", "Empty"))
        self.pushButton_loadThios.setText(_translate("MainWindow", "Load\n"
"Thiosulfate"))
        self.label_10.setText(_translate("MainWindow", "Thiosulfate (uL)"))
        self.pushButton_dispenseThios.setText(_translate("MainWindow", "Dispense\n"
"Thiosulfate"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_PumpControl), _translate("MainWindow", "Pump Controls"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
