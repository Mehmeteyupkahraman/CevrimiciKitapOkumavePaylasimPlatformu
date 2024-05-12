from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from onlinekitap import *
from PyQt5 import QtGui
from veritabani import Veritabani
from kitaplistem import KitapListemSayfa
from yorum import YorumYapSayfa
from kitapoku import KitapOkuSayfa
from icerik import IcerikSayfa
from kitapekle import KitapEkleSayfa

class AnaSayfa(QMainWindow):
    def __init__(self, uye) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.uye = uye

        self.anasayfa.sonrakiButon.clicked.connect(self.sonrakikitap)
        self.anasayfa.oncekiButon.clicked.connect(self.oncekikitap)
        self.kitap_liste_guncelle()
        self.kitapguncelle()

        kitaplistem = KitapListemSayfa(uye)
        self.anasayfa.kitapListeMenu.triggered.connect(lambda: kitaplistem.goster())
        self.anasayfa.listeEkleButon.clicked.connect(self.listeeklebuton)

        yorumyapmasayfasi = YorumYapSayfa(uye)
        self.anasayfa.yorumButon.clicked.connect(lambda: yorumyapmasayfasi.goster(self.kitaplar[self.index]))
        self.kitapokusayfa = KitapOkuSayfa()
        self.anasayfa.okuButon.clicked.connect(self.oku)

        iceriksayfa = IcerikSayfa()
        self.anasayfa.kitapIcerik.triggered.connect(lambda: iceriksayfa.goster())

        kitapeklesayfa = KitapEkleSayfa()
        self.anasayfa.kitapEkleActio.triggered.connect(lambda: kitapeklesayfa.show())
        kitapeklesayfa.ekle_sinyal.connect(self.kitap_liste_guncelle)

    def sonrakikitap(self):
        self.index += 1
        if len(self.kitaplar) == self.index:
            self.index = 0
        self.kitapguncelle()

    def oncekikitap(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.kitaplar)-1
        self.kitapguncelle()

    def kitapguncelle(self):
        kitap = self.kitaplar[self.index]
        self.anasayfa.foto.setPixmap(QtGui.QPixmap("Fotograflar/" + kitap.fotograf))
        
        self.anasayfa.aciklamaLabel.setText(kitap.aciklama)
        self.anasayfa.kitaplabel.setText(kitap.ad)
        self.anasayfa.yazarlabel.setText(kitap.yazar)
        self.anasayfa.yayinEviLabel.setText("Yayın Evi: " + kitap.yayinevi)

        Veritabani.query("SELECT * FROM kitaplistem WHERE kullaniciid = ? and kitapid = ?", (self.uye.id, kitap.id))
        listedurum = Veritabani.fetchone()

        if listedurum is None:
            self.anasayfa.listeEkleButon.setText("Listeme Ekle")
        else:
            self.anasayfa.listeEkleButon.setText("Listemden Çıkart")


    def kitap_liste_guncelle(self):
        Veritabani.query('SELECT * FROM kitaplar')
        sql = Veritabani.fetchall()
        kitaplar = []
        for kayit in sql:
            kitaplar.append(Kitap(*kayit))
        self.kitaplar = kitaplar


    def listeeklebuton(self):
        kitap = self.kitaplar[self.index]
        yanit = QMessageBox.warning(self, "Liste", "İşlemi onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        butonyazi = self.anasayfa.listeEkleButon.text()

        if butonyazi == "Listeme Ekle":
            self.uye.kitap_ekle(kitap)
            self.anasayfa.listeEkleButon.setText("Listemden Çıkart")
        else:
            self.uye.kitap_sil(kitap)
            self.anasayfa.listeEkleButon.setText("Listeme Ekle")


        QMessageBox.information(self, "Liste", "İşlem tamamlandı.", QMessageBox.Ok)

    def oku(self):
        kitap = self.kitaplar[self.index]

        Veritabani.query('SELECT * FROM kitapicerik where kitapid=?',(kitap.id,))
        icerik = Veritabani.fetchone()
        if icerik is None:
            QMessageBox.warning(self, "Kitap", "Bu kitabın içeriği yok.", QMessageBox.Ok)
        else:
            self.kitapokusayfa.goster(kitap)
