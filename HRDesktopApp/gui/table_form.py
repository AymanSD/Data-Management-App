from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QLineEdit, QCheckBox, QDateEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QMessageBox
)
from PyQt5.QtCore import Qt
from db.db_session import SessionLocal

class TableForm(QWidget):
    def __init__(self, model_class, session, fields_per_row=3):
        """
        fields_per_row: how many fields to put in a single row
        """
        super().__init__()
        self.model_class = model_class
        self.session = session
        self.records = session.query(model_class).all()
        self.index = 0 if self.records else -1
        self.fields = {}
        self.fields_per_row = fields_per_row
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        form_widget = QWidget()
        self.form_layout = QGridLayout()
        self.form_layout.setHorizontalSpacing(20)
        self.form_layout.setVerticalSpacing(5)

        # Create form fields for all columns except primary keys
        row = 0
        col = 0
        for column in self.model_class.__table__.columns:
            if column.primary_key:
                continue
            name = column.name
            if str(column.type) == 'BOOLEAN':
                widget = QCheckBox()
            elif str(column.type) == 'DATE':
                widget = QDateEdit()
                widget.setCalendarPopup(True)
            else:
                widget = QLineEdit()
            self.fields[name] = widget

            label = QLabel(name)
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # Add label and widget side by side
            self.form_layout.addWidget(label, row, col*2)
            self.form_layout.addWidget(widget, row, col*2 + 1)

            col += 1
            if col >= self.fields_per_row:
                col = 0
                row += 1

        form_widget.setLayout(self.form_layout)
        scroll.setWidget(form_widget)
        layout.addWidget(scroll)

        # Navigation / Save buttons
        btn_layout = QHBoxLayout()
        self.prev_btn = QPushButton("Previous")
        self.next_btn = QPushButton("Next")
        self.save_btn = QPushButton("Save")

        self.prev_btn.clicked.connect(self.prev_record)
        self.next_btn.clicked.connect(self.next_record)
        self.save_btn.clicked.connect(self.save_record)

        btn_layout.addWidget(self.prev_btn)
        btn_layout.addWidget(self.next_btn)
        btn_layout.addWidget(self.save_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Load the first record if exists
        if self.records:
            self.load_record()

    def load_record(self):
        """Load the record at current index into the form fields"""
        if self.index == -1:
            # No records, just clear fields
            for widget in self.fields.values():
                if isinstance(widget, QCheckBox):
                    widget.setChecked(False)
                elif isinstance(widget, QDateEdit):
                    widget.setDate(widget.minimumDate())
                else:
                    widget.setText("")
            return

        record = self.records[self.index]
        for name, widget in self.fields.items():
            value = getattr(record, name, None)
            if isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    widget.setDate(value)
            else:
                widget.setText(str(value) if value is not None else "")

    def prev_record(self):
        if self.index > 0:
            self.index -= 1
            self.load_record()

    def next_record(self):
        if self.index < len(self.records) - 1:
            self.index += 1
            self.load_record()

    def save_record(self):
        if self.index == -1:
            # Table empty, create new record
            new_record = self.model_class()
            for name, widget in self.fields.items():
                if isinstance(widget, QCheckBox):
                    setattr(new_record, name, widget.isChecked())
                elif isinstance(widget, QDateEdit):
                    setattr(new_record, name, widget.date().toPyDate())
                else:
                    setattr(new_record, name, widget.text())
            self.session.add(new_record)
            self.session.commit()
            self.records.append(new_record)
            self.index = len(self.records) - 1
        else:
            # Update existing record
            record = self.records[self.index]
            for name, widget in self.fields.items():
                if isinstance(widget, QCheckBox):
                    setattr(record, name, widget.isChecked())
                elif isinstance(widget, QDateEdit):
                    setattr(record, name, widget.date().toPyDate())
                else:
                    setattr(record, name, widget.text())
            self.session.commit()

        QMessageBox.information(self, "Success", "Record saved successfully!")
