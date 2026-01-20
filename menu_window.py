from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class MenuWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Меню")
        self.resize(300, 200)

        layout = QVBoxLayout()
        btn_back = QPushButton("⬅ Назад")

        btn_back.clicked.connect(self.go_back)

        layout.addWidget(btn_back)
        self.setLayout(layout)

        self.parent = parent

    def go_back(self):
        self.close()
        if self.parent:
            self.parent.show()
