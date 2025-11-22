import sys
import os

# Add the app root folder to sys.path so Python can find gui/ and db/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from db.db_session import SessionLocal
from db.models import BasicInformation, ContractInfo, Roles, AccountsAccess, LeaveAbsence
from gui.table_form import TableForm

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HR Dashboard")
        self.setGeometry(400, 150, 800, 400)
        self.setup_ui()
        self.load_employees()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        layout.addWidget(self.table)
        
        self.add_btn = QPushButton("Add Employee")
        self.add_btn.clicked.connect(self.add_employee)
        layout.addWidget(self.add_btn)
        
        self.setLayout(layout)

    def load_employees(self):
        session = SessionLocal()
        employees = session.query(BasicInformation).all()
        session.close()

        self.table.setRowCount(len(employees))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Department", "Position", "Email"])
        
        for i, emp in enumerate(employees):
            self.table.setItem(i, 0, QTableWidgetItem(str(emp.id)))
            self.table.setItem(i, 1, QTableWidgetItem(emp.first_name))
            self.table.setItem(i, 2, QTableWidgetItem(emp.last_name))
            self.table.setItem(i, 3, QTableWidgetItem(emp.department or ""))
            self.table.setItem(i, 4, QTableWidgetItem(emp.position or ""))
            self.table.setItem(i, 5, QTableWidgetItem(emp.email or ""))

    def add_employee(self):
        self.form = TableForm(self)
        self.form.show()
