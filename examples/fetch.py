import argparse, json, urllib.request
ENDPOINTS={
    'weather':'https://api.open-meteo.com/v1/forecast?latitude=24.89&longitude=91.87&current=temperature_2m',
    'earthquakes':'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=3&orderby=time',
    'books':'https://openlibrary.org/search.json?q=python&limit=3',
    'worldbank':'https://api.worldbank.org/v2/country/BGD/indicator/SP.POP.TOTL?format=json&per_page=3',
    'test':'https://jsonplaceholder.typicode.com/posts/1',
}
def main():
    p=argparse.ArgumentParser();p.add_argument('example',choices=ENDPOINTS);a=p.parse_args()
    req=urllib.request.Request(ENDPOINTS[a.example],headers={'User-Agent':'free-api-directory-learning-example/1.0','Accept':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=20) as response:
            body=response.read(2_000_001)
            if len(body)>2_000_000: raise ValueError('Response too large')
            print(json.dumps(json.loads(body),indent=2,ensure_ascii=False))
    except (OSError,ValueError) as e: p.exit(1,f'Request failed: {e}\n')
if __name__=='__main__':main()
