from dataclasses import dataclass


@dataclass
class Response:
    code: int
    status: bool
    data: dict | str | None
