import src.readConfig as readConfig
import configparser
import os
import psutil
class frpController():
    def __init__(self) -> None:
        self.porcess_pool={}
        self.porcess_list=[]
        self.config=readConfig.FrpConfig()
        pass
    def createIni(self,name,local_port,sever_port):
        frpini = configparser.ConfigParser()
        frpini['common'] = {
        'server_addr': self.config.addr, 
        'server_port': self.config.port
        }

        frpini[name] = {
            'type': self.config.tpye,
            'local_ip': '127.0.0.1',
            'local_port': local_port,
            'remote_port': sever_port
        }
        path=f'res//data//{name}'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f'{path}//{name}.ini', 'w') as configfile:
            frpini.write(configfile)

    def args(self,name):
        return 'res\\frp\\frpc.exe','-c',f'res\\data\\{name}\\{name}.ini'
    def runfrp(self,name):
        process = psutil.Popen(self.args(name))
        self.porcess_pool[name]=process
        self.porcess_list.append(name)
        print(self.porcess_list)
    def stopfrp(self,name):
        porcess=self.porcess_pool[name]
        porcess.kill()
        self.porcess_list.remove(name)
        print(self.porcess_list)
    def close(self):
        for name in self.porcess_list:
            self.porcess_pool[name].kill()
            print(name)
        self.porcess_list=[]