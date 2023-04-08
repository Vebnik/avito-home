from dataclasses import dataclass


@dataclass
class Advertising:
    description: str
    title: str
    url: str
    value: str

    def to_dict(self):
        return {
            'description': self.description,
            'title': self.title,
            'url': self.url,
            'value': self.value,
        }

    def __str__(self) -> str:
        return f'{self.title} | {self.url}'

@dataclass
class AdvtType:
    home_time = 'kvartiry/sdam/na_dlitelnyy_srok'
