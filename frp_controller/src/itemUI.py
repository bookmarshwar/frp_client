
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QHBoxLayout)
import shutil
import src.dataUI as DataUI
class ItemWidget(QWidget):

    def __init__(self, name,local_port,server_port,frp):
        super().__init__()
        self.open_status=False
        self.name = name
        self.local_port=local_port
        self.server_port=server_port
        self.frp=frp
        self.label = QLabel(name)
        self.button_open= QPushButton("⚫️")
        self.button_delete= QPushButton("删除")
        self.button_change= QPushButton("更改")
        self.button_open.clicked.connect(self.open)
        self.button_change.clicked.connect(self.change)
        self.button_delete.clicked.connect(self.delete)
        self.button_open.setStyleSheet("QPushButton {  " 
                        "border-radius: 50px; }")
        self.setup_ui()
        
    def setup_ui(self):

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_open)
        layout.addWidget(self.button_delete)
        layout.addWidget(self.button_change)
        self.setLayout(layout)
    def open(self):
        if self.open_status==False:
            self.button_open.setText("🔴")
            self.open_status=True
            self.frp.runfrp(self.name)
        else :
            self.button_open.setText("⚫️")
            self.open_status=False
            self.frp.stopfrp(self.name)
        print("open!")
    def delete(self):  
        self.deleteLater()
        if self.open_status ==True:
            self.frp.stopfrp(self.name)
        folder_path = f'res//data//{self.name}'
        shutil.rmtree(folder_path,ignore_errors=True)
    def change(self):
        lastname=self.name
        dialog = DataUI.SetDialog(self.name,self.local_port,self.server_port)

        if dialog.exec():
            self.name = dialog.name_edit.text()  
            self.local_port = dialog.local_port_edit.text()
            self.server_port = dialog.server_port_edit.text()
        self.label.setText(self.name)
        if self.open_status==True:
            self.frp.stopfrp(self.name)
            self.button_open.setText("⚫️")
            self.open_status=False
        self.frp.createIni(self.name,self.local_port,self.server_port)
        if lastname !=self.name:
            folder_path = f'res//data//{lastname}'
            shutil.rmtree(folder_path,ignore_errors=True)