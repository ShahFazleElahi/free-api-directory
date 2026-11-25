import argparse, json
from pathlib import Path
def search(items, query='', category=''):
    return [x for x in items if query.casefold() in ' '.join(x.values()).casefold() and (not category or x['category'].casefold()==category.casefold())]
def main():
    parser=argparse.ArgumentParser(description='Search the offline directory')
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--category', default='')
    parser.add_argument('--json', action='store_true')
    a=parser.parse_args()
    items=json.loads((Path(__file__).resolve().parents[1]/'data/catalog.json').read_text())
    result=search(items,a.query,a.category)
    if a.json: print(json.dumps(result,indent=2,ensure_ascii=False))
    else:
        for x in result: print(f"{x['name']} [{x['category']}] — {x['url']}")
        print(f'{len(result)} matches')
if __name__=='__main__': main()
