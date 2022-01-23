import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(300,300)
janela.setWindowTitle("Primeira")
janela.show()

app.exec()
