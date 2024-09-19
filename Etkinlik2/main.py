import sys
from PyQt5.QtWidgets import QApplication
from hesap_makinesi import HmArayuz

uygulama = QApplication(sys.argv)

hesap_makinesi = HmArayuz()

sys.exit(uygulama.exec_())
