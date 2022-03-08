import requests
import json

s = requests.Session()

response = s.get("https://app.autelrobotics.com/personal_center/index.php/Utils/fetchNoflyzoneinfo")
with open("zones_autel/all-zones.json", "w+", encoding='utf8') as f:
	r = response.json().get("data").get("noflyzones")
	json.dump(r, f, indent=4, ensure_ascii=False)

response = s.get("https://app.autelrobotics.com/personal_center/index.php/Utils/fetchNfzEnabledCountrys")
with open("zones_autel/enabled-countries.json", "w+", encoding='utf8') as f:
	r = response.json().get("data").get("countrys")
	json.dump(r, f, indent=4, ensure_ascii=False)