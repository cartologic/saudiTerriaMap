import requests, json, os

# Fetch and return all layers objects
def fetchData():
    response = requests.get("http://datagovsa.mapapps.cloud/api/layers/")
    data = response.json()["objects"]
    return data

allLayers = fetchData()

def filterCheck(category, obj):
    return "category__gn_description" in obj and obj["category__gn_description"] == category

def filterByCategory(category, objects=allLayers):
    categoryList = list(filter((lambda obj: filterCheck(category, obj)), objects))
    return categoryList

# Open Data categories
socialServicesList = filterByCategory("Social Services")
agricultureAndFishingList = filterByCategory("Agriculture and Fishing")
healthList = filterByCategory("Health")
tradeList = filterByCategory("Trade (Internal and External)")

transportList = filterByCategory("Transport and Communications")
educationAndTrainingList = filterByCategory("Education and Training")
weatherConditionsList = filterByCategory("Weather Conditions")
pricesAndIndicesList = filterByCategory("Prices and Indices")

economyAndPlanningList = filterByCategory("Economy and Planning")
monitoringAgenciesList = filterByCategory("Monitoring Agencies")
populationAndHousingList = filterByCategory("Population and Housing")
industryList = filterByCategory("Industry")

socialInsuranceList = filterByCategory("Social Insurance")
energyAndWaterList = filterByCategory("Energy and Water")
laborMarketList = filterByCategory("Labor Market")
openDataMigrationList = filterByCategory("Open Data Migration Group")

gccList = filterByCategory("Arab Gulf Cooperation Council (GCC)")
financialAndIndustryList = filterByCategory("Accounts Financial Monetary Affairs and Industry")


def getObjectKeys(object):
    keys = ["title", "typename"]
    newObject = {x: object[x] for x in keys}
    newObject["name"] = newObject.pop("title")
    newObject["type"] = "wms"
    newObject["url"] = "http://datagovsa.mapapps.cloud/geoserver/ows"
    newObject["layers"] = "geonode_data:" + newObject.pop("typename")
    newObject["opacity"] = 0.9

    return newObject


newSocialServicesList = list(map(getObjectKeys, socialServicesList))
newAgricultureAndFishingList = list(map(getObjectKeys, agricultureAndFishingList))
newHealthList = list(map(getObjectKeys, healthList))
newTradeList = list(map(getObjectKeys, tradeList))

newTransportList = list(map(getObjectKeys, transportList))
newEducationAndTrainingList = list(map(getObjectKeys, educationAndTrainingList))
newWeatherConditionsList = list(map(getObjectKeys, weatherConditionsList))
newPricesAndIndicesList = list(map(getObjectKeys, pricesAndIndicesList))

newEconomyAndPlanningList = list(map(getObjectKeys, economyAndPlanningList))
newMonitoringAgenciesList = list(map(getObjectKeys, monitoringAgenciesList))
newPopulationAndHousingList = list(map(getObjectKeys, populationAndHousingList))
newIndustryList = list(map(getObjectKeys, industryList))

newSocialInsuranceList = list(map(getObjectKeys, socialInsuranceList))
newEnergyAndWaterList = list(map(getObjectKeys, energyAndWaterList))
newLaborMarketList = list(map(getObjectKeys, laborMarketList))
newOpenDataMigrationList = list(map(getObjectKeys, openDataMigrationList))

newGccList = list(map(getObjectKeys, gccList))
newFinancialAndIndustryList = list(map(getObjectKeys, financialAndIndustryList))


terriaCatalogConfig = {
    "homeCamera": {
        "north": 30.390489396093574,
        "east": 62.986841147401385,
        "south": 16.293443380030926,
        "west": 28.72117778092538
    },
    "catalog": [
        {
            "name": "OPEN DATA datasets",
            "type": "group",
            "description": "The primary role of the platform is to publish datasets that belong to various categories which are initiated by Saudi ministries and government agencies in an open format, making this data available to the public. This platform enables the public to have central point of access to find, download and use datasets generated by the ministries and government agencies.\n\n**What is open data?**\n\nOpen data is the data that can be freely used by anyone without technical, financial or legal constraints. The open data can also be re-used and redistributed, taking into account the requirements of the legal license under which such data were distributed.\n\n More information about the open data platform, from [here](http://datagovsa.mapapps.cloud/).",
            "isOpen": True,
            "items": [
                {
                    "name": "Social Services",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newSocialServicesList
                },
                {
                    "name": "Agriculture and Fishing",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newAgricultureAndFishingList
                },
                {
                    "name": "Health",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newHealthList
                },
                {
                    "name": "Trade (Internal and External)",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newTradeList
                },
                {
                    "name": "Transport and Communications",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newTransportList
                },
                {
                    "name": "Education and Training",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newEducationAndTrainingList
                },
                {
                    "name": "Weather Conditions",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newWeatherConditionsList
                },
                {
                    "name": "Prices and Indices",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newPricesAndIndicesList
                },
                {
                    "name": "Economy and Planning",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items":newEconomyAndPlanningList
                },
                {
                    "name": "Monitoring Agencies",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newMonitoringAgenciesList
                },
                {
                    "name": "Population and Housing",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newPopulationAndHousingList
                },
                {
                    "name": "Industry",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newIndustryList
                },
                {
                    "name": "Social Insurance",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newSocialInsuranceList
                },
                {
                    "name": "Energy and Water",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newEnergyAndWaterList
                },
                {
                    "name": "Labor Market",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newLaborMarketList
                },
                {
                    "name": "Open Data Migration Group",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newOpenDataMigrationList
                },
                {
                    "name": "Arab Gulf Cooperation Council (GCC)",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newGccList
                },
                {
                    "name": "Accounts Financial Monetary Affairs and Industry",
                    "type": "group",
                    "isEnabled": True,
                    "zoomOnEnable": True,
                    "items": newFinancialAndIndustryList
                }
            ]
        }
    ]
}

script_dir = os.path.dirname(os.path.abspath(__file__)).split('/generateData')[0]
file_path = os.path.join(script_dir, 'init/saudiLayers.json')

with open(file_path, 'w') as outfile:
    json.dump(terriaCatalogConfig, outfile)
