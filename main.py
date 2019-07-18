import sel
import cut
import json

with open('config.json', 'r') as f:
    config = json.load(f)

sel.path = config['selenium']['path-to-gecko']
w = config['website']

print('--- logging into the website ---')
sel.get_timetable(w['url'], w['username'], w['password'], '2e')
print('--- took screenshot ---')
cut.cut_pic('timetable.png', 0, 270, 1450, 1200)
print('--- successfully cropped ---')