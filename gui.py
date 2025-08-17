from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QTextEdit, QVBoxLayout, QHBoxLayout, QGroupBox, QSpinBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import pyfiglet
import sys

from funcoes import senha_fraca, senha_media, senha_forte, forca_senha

class GeradorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Senhas")
        self.setMinimumSize(700, 500)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Título ASCII estático
        ascii_text = pyfiglet.figlet_format("GERADOR DE SENHAS")
        self.title_label = QLabel(ascii_text)
        self.title_label.setFont(QFont("Courier", 16))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #FFFF;")  
        layout.addWidget(self.title_label)

        # Botões de geração e quantidade
        btn_layout = QHBoxLayout()
        self.btn_fraca = QPushButton("Gerar Senha Fraca")
        self.btn_media = QPushButton("Gerar Senha Média")
        self.btn_forte = QPushButton("Gerar Senha Forte")
        self.quantity_spin = QSpinBox()
        self.quantity_spin.setRange(1, 10)
        self.quantity_spin.setValue(1)
        self.quantity_spin.setPrefix("Quantidade: ")

        for btn in [self.btn_fraca, self.btn_media, self.btn_forte]:
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #2196F3; color: white;
                    padding: 10px; border: none; border-radius: 5px;
                    font-weight: bold; font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #2196F3;
                }
                """
            )
        btn_layout.addWidget(self.btn_fraca)
        btn_layout.addWidget(self.btn_media)
        btn_layout.addWidget(self.btn_forte)
        btn_layout.addWidget(self.quantity_spin)
        layout.addLayout(btn_layout)

        # Campo para senha própria
        self.custom_input = QLineEdit()
        self.custom_input.setPlaceholderText("Digite sua própria senha aqui")
        self.custom_input.setStyleSheet(
            "padding: 8px; font-size: 14px; border-radius: 5px; border: 1px solid #ccc;"
        )
        layout.addWidget(self.custom_input)

        # Botão avaliar
        self.btn_avaliar = QPushButton("Avaliar Senha")
        self.btn_avaliar.setStyleSheet(
            "background-color: #2196F3; color: white; padding: 10px; font-weight: bold; border-radius: 5px;"
        )
        layout.addWidget(self.btn_avaliar)

        # Área de resultados
        result_group = QGroupBox("Resultado")
        result_layout = QVBoxLayout()

        self.senha_label = QLabel("Senha gerada: ")
        self.senha_label.setFont(QFont("Courier", 12))
        self.forca_label = QLabel("Força: ")
        self.forca_label.setFont(QFont("Courier", 12))
        self.dicas_text = QTextEdit()
        self.dicas_text.setReadOnly(True)
        self.dicas_text.setStyleSheet("background-color: #f5f5f5; border-radius: 5px;")

        result_layout.addWidget(self.senha_label)
        result_layout.addWidget(self.forca_label)
        result_layout.addWidget(self.dicas_text)
        result_group.setLayout(result_layout)
        layout.addWidget(result_group)

        self.setLayout(layout)

        # Conectar botões
        self.btn_fraca.clicked.connect(lambda: self.gerar_senha("fraca"))
        self.btn_media.clicked.connect(lambda: self.gerar_senha("media"))
        self.btn_forte.clicked.connect(lambda: self.gerar_senha("forte"))
        self.btn_avaliar.clicked.connect(self.avaliar_senha)

    def gerar_senha(self, nivel):
        quantidade = self.quantity_spin.value()
        senhas_texto = []
        for _ in range(quantidade):
            if nivel == "fraca":
                senha = senha_fraca()
            elif nivel == "media":
                senha = senha_media()
            else:
                senha = senha_forte()
            forca, emoji, dicas = forca_senha(senha)
            senhas_texto.append(f"{senha} | {emoji} {forca}")
        self.senha_label.setText("Senhas geradas:\n" + "\n".join(senhas_texto))
        self.forca_label.setText("")
        self.dicas_text.setText("")

    def avaliar_senha(self):
        senha = self.custom_input.text()
        if senha.strip() == "":
            return
        forca, emoji, dicas = forca_senha(senha)
        self.senha_label.setText(f"Senha avaliada: {senha}")
        self.forca_label.setText(f"Força: {emoji} {forca}")
        self.dicas_text.setText("\n".join(dicas))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeradorGUI()
    window.show()
    sys.exit(app.exec())
