from config import ConfigLoader


def test_env():
    ENV_config = ConfigLoader(r'tests/.env')
    print(ENV_config.get_attrs()) # {'username': 'zzeyy', 'password': '123l123'}
    print(ENV_config.username) # zzeyy
    print(ENV_config.password) # 123l123


def test_json():
    JSON_config = ConfigLoader(r'tests/config.json')
    print(JSON_config.get_attrs()) # {'url': 'example.url', 'user': 'root', 'password': 'rdxctfvygbuhinjomkpl!#'}
    print(JSON_config.url) # example.url
    print(JSON_config.user) # root
    print(JSON_config.password) # rdxctfvygbuhinjomkpl!#


def test_yaml():
    YAML_config = ConfigLoader(r'tests/config.yaml')
    print(YAML_config.get_attrs()) # {'version': 1.11, 'logger': {'level': 'DEBUG', 'format': '[%(asctime)s - %(name)s] | %(levelname)s: %(message)s'}}
    print(YAML_config.version) # 1.11
    print(YAML_config.logger) # {'level': 'DEBUG', 'format': '[%(asctime)s - %(name)s] | %(levelname)s: %(message)s'}
    print(YAML_config.logger.format) # [%(asctime)s - %(name)s] | %(levelname)s: %(message)s
    

def test_ini():
    INI_config = ConfigLoader(r'tests/config.ini')
    print(INI_config.get_attrs()) # {'DEFAULT': {}, 'BOT_CONFIG': {'token': '23626346346-dfgfdfggdfg:63463443', 'bot_name': 'zzeyy'}}
    print(INI_config.BOT_CONFIG.token) # 23626346346-dfgfdfggdfg:63463443
    print(INI_config.BOT_CONFIG.bot_name) # zzeyy
