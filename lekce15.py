# import requests as req
#
# token = "demo"
#
# res = req.get(f"https://eodhd.com/api/fundamentals/AAPL.US?api_token={token}&fmt=json")
#
# print(res.json())

import websocket

def on_message(wsapp, message):
    print(message)

# wsapp = websocket.WebSocketApp("wss://fstream.binance.com/ws/bnbusdt@aggTrade", on_message=on_message)
# wsapp.run_forever()