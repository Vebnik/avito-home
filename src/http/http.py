from requests import get
from src.http.models import Response
import logging


class Http:

    request_config = {
        'allow_redirects': True
    }

    @classmethod
    def get(cls, url: str) -> Response:
        try:
            res = get(url, **cls.request_config)

            if res.ok:
                return Response(
                    code=res.status_code,
                    status=True,
                    data=(res.json() if res.headers.get('content-type') == 'application/json' else res.text)
                )
            return Response(code=res.status_code, status=False, data=None)
        except Exception as ex:
            logging.critical(ex)
