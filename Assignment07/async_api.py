import time
import requests
import asyncio
import os
import dotenv


async def rhyme_finder(RHYME_FINDER_API_KEY, word):
    url = f"https://rhyming.ir/api/rhyme-finder?api={RHYME_FINDER_API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)
    return list(map(lambda x : x['word'], response.json()['data_items']))


def get_states():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)
    return response.json()


def get_cities(state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    return response.json()['cities']


async def get_coordinates(state_name, city_name):
    states_list = get_states()
    latitude = None
    longitude = None
    for state in states_list:
        if state['name'] == state_name:
            state_id = state['id']
            cities_list = get_cities(state_id)
            for city in cities_list:
                if city['name'] == city_name:
                    latitude = city['latitude']
                    longitude = city['longitude']
                    break
            else:
                print('Can\'t find your city.')
            break
    else:
        print('Can\'t find your state.')
    return latitude, longitude


async def main(RHYME_FINDER_API_KEY):
    coordinate, rhyme = await asyncio.gather(
        get_coordinates('خراسان رضوی', 'مشهد'),
        rhyme_finder(RHYME_FINDER_API_KEY, 'غریبا')
    )
    print(f'latitude: {coordinate[0]} longitude: {coordinate[1]} \nrhyme: {rhyme}')


if __name__ == "__main__":
    start_time = time.perf_counter()
    dotenv = dotenv.load_dotenv()
    RHYME_FINDER_API_KEY = os.getenv("RHYME_FINDER_API_KEY")
    asyncio.run(main(RHYME_FINDER_API_KEY))
    elapsed = time.perf_counter() - start_time
    print(f"Executed in {elapsed:0.3f} seconds.")
