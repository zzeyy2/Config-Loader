import os
import json
import yaml
from configparser import ConfigParser
from dotenv import dotenv_values
from pathlib import Path
from typing import NoReturn, Union


class WrapperMap:
    def __init__(self, d: dict):
        self.d = d

    def get_value(self):
        return self.d

    def __getattr__(self, item: str):
        value = self.d.get(item)
        if isinstance(value, dict):
            return self.__class__(value)

        return value

    def __repr__(self):
        return repr(self.d)


class ConfigLoader:
    def __init__(self, file_path: Union[str, Path]):
        self._load_config(self._process_path(file_path))

    def _process_path(self, path: Union[str, Path]):
        return Path(path) if not isinstance(path, Path) else path

    def _load_config(self, file_path: Path) -> NoReturn:
        name, ext = os.path.splitext(file_path.name)
        if ext == ".json":
            self._load_json_config(file_path)
        elif ext == ".ini":
            self._load_ini_config(file_path)
        elif ext == ".yaml":
            self._load_yaml_config(file_path)
        elif name == ".env":
            self._load_env_config(file_path)
        else:
            raise TypeError(f'Uknown file extension "{ext}"')

    def _load_ini_config(self, path: Union[str, Path]) -> NoReturn:
        parser = ConfigParser()
        parser.read(path)
        for section in parser.keys():
            setattr(self, section, WrapperMap(dict(parser[section])))

    def _load_json_config(self, path: Union[str, Path]) -> NoReturn:
        with open(path, "r") as file:
            data = json.load(file)
        for key, value in data.items():
            setattr(self, key, value)

    def _load_yaml_config(self, path: Union[str, Path]) -> NoReturn:
        with open(path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        for section in data:
            if not isinstance(section, str):
                for key, value in section.items():
                    setattr(
                        self,
                        key,
                        WrapperMap(value) if isinstance(value, dict) else value,
                    )
            else:
                setattr(
                    self,
                    section,
                    WrapperMap(data[section])
                    if isinstance(data[section], dict)
                    else data[section],
                )

    def _load_env_config(self, path: Union[str, Path]) -> NoReturn:
        config = dotenv_values(path)
        for k, v in config.items():
            setattr(self, k, WrapperMap(v) if isinstance(v, dict) else v)

    def get_attrs(self) -> dict:
        """Get all config attributes"""
        return vars(self)
