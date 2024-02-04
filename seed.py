import os
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

api_host = os.environ.get('ITEM_API_HOST', 'http://localhost:8001')

mario_kart_items = [
    "Mushroom",
    "Triple Mushrooms",
    "Golden Mushroom",
    "Green Shell",
    "Red Shell",
    "Triple Green Shells",
    "Triple Red Shells",
    "Banana",
    "Triple Bananas",
    "Star",
    "Bullet Bill",
    "Lightning",
    "Blooper",
    "Bob-omb",
    "Coin",
    "Boomerang Flower",
    "Piranha Plant",
    "Super Horn",
    "Crazy Eight",
    "Spiny Shell",
    "Fake Item Box",
    "Lucky 7",
    "Fire Flower",
]

print('\n\n### ADDING ITEMS TO DATABASE ###\n\n')
for item in mario_kart_items:
    logger.info(f"Adding item: '{item}'.")
    response = requests.post(f'{api_host}/items', json={'name': item})
    if response.status_code != 200:
        logger.info(f'Failed upload: {response.text}')

print('\n\n### ITEMS IN DATABASE ###\n\n')
response = requests.get(f'{api_host}/items')
for item in response.json():
    print(f'>>> {item["name"]}')