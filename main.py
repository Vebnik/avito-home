from src.avito.avito import Avito
import logging
import argparse


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='A simple avito advt parser')

    parser.add_argument('pages', metavar='nums', type=int, nargs='+',
                        help='pages count to parse', default=0)
    parser.add_argument('city', metavar='city', type=str, nargs='+',
                        help='target city (ex: naberezhnye_chelny)', default='naberezhnye_chelny')
    args = parser.parse_args()

    params = {
        'city': args.city[0],
        'pages': args.pages[0],
    }

    avito = Avito(params)
    avito.get_advt(save=True)


if __name__ == '__main__':
    main()
