from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from kitaplistem_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from onlinekitap import Kitap

class KitapListemSayfa(QWidget):
    def __init__(self, uye) -> None:
        super().__init__()
        self.oduncform = Ui_Form()
        self.oduncform.setupUi(self)
        self.uye = uye

    def goster(self):
        tablo = self.oduncform.tablo
        tablo.setRowCount(0)
        Veritabani.query('SELECT kullaniciid, kitapid FROM kitaplistem WHERE kullaniciid = ?', (self.uye.id,))
        kitaplarsql = Veritabani.fetchall()

        self.show()
        if kitaplarsql is None:
            return
        
        tablo.setRowCount(len(kitaplarsql))
        satir = 0
        tablo.setColumnWidth(0, 140)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 140)

        for kullaniciid, kitapid in kitaplarsql:
            Veritabani.query("SELECT * FROM kitaplar WHERE id = ?", (kitapid,))
            kitapsql = Veritabani.fetchone()
            kitap = Kitap(*kitapsql)

            kitapcell = QTableWidgetItem(kitap.ad)
            yazarcell = QTableWidgetItem(kitap.yazar)
            yayinevicell = QTableWidgetItem(kitap.yayinevi)

            #Hepsinin yazısını ortala
            kitapcell.setTextAlignment(QtCore.Qt.AlignCenter)
            yazarcell.setTextAlignment(QtCore.Qt.AlignCenter)
            yayinevicell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, kitapcell)
            tablo.setItem(satir, 1, yazarcell)
            tablo.setItem(satir, 2, yayinevicell)
            satir+=1

        #tablo.resizeColumnsToContents()