import requests

def locu_search_restaurant_in(query):
    api_key = "40dfc53d0ede8bd70fd6581addd44f3971ebf06b"
    url = "https://api.locu.com/v1_0/venue/search/?api_key=" + api_key
    locality = query.replace(" ","%20")
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = requests.get(final_url)
    data = json_obj.json()
    for item in data["objects"]:
        print(item["name"], item["phone"])
