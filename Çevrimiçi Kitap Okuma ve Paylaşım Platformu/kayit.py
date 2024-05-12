from PyQt5.QtWidgets import QWidget, QMessageBox
from kayit_ui import Ui_Form
from onlinekitap import Kullanici

class KayitSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfa = Ui_Form()
        self.anasayfa.setupUi(self)

        self.anasayfa.kayitButon.clicked.connect(self.kayitol)

    def kayitol(self):
        kullaniciadi = self.anasayfa.kullaniciLine.text()
        sifre = self.anasayfa.sifreLine.text()
        telefon = self.anasayfa.telefonLine.text()
        soyad = self.anasayfa.soyadLine.text()
        ad = self.anasayfa.adLine.text()

        Kullanici.kayitol(kullaniciadi, sifre, ad, soyad, telefon)

        msg = QMessageBox()
        msg.setText("Kayıt işlemi tamamlandı")
        msg.setWindowTitle("Kayıt")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        msg.exec_()

        #yanit = QMessageBox.information(self, "Kayıt", "Kayıt işlemi tamamlandı.", QMessageBox.Ok).setStyleSheet("QLabel{ color: white}")

        self.close()