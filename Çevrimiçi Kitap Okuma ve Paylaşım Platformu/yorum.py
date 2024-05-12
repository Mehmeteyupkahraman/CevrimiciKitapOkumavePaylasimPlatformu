from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from yorum_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from onlinekitap import Kitap, Kullanici

class YorumYapSayfa(QWidget):
    def __init__(self, uye) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.uye = uye
        self.form.yorumYapButon.clicked.connect(self.yorumyap)

    def goster(self, kitap):
        self.kitap = kitap
        self.tablo_guncelle()
        self.show()

        #tablo.resizeColumnsToContents()

    def yorumyap(self):
        yorum = self.form.yorumText.toPlainText()

        yanit = QMessageBox.warning(self, "Yorum Yap", "Yorum yapma işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return

        self.kitap.yorum_yap(self.uye, yorum)
        QMessageBox.information(self, "Yorum Yap", "Yorum yapma işlemi tamamlandı.", QMessageBox.Ok)
        self.tablo_guncelle()


    def tablo_guncelle(self):
        tablo = self.form.tablo
        tablo.setRowCount(0)
        Veritabani.query('SELECT kullaniciid, yorum FROM yorumlar WHERE kitapid = ?', (self.kitap.id,))
        yorumlarsql = Veritabani.fetchall()

        if yorumlarsql is None:
            return
        
        tablo.setRowCount(len(yorumlarsql))
        satir = 0
        tablo.setColumnWidth(0, 120)
        tablo.setColumnWidth(1, 300)

        for kullaniciid, yorum in yorumlarsql:
            Veritabani.query("SELECT * FROM kullanicilar WHERE id = ?", (kullaniciid,))
            kullanicisql = Veritabani.fetchone()
            kullanici = Kullanici(*kullanicisql)

            kullanicicell = QTableWidgetItem(f"{kullanici.ad} {kullanici.soyad}")
            yorumcell = QTableWidgetItem(yorum)

            #Hepsinin yazısını ortala
            kullanicicell.setTextAlignment(QtCore.Qt.AlignCenter)
            yorumcell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, kullanicicell)
            tablo.setItem(satir, 1, yorumcell)
            satir+=1