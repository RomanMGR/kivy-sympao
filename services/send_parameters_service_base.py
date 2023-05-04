from typing import Protocol
from abc import abstractmethod


class SendParametersServiceBase(Protocol):
    @abstractmethod
    async def send_anode(self, ble_client, n):
        raise NotImplementedError('Abstract method get_parameters is not implemented')