from typing import Protocol
from abc import abstractmethod


class ConnectServiceBase(Protocol):
    @abstractmethod
    async def connect(self):
        raise NotImplementedError('Abstract method connect is not implemented')