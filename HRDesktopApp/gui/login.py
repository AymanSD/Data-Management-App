from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from db.db_session import SessionLocal
from db.models import User

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HR System Login")
        self.setGeometry(600, 300, 300, 150)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        
        layout.addWidget(QLabel("HR System Login"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)

    def check_login(self):
        user_text = self.username.text()
        pwd_text = self.password.text()
        session = SessionLocal()
        user = session.query(User).filter_by(username=user_text, password=pwd_text).first()
        session.close()
        if user:
            from gui.dashboard import DashboardWindow
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")
