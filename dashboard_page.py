from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class DashboardWindow(QWidget):
    def __init__(self, app):
        super().__init__()

        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()

        self.label = QLabel("Welcome to the Dashboard!")
        layout.addWidget(self.label)

        self.setLayout(layout)
