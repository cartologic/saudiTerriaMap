import requests, os, json

API_URL = "http://mapsaudi.com/api/"

terriaCatalogConfig = {
    "homeCamera": {
        "north": 30.390489396093574,
        "east": 62.986841147401385,
        "south": 16.293443380030926,
        "west": 28.72117778092538
    },
    "catalog": [
        {
            "name": "MapSaudi datasets",
            "type": "group",
            "description": "The primary role of the platform is to publish datasets that belong to various categories which are initiated by Saudi ministries and government agencies in an open format, making this data available to the public. This platform enables the public to have central point of access to find, download and use datasets generated by the ministries and government agencies.\n\n**What is open data?**\n\nOpen data is the data that can be freely used by anyone without technical, financial or legal constraints. The open data can also be re-used and redistributed, taking into account the requirements of the legal license under which such data were distributed.\n\n More information about the open data platform, from [here](http://mapsaudi.com/).",
            "isOpen": True,
            "items": []
        }
    ]
}

def fetch_resources(resource, parameter=None):
    if parameter: # Request layers by category
        response = requests.get(API_URL + "{}/?category__identifier__in={}".format(resource, parameter))
    else: # Request categories
        response = requests.get(API_URL + "{}".format(resource))
    return response.json()["objects"]


def create_terria_element(object):
    keys = ["title", "detail_url"]
    terria_element = {x: object[x] for x in keys}
    terria_element["name"] = terria_element.pop("title")
    terria_element["type"] = "wms"
    terria_element["url"] = "http://mapsaudi.com/geoserver/ows"
    terria_element["layers"] = terria_element.pop("detail_url").split('/layers/')[1]
    terria_element["opacity"] = 0.9

    return terria_element


def create_terria_categories(categories):
    for category in categories:
        category_layers = fetch_resources('layers', category['identifier'])
        terria_layers = list(map(create_terria_element, category_layers))
        terria_category = {
            "name": category['gn_description'],
            "type": "group",
            "isEnabled": True,
            "zoomOnEnable": True,
            "items": terria_layers
        }
        catalog = terriaCatalogConfig['catalog']
        catalog[0]['items'].append(terria_category)


def main():
    categories = fetch_resources('categories')
    create_terria_categories(categories)

    script_dir = os.path.dirname(os.path.abspath(__file__)).split('/generateData')[0]
    file_path = os.path.join(script_dir, 'init/saudiLayers.json')

    with open(file_path, 'w', encoding='utf8') as outfile:
        json.dump(terriaCatalogConfig, outfile, ensure_ascii = False)


if __name__ == "__main__":
    main()
