from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app  # Reference to Main App
        
        self.setWindowTitle("Login")
        layout = QVBoxLayout()

        self.label = QLabel("Enter Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Enter Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.authenticate)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # For now, simulate successful login
        if username == "admin" and password == "password":
            self.app.show_dashboard()
