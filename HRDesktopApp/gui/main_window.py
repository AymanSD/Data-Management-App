from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from gui.table_form import TableForm
from db.db_session import SessionLocal
from db.models import BasicInformation, ContractInfo, Roles, AccountsAccess, LeaveAbsence

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.session = SessionLocal()
        self.setWindowTitle("HR Desktop App")
        self.setGeometry(200, 100, 1000, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # --- Left Panel: Tab List ---
        self.tab_list = QListWidget()
        self.tab_list.setFixedWidth(180)  # Smaller width
        self.tab_list.setFont(QFont("Arial", 12, QFont.Bold))  # Larger text
        self.tab_list.setStyleSheet("""
            QListWidget::item {
                padding: 10px;
                border-radius: 8px;
            }
            QListWidget::item:selected {
                background-color: #367580;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #A1A1A1;
            }
        """)
        self.tab_list.addItems([
            "Basic Information",
            "Contract Info",
            "Roles",
            "Accounts & Access",
            "Leave & Absence"
        ])
        self.tab_list.currentRowChanged.connect(self.display_tab)
        main_layout.addWidget(self.tab_list)

        # --- Right Panel: Stacked Forms ---
        self.stack = QStackedWidget()
        self.forms = [
            TableForm(BasicInformation, self.session),
            TableForm(ContractInfo, self.session),
            TableForm(Roles, self.session),
            TableForm(AccountsAccess, self.session),
            TableForm(LeaveAbsence, self.session)
        ]
        for form in self.forms:
            self.stack.addWidget(form)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
        self.tab_list.setCurrentRow(0)

    def display_tab(self, index):
        self.stack.setCurrentIndex(index)
