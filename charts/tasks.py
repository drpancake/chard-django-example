import httpx
from asgiref.sync import sync_to_async

import chard

from .models import ChartRank


@chard.task
async def get_itunes_charts(country_code):
    url = (
        "https://itunes.apple.com/WebObjects/MZStoreServices.woa/ws/"
        f"charts?cc={country_code}&name=Podcasts&limit=100"
    )
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        obj = resp.json()
    for i, itunes_id in enumerate(map(int, obj["resultIds"])):
        await sync_to_async(ChartRank.objects.create)(
            itunes_id=itunes_id, position=i + 1, country_code=country_code
        )
