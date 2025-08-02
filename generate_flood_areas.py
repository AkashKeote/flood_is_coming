import pandas as pd

df = pd.read_excel('mumbai_flood_risk_professional_dataset.xlsx')
unique = df.drop_duplicates(subset=['Coordinates','Key Areas Affected','Flood Risk Level','Water_Level_m','Water_Source'])

def parse_latlng(coord):
    try:
        lat, lon = map(float, coord.split(','))
        return f'LatLng({lat}, {lon})'
    except:
        return 'LatLng(0, 0)'

print('final List<_FloodArea> _floodAreas = [')
for row in unique[['Coordinates','Key Areas Affected','Flood Risk Level','Water_Level_m','Water_Source']].itertuples(index=False):
    print(f'  _FloodArea(')
    print(f'    name: "{row[1]}",')
    print(f'    position: {parse_latlng(row[0])},')
    print(f'    risk: "{row[2]}",')
    print(f'    waterLevel: {row[3]},')
    print(f'    source: "{row[4]}",')
    print(f'  ),')
print('];') 