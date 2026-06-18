# Grade 10 Geography: Mapwork

## Overview
Mapwork involves the interpretation of topographical maps, orthophoto maps, and standard maps. 

## Co-ordinates
Coordinates pinpoint absolute locations using Latitude (South of the equator) and Longitude (East of the prime meridian).

## Geographic Rendering
To show students specific locations, use the `render_visual` tool.
Set `type="geography"`.
The `data` should be a JSON string like:
```json
{
  "lat": -26.2041,
  "lng": 28.0473,
  "zoom": 10,
  "markers": [
    {"lat": -26.2041, "lng": 28.0473, "popupText": "Johannesburg"}
  ]
}
```

## Scale
Scale represents the ratio between distance on a map and the actual distance on the ground.
Example: 1:50 000 means 1 unit on the map represents 50 000 units on the ground.
