from requests_html import HTMLSession
from abc import ABC, abstractmethod
import json


class BaseParser(ABC):
    _data = []
    _url = None

    def __init__(self, url, session=None) -> None:
        self._url = url
        self.session = session or HTMLSession()

    def get_page_html(self):
        try:
            response = self.session.get(self._url)
            if response.status_code == 200:
                return response
        except Exception as err:
            print(err)

    @abstractmethod
    def parse(self):
        raise NotImplementedError("Abstract method should be implemented")

    def save(self, file_name: str):
        with open(file_name, "a") as file:
            file.write(json.dumps(self._data, indent=4, ensure_ascii=False))
