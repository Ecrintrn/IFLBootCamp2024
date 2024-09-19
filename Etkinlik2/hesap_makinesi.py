from PyQt5 import QtWidgets
from hm_arayuzu import Ui_MainWindow

class HmArayuz(QtWidgets.QMainWindow, Ui_MainWindow):
    ilk_sayi = None
    ikinci_sayi = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pb_1.clicked.connect(self.frakam_basma)
        self.pb_2.clicked.connect(self.frakam_basma)
        self.pb_3.clicked.connect(self.frakam_basma)
        self.pb_4.clicked.connect(self.frakam_basma)
        self.pb_5.clicked.connect(self.frakam_basma)
        self.pb_6.clicked.connect(self.frakam_basma)
        self.pb_7.clicked.connect(self.frakam_basma)
        self.pb_8.clicked.connect(self.frakam_basma)
        self.pb_9.clicked.connect(self.frakam_basma)
        self.pb_0.clicked.connect(self.frakam_basma)

        self.pb_nokta.clicked.connect(self.fondalik)

        self.pb_isaret.clicked.connect(self.fisaret_yuzde)
        self.pb_yuzde.clicked.connect(self.fisaret_yuzde)

        self.pb_topla.clicked.connect(self.faritmetik)
        self.pb_cikar.clicked.connect(self.faritmetik)
        self.pb_carp.clicked.connect(self.faritmetik)
        self.pb_bol.clicked.connect(self.faritmetik)

        self.pb_topla.setCheckable(True)
        self.pb_cikar.setCheckable(True)
        self.pb_carp.setCheckable(True)
        self.pb_bol.setCheckable(True)

        self.pb_esit.clicked.connect(self.fsonuc)
        self.pb_esit.setCheckable(True)

        self.pb_C.clicked.connect(self.ftemizle)

    def frakam_basma(self):
        buton = self.sender()

        if ((self.ikinci_sayi) and (self.pb_esit.isChecked())):
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikinci_sayi = True
            self.pb_esit.setChecked(False)
        elif (self.pb_topla.isChecked() or self.pb_cikar.isChecked() or self.pb_carp.isChecked() or self.pb_bol.isChecked()) and (not self.ikinci_sayi):
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikinci_sayi = True
        else:
            if (('.' in self.label.text()) and self.buton.text() == "0"):
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))
            else:
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))


    def fondalik(self):
        self.label.setText(self.label.text()+'.')

    def fisaret_yuzde(self):
        buton = self.sender()

        deger = float(self.label.text())

        if buton.text() =="+/-":
            deger = deger *-1
        else:
            deger = deger*0.01

        self.label.setText(format(deger,'.15g'))

    def faritmetik(self):
        buton = self.sender()
        self.ilk_sayi = float(self.label.text())
        buton.setChecked(True)

    def fsonuc(self):
        ikinci_deger = float(self.label.text())

        if self.pb_topla.isChecked():
            yeniDeger = self.ilk_sayi + ikinci_deger
            self.label.setText(format(yeniDeger, '.15g'))
            self.pb_topla.setChecked(False)

        elif self.pb_cikar.isChecked():
            yeniDeger = self.ilk_sayi - ikinci_deger
            self.label.setText(format(yeniDeger, '.15g'))
            self.pb_cikar.setChecked(False)

        elif self.pb_carp.isChecked():
            yeniDeger = self.ilk_sayi * ikinci_deger
            self.label.setText(format(yeniDeger, '.15g'))
            self.pb_carp.setChecked(False)

        elif self.pb_bol.isChecked():
            if ikinci_deger == 0.0:
                print("İkinci değer sıfır olamaz.")
            yeniDeger = self.ilk_sayi / ikinci_deger
            self.label.setText(format(yeniDeger, '.15g'))
            self.pb_bol.setChecked(False)

        self.ilk_sayi = yeniDeger
        self.pb_esit.setChecked(True)

    def ftemizle(self):
        self.ilk_sayi = 0
        self.ikinci_sayi = False
        self.label.setText('0')
        self.pb_bol.setChecked(False)
        self.pb_topla.setChecked(False)
        self.pb_cikar.setChecked(False)
        self.pb_carp.setChecked(False)
        self.pb_esit.setChecked(False)