import requests
import json

s = requests.Session()
s.get("https://www.dji.com/es/flysafe/geo-map")

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
	)
}


for spot in params_ua_spots:
	params = params_ua_spots[spot] + params_base
	response = s.get('https://www-api.dji.com/es/api/geo/areas', headers=headers, params=params)
	with open("zones/%s-zones.json" % spot, "w+") as f:
		r = response.json().get("areas")
		x = sorted(r, key=lambda x: (x['area_id'], x['name']))
		json.dump(x, f, indent=4)