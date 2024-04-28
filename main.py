import asyncio
import aiohttp
import config
from config import ParseResult
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://emall.by/category/3855'


async def main():
    with open('parse_result.txt', encoding='UTF-8', mode='w+') as file:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=BASE_URL) as response:
                r = await aiohttp.StreamReader.read(response.content)
                soup = BS(r, 'html.parser')
                items = soup.find_all('div', {'class': 'adult-wrapper_adult__eCCJW vertical_pro'
                                                       'duct__Q8mUI products_product_vertical__Sovsr'})
                res = []
                for i in items:
                    price = i.find('span', {'class': 'price_main__5jwcE'}).text.strip().replace('\xa0р.', '')
                    title = i.find('a', {'class': 'vertical_title__9_9cV vertical_title_with_actions__e4aNO'}).text.strip().replace('Кофе растворимый', '')
                    link = f"{'https://emall.by' + i.find('a', {'class': 'vertical_title__9_9cV vertical_title_with_actions__e4aNO'}).get('href')}"
                    res.append(ParseResult(title, price, link))

                output_info = config.OutputValues(res=res, file=file)
                print(output_info.printing())
                print(output_info.profitable())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
