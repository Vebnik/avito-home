from src.avito.avito import Avito
import logging


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    params = {
        'city': 'naberezhnye_chelny',
        'pages': 5,
    }

    avito = Avito(params)
    avito.get_advt(save=True)


if __name__ == '__main__':
    main()
