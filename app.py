from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from login_page import LoginWindow  # Import the Login Page class
from dashboard_page import DashboardWindow  # Import the Dashboard UI

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Analyzer App")
        self.setGeometry(100, 100, 800, 600)

        # Stacked Widget to Switch Between Login and Dashboard
        self.stack = QStackedWidget()
        self.login_page = LoginWindow(self)
        self.dashboard_page = DashboardWindow(self)

        # Add Pages to Stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.dashboard_page)

        # Set Login as Default Page
        self.setCentralWidget(self.stack)

    def show_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard_page)

app = QApplication([])
window = App()
window.show()
app.exec()
