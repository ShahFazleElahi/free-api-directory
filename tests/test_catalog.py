import json, unittest, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from search import search
class CatalogTests(unittest.TestCase):
    def setUp(self): self.items=json.loads((ROOT/'data/catalog.json').read_text())
    def test_records(self):
        self.assertGreater(len(self.items), 10)
        self.assertEqual(len({x['name'].casefold() for x in self.items}),len(self.items))
        for x in self.items:
            self.assertTrue(x['url'].startswith('https://'))
            self.assertTrue(all(isinstance(v,str) and v.strip() for v in x.values()))
    def test_search(self):
        x=self.items[0]
        self.assertIn(x,search(self.items,x['name'].upper(),x['category'].upper()))
        self.assertEqual(search(self.items,'not-a-real-entry-123456789'),[])
if __name__=='__main__': unittest.main()
