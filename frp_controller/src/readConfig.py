import yaml,os
class FrpConfig():
    def __init__(self) -> None:
      self.read()
      pass
    def read(self):
        config_dir = r'res/config'
        if not os.path.exists(config_dir):
          os.makedirs(config_dir)
        with open(r'res/config/config.yml','r') as f:
          data = yaml.load(f, Loader=yaml.FullLoader)
        self.tpye=data['servers'][0]['type']
        self.name=data['servers'][0]['name']
        self.addr=data['servers'][0]['server_addr']
        self.port=data['servers'][0]['server_port']
