import logging
import json
import os
from bs4 import BeautifulSoup
from re import compile

from src.avito.models import Advertising, AdvtType
from src.http.http import Http
from src.utils.utils import Utils


class Avito:

    root_url = 'https://www.avito.ru'
    params: dict

    def __init__(self, params: dict) -> None:
        self.params = params

    def get_advt(self, save: bool) -> list[Advertising]:
        data: list[Advertising] = []

        for page in range(self.params.get('pages')):
            response = Http.get(self._url_compare(page))

            logging.info(f'{response.code} {response.status}')

            data.extend(self._parse_data(response.data))
            logging.info(f'Completed {page} page')

        try:
            if 'dist' not in os.listdir('.'):
                os.mkdir('dist')

            if save:
                with open(f"dist/{Utils.date()}.json", 'w') as file:
                    json_data = json.dumps(
                        obj=[item.to_dict() for item in data],
                        indent=2,
                        ensure_ascii=False
                    )
                    file.write(json_data)
        except Exception as ex:
            logging.critical(ex)

        return data

    def _url_compare(self, p=0) -> str:
        return f"{self.root_url}/{self.params.get('city')}/{AdvtType.home_time}?{p=}"

    def _parse_data(self, raw_data: str) -> list[Advertising]:
        try:
            soup = BeautifulSoup(raw_data, 'html.parser')
            return [
                Advertising(
                    title=item.find_next(class_=compile('iva-item-titleStep-')).text.replace('\xa0', ''),
                    value=item.find_next(class_=compile('iva-item-priceStep-')).text.replace('\xa0', ''),
                    description=item.find_next(class_=compile('iva-item-descriptionStep-')).text.replace('\xa0', ''),
                    url=f"{self.root_url}{item.find_next(class_=compile('iva-item-titleStep-')).find_next('a').get('href')}"
                ) for item in soup.find_all(class_=compile('iva-item-body-'))
            ]
        except Exception as ex:
            logging.critical(ex)