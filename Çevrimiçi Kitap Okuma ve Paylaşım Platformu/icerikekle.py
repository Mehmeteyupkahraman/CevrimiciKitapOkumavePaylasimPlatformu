from PyQt5.QtWidgets import QWidget, QMessageBox
from icerikekle_ui import Ui_Form
from veritabani import Veritabani

class IcerikYukleSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.index = 0
        self.form.sonrakiButon.clicked.connect(self.sonraki)
        self.form.oncekiButon.clicked.connect(self.onceki)
        self.form.kaydetButon.clicked.connect(self.kaydet)

    def goster(self, kitap, sayfa):
        self.kitap = kitap
        self.sayfa = sayfa
        self.index = 0
        self.icerikler = []
        self.show()
        self.sayfaguncelle()

    def sonraki(self):
        self.sayfakaydet()
        self.index += 1
        if self.sayfa == self.index:
            self.index = self.sayfa-1
            return
        self.sayfaguncelle()

    def onceki(self):
        self.sayfakaydet()
        self.index -= 1
        if self.index == -1:
            self.index = 0
            return
        self.sayfaguncelle()

    def sayfaguncelle(self):
        self.form.sayfa.setText(f"Sayfa: {self.index+1}/{self.sayfa}")
        if self.index+1 == self.sayfa:
            self.form.kaydetButon.setEnabled(True)
        else:
            self.form.kaydetButon.setEnabled(False)
        for icerik in self.icerikler:
            if icerik["Sayfa"] == self.index+1:
                self.form.aciklama.setText(icerik["Açıklama"])
                return
            
        self.form.aciklama.clear()

    def sayfakaydet(self):
        aciklama = self.form.aciklama.toPlainText()
        for icerik in self.icerikler:
            if icerik["Sayfa"] == self.index+1:
                icerik["Açıklama"] = aciklama
                return
        self.icerikler.append({"Açıklama": aciklama, "Sayfa": self.index+1})

    def kaydet(self):
        yanit = QMessageBox.warning(self,"İçerik Yükle", "Kitap içeriğini eklemek istediğinize emin misiniz?",QMessageBox.Yes,QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        self.sayfakaydet()
        for icerik in self.icerikler:
            Veritabani.query("insert into kitapicerik (kitapid,sayfa,icerik) values (?,?,?)",(self.kitap.id,icerik["Sayfa"],icerik["Açıklama"]))
        yanit = QMessageBox.information(self,"İçerik Yükle", "İçerik yüklendi",QMessageBox.Ok)
        self.close()
