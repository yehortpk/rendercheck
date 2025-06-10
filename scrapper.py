import aiohttp

from models import ScrappingResult

SCRAPPER_HEADERS = {
    "User-Agent": "RenderCheckBot/0.1"
}

SCRAPPER_TIMEOUT_SEC = 5


class StaticScrapper:
    def __init__(self, url: str):
        self.url = url

    async def fetch(self) -> ScrappingResult:
        async with aiohttp.ClientSession(headers=SCRAPPER_HEADERS) as session:
            async with session.get(self.url, timeout=SCRAPPER_TIMEOUT_SEC) as response:
                text = await response.text()
                result = ScrappingResult(
                    url=str(response.url),
                    status=response.status,
                    html=text
                )

                return result

