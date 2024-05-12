from PyQt5.QtWidgets import QWidget, QMessageBox
from icerik_ui import Ui_Form
from veritabani import Veritabani
from onlinekitap import Kitap
from icerikekle import IcerikYukleSayfa
from kitapekle import Kitap

class IcerikSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ekleButon.clicked.connect(self.ekle)

    def goster(self):
        Veritabani.query("SELECT kitaplar.* FROM kitaplar LEFT JOIN kitapicerik ON kitaplar.id = kitapicerik.kitapid WHERE kitapicerik.kitapid IS NULL")
        kitaplar = Veritabani.fetchall()
        self.kitaplar = []
        self.form.kitapBox.clear()
        for kitap in kitaplar:
            kitapp = Kitap(*kitap)
            self.form.kitapBox.addItem(kitapp.ad, kitapp.id)
            self.kitaplar.append(kitapp)
        self.show()

    def ekle(self):
        index = self.form.kitapBox.currentIndex()
        if index < 0:
            return
        kitap = self.kitaplar[index]
        sayfa = self.form.sayfaBox.value()
        self.icerikyuklesayfa = IcerikYukleSayfa()
        self.icerikyuklesayfa.goster(kitap,sayfa)
        self.close()