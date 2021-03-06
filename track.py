from typing import Optional, Tuple, List
import requests
import json
from gjson import GeoJSONHelper

s = requests.Session()
s.get("https://www.dji.com/es/flysafe/geo-map")

gj = GeoJSONHelper()

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.dji.com/es/flysafe/geo-map',
	'Origin': 'https://www.dji.com',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'Sec-GPC': '1',
	'TE': 'trailers',
}

params_base = (
		('country', 'UA'),
		('drone', 'dji-mavic-3'),
		('level', '1,2,4,7'),
		('zones_mode', 'total'),
)

params_ua_spots = {
	"kyiv": (
		('lng', '30.584250786011808'),
		('lat', '50.493588015005315'),
		('search_radius', '139225')
	),
	"lviv": (
		("lng", "24.6242284128125"),
		("lat", "49.60442393085867"),
		("search_radius", "216995"),
	),
	"mariupol-kharkiv": (
		("lng", "35.379776104271286"),
		("lat","47.917047252258214"),
		("search_radius", "245113")
	),
	"dnipro": (
		("lng", "34.92684203119086"),
  		("lat", "48.29874265530242"),
		("search_radius", "153387")
	)
}

def as_geojson(spot) -> Optional[List[Tuple[int, int]]]:
    if  spot.get("polygon_points") == None:
        return None
    p = spot.get("polygon_points")[0]
    return [[(x[0], x[1]) for x in p]]

for spot in params_ua_spots:
	params = params_ua_spots[spot] + params_base
	response = s.get('https://www-api.dji.com/es/api/geo/areas', headers=headers, params=params)
	r = response.json().get("areas")
	x = sorted(r, key=lambda x: (x['area_id'], x['name']))
	with open("zones/%s-zones.json" % spot, "w+", encoding='utf8') as f:
		json.dump(x, f, indent=4, ensure_ascii=False)
	for zone in x:
		result = as_geojson(zone.get("sub_areas")[0])
		if result != None:
			gj.append(result)
	with open("zones/all-ukraine-zones.geojson", "w+", encoding="utf-8") as geofile:
		json.dump(gj.make(), geofile, indent=4, ensure_ascii=False)