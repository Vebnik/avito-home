import datetime


class Utils:

    @staticmethod
    def date() -> str:
        return datetime.datetime.today().strftime('%Y-%m-%d_%H-%M')
