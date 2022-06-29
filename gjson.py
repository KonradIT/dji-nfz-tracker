# Helper class to convert a simple polygon into a GeoJSON object

from typing import List, Dict
from geojson import MultiPolygon

class GeoJSONHelper:
    
    def __init__(self):
        self.polygons = []
    
    def make(self) -> Dict:
        return MultiPolygon([
			(x) for x in self.polygons
		])
    
    def append(self, polygon):
        self.polygons.append(polygon)