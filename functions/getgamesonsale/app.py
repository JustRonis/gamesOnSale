import requests
import json
def lambda_handler(event, context):
    params = {'pageSize': 25}
    game_api_response = requests.get("https://www.cheapshark.com/api/1.0/deals", params=params)
    games = json.loads(game_api_response.content)

    [print(game) for game in games]

if __name__ == "__main__":
    lambda_handler({}, {})