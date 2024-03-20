from typing import Protocol
from abc import abstractmethod


class ScanServiceBase(Protocol):
    @abstractmethod
    async def scan(self):
        raise NotImplementedError('Abstract method get_volt is not implemented')