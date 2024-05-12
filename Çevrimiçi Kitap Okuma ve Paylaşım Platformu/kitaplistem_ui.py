from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(442, 460)
        Form.setStyleSheet("background-color: lightblue;")  # Arka plan rengi lightblue olarak değiştirildi
        self.tablo = QtWidgets.QTableWidget(Form)
        self.tablo.setGeometry(QtCore.QRect(0, 0, 441, 461))
        self.tablo.setObjectName("tablo")
        self.tablo.setColumnCount(3)
        self.tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitap Listem"))
        item = self.tablo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Kitap Adı"))
        item = self.tablo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Yazarı"))
        item = self.tablo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Yayınevi"))
