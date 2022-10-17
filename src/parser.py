import json
import re
import base64
import email
import sys
import aiohttp
import asyncio
from urllib.parse import parse_qs, urlencode, urlparse

import requests

from test_mail import test_mail1, test_mail2

LINKS_REGEX = re.compile('https?://[^\s]+startDate[^\s]+', re.MULTILINE)

YAD_2_SEARCH_URL = 'https://gw.yad2.co.il/feed-search-legacy/realestate/forsale'
YAD_2_UNIT_URL = 'https://gw.yad2.co.il/feed-search-legacy/item'

def _get_unit_metadata(link):
  query = parse_qs(urlparse(link).query)
  query['forceLdLoad'] = True

  page = 0
  last_page = None
  
  units_metadata = set()
  while page != last_page:
    page += 1
    query['page'] = page

    print(f'GET {YAD_2_SEARCH_URL}?{urlencode(query)}', file=sys.stderr)
    res = requests.get(YAD_2_SEARCH_URL, params=query).json()
    last_page = res['data']['pagination']['last_page']
    total_items = res['data']['pagination']['total_items']

    for item in res['data']['feed']['feed_items']:
      if 'id' not in item:
        continue

      metadata = (item['id'], item['abovePrice'])
      if metadata in units_metadata:
        continue

      units_metadata.add(metadata)

  print(f'{len(units_metadata)} units found', file=sys.stderr)
  return list(units_metadata)

async def _get_unit_data(session, url):
  async with session.get(url) as resp:
    resp_json = await resp.json()
    print(f'Received response for url {url}', file=sys.stderr)
    return resp_json['data']


async def _get_all_unit_data(units_metadata):
  units = []

  async with aiohttp.ClientSession() as session:
    tasks = []
    for [id, _] in units_metadata:
      url = f'{YAD_2_UNIT_URL}?token={id}'
      print(f'GET {url}', file=sys.stderr)
      tasks.append(asyncio.ensure_future(_get_unit_data(session, url)))

    responses = await asyncio.gather(*tasks)
    for i, resp in enumerate(responses):
      resp['abovePrice'] = units_metadata[i][1]
      units.append(resp)

  return units

def _extract_unit_data(unit):
  items = { item['key']: item['value'] for item in unit['additional_info_items_v2'] }
  info_items = { item['key']: item['value'] for item in unit['important_info_items'] }

  return {
    'boiler': items['boiler'],
    'renovated': items['renovated'],
    'warhouse': items['warhouse'],
    'tadiran': items['tadiran_c'],
    'address_description': unit.get('address_more'),
    'air_conditioner': unit['analytics_items']['air_conditioner'] != 0,
    'building_mr': unit['analytics_items']['building_mr'],
    'elevator': unit['analytics_items']['elevator'] != 0,
    'floor': unit['analytics_items']['floor'],
    'furniture': unit['analytics_items']['furniture'] != 0,
    'handicapped': unit['analytics_items']['handicapped'] != 0,
    'on_pillars': unit['analytics_items']['on_pillars'] != 0,
    'rooms': unit['analytics_items']['rooms'],
    'shelter_room': unit['analytics_items']['shelter_room'],
    'storeroom': unit['analytics_items']['storeroom'],
    'area_id': unit['area_id'],
    'balconies': unit['balconies'],
    'city_text': unit['city_text'],
    'date_added': unit['date_added'],
    'garden_area': unit['garden_area'],
    'link': f'https://www.yad2.co.il/item/{unit["id"]}',
    'info': unit['info_text'],
    'main_title': unit['main_title'],
    'longitude': unit['navigation_data']['coordinates']['longitude'],
    'latitude': unit['navigation_data']['coordinates']['latitude'],
    'neighborhood': unit['neighborhood'],
    'on_pillars': unit['on_pillars'] != 0,
    'parking': unit['parking'] != '1',
    'price': int(unit['price'].replace('₪', '').replace(',', '').strip()),
    'square_meters': unit['square_meters'],
    'street': unit.get('street'),
    'mediation': 'משרד תיווך' in info_items,
    'abovePrice': int(unit['abovePrice']),
    'asset_classification': str(unit['analytics_items'].get('asset_classification'))
  }


async def parse_mail(mail_content):
  message = email.message_from_string(mail_content)

  if (isinstance(message.get_payload(), str)):
    body = message.get_payload(decode=True).decode()
  else:
    submessage = message.get_payload()[0]
    if (submessage['Content-Transfer-Encoding'] == 'base64'):
      body = base64.b64decode(message.get_payload()[0].get_payload()).decode()
    else:
      body = message.get_payload()[0].get_payload()

  url = LINKS_REGEX.findall(body)[0]
  units_metadata = _get_unit_metadata(url)
  units = await _get_all_unit_data(units_metadata)

  units_data = []
  for unit in units:
    try: 
      units_data.append(_extract_unit_data(unit))
    except Exception as e:
      print(f'Error parsing unit {unit["id"]}', file=sys.stderr)
      print(e, file=sys.stderr)
      continue
  return units_data

if __name__ == '__main__':
  print(asyncio.run(parse_mail(test_mail1)))
  # print(asyncio.run(parse_mail(test_mail2)))
