# Config-Loader
### Simple loader for your config

Working with the following formats: .env, .json, .ini, .yaml. 

Why use Config Loader? Because all that is required of you is to specify the path to the config file, and you will be able to freely access your config using the dot.
## Installing
```bash
pip3 install python-dotenv configparser pyyaml
```
1. Just import the config.py file into your project
2.
```python
from config import ConfigLoader
```

<details>
<summary>Usage</summary>

.ENV
```python
def test_env():  
    ENV_config = ConfigLoader('tests/.env')  
    print(ENV_config.get_attrs()) # {'username': 'zzeyy', 'password': '123l123'}  
    print(ENV_config.username) # zzeyy  
    print(ENV_config.password) # 123l123
```
.JSON
```python
def test_json():
    JSON_config = ConfigLoader('tests/config.json')
    print(JSON_config.get_attrs()) # {'url': 'example.url', 'user': 'root', 'password': 'rdxctfvygbuhinjomkpl!#'}
    print(JSON_config.url) # example.url
    print(JSON_config.user) # root
    print(JSON_config.password) # rdxctfvygbuhinjomkpl!#
```
.YAML
```python
def test_yaml():
    YAML_config = ConfigLoader('tests/config.yaml')
    print(YAML_config.get_attrs()) # {'version': 1.11, 'logger': {'level': 'DEBUG', 'format': '[%(asctime)s - %(name)s] | %(levelname)s: %(message)s'}}
    print(YAML_config.version) # 1.11
    print(YAML_config.logger) # {'level': 'DEBUG', 'format': '[%(asctime)s - %(name)s] | %(levelname)s: %(message)s'}
    print(YAML_config.logger.format) # [%(asctime)s - %(name)s] | %(levelname)s: %(message)s
```
.INI
```python
def test_ini():
    INI_config = ConfigLoader('tests/config.ini')
    print(INI_config.get_attrs()) # {'DEFAULT': {}, 'BOT_CONFIG': {'token': '23626346346-dfgfdfggdfg:63463443', 'bot_name': 'zzeyy'}}
    print(INI_config.BOT_CONFIG.token) # 23626346346-dfgfdfggdfg:63463443
    print(INI_config.BOT_CONFIG.bot_name) # zzeyy
```
</details>

### Tip 
If, for example, you want to create a config for a Telegram bot, then it’s better to call it BotConfig and the like. There is no need to name class objects IniConfig, JSON_CFG, etc.
