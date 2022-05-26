# Form implementation generated from reading ui file '.\loading.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogLoading(object):
    def setupUi(self, DialogLoading):
        DialogLoading.setObjectName("DialogLoading")
        DialogLoading.resize(500, 125)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLoading.sizePolicy().hasHeightForWidth())
        DialogLoading.setSizePolicy(sizePolicy)
        DialogLoading.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogLoading)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLoadingWelcome = QtWidgets.QLabel(DialogLoading)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.labelLoadingWelcome.setFont(font)
        self.labelLoadingWelcome.setObjectName("labelLoadingWelcome")
        self.horizontalLayout.addWidget(self.labelLoadingWelcome, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(DialogLoading)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLoadingMessage = QtWidgets.QLabel(DialogLoading)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        self.labelLoadingMessage.setFont(font)
        self.labelLoadingMessage.setObjectName("labelLoadingMessage")
        self.horizontalLayout_2.addWidget(self.labelLoadingMessage, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogLoading)
        QtCore.QMetaObject.connectSlotsByName(DialogLoading)

    def retranslateUi(self, DialogLoading):
        _translate = QtCore.QCoreApplication.translate
        DialogLoading.setWindowTitle(_translate("DialogLoading", "Dialog"))
        self.labelLoadingWelcome.setText(_translate("DialogLoading", "Recipie is loading, thanks for your patience..."))
        self.labelLoadingMessage.setText(_translate("DialogLoading", "Beggining to Load"))
