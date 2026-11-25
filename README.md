# Free API Directory
Public APIs for learning, prototypes and research. Public access does not imply unlimited or commercial use. Always read provider terms.
**30 entries** • JSON dataset • Offline search CLI
## Contents
- [Weather and science](#weather-and-science)
- [Geography](#geography)
- [Public data](#public-data)
- [Research and books](#research-and-books)
- [Developer data](#developer-data)

## Weather and science
| API | Authentication / access | Use case |
| --- | --- | --- |
| [Open-Meteo](https://open-meteo.com/en/docs) | No key for eligible non-commercial access | Forecasts and historical weather; commercial terms differ |
| [USGS Earthquake Catalog](https://earthquake.usgs.gov/fdsnws/event/1/) | No key | Earthquake event searches |
| [NASA Open APIs](https://api.nasa.gov/) | API key or limited DEMO_KEY | Space and Earth science; endpoint-specific limits |
| [US National Weather Service](https://www.weather.gov/documentation/services-web-api) | No key; identifying User-Agent | US weather alerts and forecasts |
| [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/webservices/v2) | Token | Climate station and observation data |

## Geography
| API | Authentication / access | Use case |
| --- | --- | --- |
| [REST Countries](https://restcountries.com/) | Check current version and access rules | Country metadata |
| [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | No key on public instance; strict policy | Geocoding; no bulk use on public server |
| [GeoNames](https://www.geonames.org/export/web-services.html) | Registered username | Place names and coordinates |
| [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API_v0.6) | Authentication for edits | Map data editing API; not a general bulk query service |

## Public data
| API | Authentication / access | Use case |
| --- | --- | --- |
| [World Bank Indicators](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information) | No key | International development indicators |
| [UNdata](https://data.un.org/Host.aspx?Content=API) | See service documentation | International statistical datasets |
| [Eurostat](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access) | No key for public data | European statistics |
| [US Census](https://www.census.gov/data/developers.html) | Key recommended or required depending on use | US population and economic data |
| [Nager.Date](https://date.nager.at/Api) | No key for public API | Public holidays for supported countries |

## Research and books
| API | Authentication / access | Use case |
| --- | --- | --- |
| [Open Library](https://openlibrary.org/developers/api) | No key for public endpoints | Book search and bibliographic metadata |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | No key for public pool; identify client | DOI and scholarly metadata |
| [Europe PMC](https://europepmc.org/RestfulWebService) | No key for public search | Biomedical literature metadata |
| [OpenAlex](https://docs.openalex.org/) | Check key and current free allowance | Scholarly works and institutions |
| [arXiv](https://info.arxiv.org/help/api/index.html) | No key; usage policy applies | Preprint metadata |
| [Wikimedia APIs](https://www.mediawiki.org/wiki/API:Main_page) | Public reads; auth for writes | Wiki content and metadata |
| [Wikidata Query Service](https://query.wikidata.org/) | No key for public queries; limits apply | Structured linked data via SPARQL |

## Developer data
| API | Authentication / access | Use case |
| --- | --- | --- |
| [GitHub REST API](https://docs.github.com/en/rest) | Public reads may be keyless; auth raises limits | Public repository and user metadata |
| [npm Registry](https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md) | Public package metadata generally keyless | Package information |
| [PyPI JSON API](https://docs.pypi.org/api/json/) | No key for public package reads | Python package metadata |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | No key | Fake REST data for testing; writes simulated |
| [httpbin](https://httpbin.org/) | No key on public instance | Inspect HTTP request behavior |
| [Open Food Facts](https://openfoodfacts.github.io/openfoodfacts-server/api/) | Public reads; identify client; quotas | Food product metadata; database license applies |
| [PokéAPI](https://pokeapi.co/docs/v2) | No key; fair-use policy | Pokémon reference data |
| [TVmaze](https://www.tvmaze.com/api) | No key for public API | TV show metadata; attribution rules apply |
| [Frankfurter](https://frankfurter.dev/) | See current public service terms | Reference exchange rates, not trading quotes |

## Search locally
Requires Python 3.9+; no dependencies.
```bash
python3 scripts/search.py postgres
python3 scripts/search.py --category "Weather and science"
python3 scripts/search.py --json
```
## Data and contributions
Machine-readable records: [`data/catalog.json`](data/catalog.json). See [CONTRIBUTING.md](CONTRIBUTING.md) for adding entries.
External services, licensing, quotas and eligibility can change. Check the linked official documentation before using a tool or API. This initial catalog has not been exhaustively live-tested.

## API examples

Run `python3 examples/fetch.py weather` (eligible non-commercial use), `books`, `earthquakes`, `worldbank`, or `test`. Network access is required; these are read-only examples and provider availability is not guaranteed.

## License

Original repository code and text are offered under the [MIT License](LICENSE). Linked services, brands, data and documentation retain their own terms and licenses.
