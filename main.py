import sel
import cut
import json
from PIL import Image
import asyncio

with open('config.json', 'r') as f:
    config = json.load(f)

async def make_timetable(config):
    sel.path = config['selenium']['path-to-gecko']
    w = config['website']

    print('--- logging into the website ---')
    sel.get_timetable(w['url'], w['username'], w['password'], '3a')
    print('--- took screenshot ---')
    cut.cut_pic('timetable.png', 0, 270, 1450, 1200)
    print('--- successfully cropped ---')


if __name__ == '__main__':
    asyncio.run(make_timetable(config))
    im = Image.open('cut_timetable.png')
    im.show()
