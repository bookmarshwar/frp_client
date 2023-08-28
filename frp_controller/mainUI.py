import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QScrollArea, 
                             QDialog,QLineEdit)
from PyQt5.QtCore import Qt
import src.frpController as frpController
import os
import configparser
import src.itemUI as ItemUI

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


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.frp=frpController.frpController()
        self.setup_ui()
        self.readData()
    def setup_ui(self):
        self.addButton = QPushButton("添加")
        
        self.scroll_area = QScrollArea()
        
        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)
        layout.setAlignment(Qt.AlignTop) # 设置对齐方式为上对齐

        layout.setContentsMargins(0, 0, 0, 0) # 移除内边距
        layout.setSpacing(0) # 移除控件间距
        self.scroll_area.setWidget(content_widget)
        self.scroll_area.setWidgetResizable(True)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scroll_area)
        main_layout.addWidget(self.addButton)
        self.addButton.clicked.connect(self.add_item)
        
        self.setLayout(main_layout)
        
    def add_item(self):
        dialog = SetDialog('','','')

        if dialog.exec():
            name = dialog.name_edit.text()  
            local_port = dialog.local_port_edit.text()
            server_port = dialog.server_port_edit.text()
        item = ItemUI.ItemWidget(name,local_port,server_port,self.frp)
        
        layout = self.scroll_area.widget().layout()
        layout.addWidget(item)
        self.frp.createIni(name,local_port,server_port)
    def readData(self):
        folder_path = r'res/data'
        files = os.listdir(folder_path)
        config = configparser.ConfigParser()
        for name in files:
            config.read(f'{folder_path}//{name}//{name}.ini') 
            item = ItemUI.ItemWidget(name,config[name]['local_port'],config[name]['remote_port'],self.frp)
        
            layout = self.scroll_area.widget().layout()
            layout.addWidget(item)
    def closeEvent(self, event):
        print("Window closing")
        self.frp.close()
  # 清理工作

        event.accept()
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())