# Tracking DJI GEO ZONE NoFlyZone (NFZ)

## Introduction:

This is a Python service that keeps track of which No Fly Zones are currently displayed on [DJI's GEO map](https://www.dji.com/es/flysafe/geo-map) site.

## Backstory:

SZ DJI Technology - Da Jiang Innovations, commonly known as DJI, is the world's largest drone maker, having over 70% of [global market share of consumer and commercial drones based on sales volume](https://www.statista.com/statistics/1254982/global-market-share-of-drone-manufacturers/). DJI operates out of Shenzhen, China.

If you've ever seen a consumer / cinema quadcopter, chances are it was made by DJI.

DJI develops their own software stack that ships on their drones, as well as the APIs, SDKS, mobile apps, remote controllers and firmware update OTA infra. This allows more control over how a drone can be used versus competitors who opt for open source flight controllers and remote control platforms (betaflight, ardupilot...).

DJI has been subject to scrutiny from the US, thus not allowing DoI, DoD to buy DJI drones, and being placed on the Bureau of Industry and Security's Entity List in 2020.

In 2017, DJI released an update to their No Fly Zone system - a list of places where a drone cannot fly, which is polled via the Mobile App - to [effectively ban most of Syrian and Iraqi airspace](https://www.theregister.com/2017/04/26/dji_drone_geofencing_iraq_syria/). Believed to have been implemented to stop ISIS from using DJI drones to drop bombs. 

This software tracks No Fly Zones on 4 different zones:

- Kyiv 🇺🇦
- Lviv area 🇺🇦
- Mariupol 🇺🇦
- Kharkiv 🇺🇦