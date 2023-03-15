from typing import Protocol
from abc import abstractmethod


class GetVoltServiceBase(Protocol):
    @abstractmethod
    async def get_volt(self):
        raise NotImplementedError('Abstract method get_volt is not implemented')