from typing import Protocol
from abc import abstractmethod


class GetParametersServiceBase(Protocol):
    @abstractmethod
    async def get_parameters(self, ble_client):
        raise NotImplementedError('Abstract method get_parameters is not implemented')