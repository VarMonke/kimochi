__version__ = '0.0.1'
__author__ = 'VarMonke'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 VarMonke'

from typing import Optional
from typing_extensions import Self

import aiohttp

from .abc import BaseObject


class Client:

    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self.session = session if session else None

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            await self.session.close()

    async def __request(self, reaction: str) -> BaseObject:
        if self.session is None:
            self.session = aiohttp.ClientSession(headers={'User-Agent' : f'Kimochi Client (https://github.com/VarMonke/kimochi) @ {__version__}'})
        async with self.session.get(f'https://api.otakugifs.xyz/gif?reaction={reaction}') as response:
            return BaseObject(await response.json(), reaction)


    async def kiss(self) -> BaseObject:
        return await self.__request('kiss')

    async def hug(self) -> BaseObject:
        return await self.__request('hug')

    async def pat(self) -> BaseObject:
        return await self.__request('pat')

    async def slap(self) -> BaseObject:
        return await self.__request('slap')

    async def poke(self) -> BaseObject:
        return await self.__request('poke')

    async def cuddle(self) -> BaseObject:
        return await self.__request('cuddle')

    async def lick(self) -> BaseObject:
        return await self.__request('lick')

    async def bite(self) -> BaseObject:
        return await self.__request('bite')

    async def get(self, reaction: str) -> BaseObject:
        return await self.__request(reaction)

    async def close(self):
        if self.session is not None:
            await self.session.close()

    

    