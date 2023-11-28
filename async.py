import asyncio
import aiohttp
import random


def show_link(image_link: dict) -> None:
    """Выводит ссылку."""

    print(f'Ссылка: {image_link}')
    return


async def make_async_request(number: int) -> dict:
    """Делает асинк запрос."""

    url = 'https://dog.ceo/api/breeds/image/random'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url)
        image_link = await response.json()
        show_link(image_link=image_link)

        print(f'Номер запроса: {number}')

        return image_link


async def main() -> None:
    """Основная кyрутина."""

    range_random = random.randint(1, 9)

    print(f'Запросов: {range_random}')

    tasks_list = []

    for iteration in range(range_random):
        number = iteration + 1
        task = asyncio.create_task(make_async_request(number=number))
        tasks_list.append(task)

    await asyncio.gather(*tasks_list, return_exceptions=True)


asyncio.run(main())
