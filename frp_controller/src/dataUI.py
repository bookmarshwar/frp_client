
from PyQt5.QtWidgets import (QPushButton, QLabel,
                             QHBoxLayout,QDialog,QLineEdit)
class SetDialog(QDialog):

    def __init__(self,name,local_port,server_port):
        super().__init__()

        self.name_edit = QLineEdit(name)
        self.local_port_edit = QLineEdit(local_port)
        self.server_port_edit = QLineEdit(server_port)

        self.button=QPushButton("ok!")
        layout = QHBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("名称")) 
        name_layout.addWidget(self.name_edit)

        port_layout = QHBoxLayout()
        port_layout.addWidget(QLabel("本地端口"))
        port_layout.addWidget(self.local_port_edit) 
        port_layout.addWidget(QLabel("服务端口"))
        port_layout.addWidget(self.server_port_edit)  
        self.button.clicked.connect(self.accept)
        layout.addLayout(name_layout)
        layout.addLayout(port_layout)
        layout.addWidget(self.button)


        self.setLayout(layout)
    def accept(self):

        if self.name_edit.text()=='' or self.local_port_edit.text()=='' or self.server_port_edit.text() =='':
            print(self.name_edit.text())
            print(self.local_port_edit.text())
            print(self.server_port_edit.text())
            print(0)
            return
        print(1)
        self.done(QDialog.Accepted)

