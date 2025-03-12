import requests

body = {
    "symbolBase": [
        {"symbol": "190032518", "symbolTyp": 4, "marketCd": 2},
        {"symbol": "140270018", "symbolTyp": 4, "marketCd": 2},
    ],
    "useLight": True,
    "withOffers": False,
}

resp = requests.post("https://trade.matsui.co.jp/mgap/resource/symbols/base", data=body)
resp.raise_for_status()
