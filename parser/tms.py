from .base import BaseParser


class TMS(BaseParser):
    __names_selector = "div.kcen6d span"
    __links_selector = "div.aoJE7e.b0ZfVe"

    def parse(self):
        page = self.get_page_html()
        names = page.html.find(self.__names_selector)
        links = page.html.find(self.__links_selector)
        self._data = [{"name": names[i].text, "links": list(links[i].absolute_links)} for i in range(len(names))]
