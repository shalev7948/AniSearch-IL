import requests

def get_image(name):
    try:
        url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"
        res = requests.get(url).json()

        if res["data"]:
            return res["data"][0]["images"]["jpg"]["image_url"]
    except:
        return None
