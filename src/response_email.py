import html

import boto3
from tabulate import tabulate


FIELDS_TO_MAIL = [
  'link',
  'info',
  'city_text',
  'rooms',
  'price',
  'predicated_diff',
]

def _get_units_table(units):
  units_table = [FIELDS_TO_MAIL] + [[html.escape(str(unit[field])) for field in FIELDS_TO_MAIL] for unit in units]

  for i, row in enumerate(units_table[1:]):
    row[0] = f'<a href="{row[0]}">{html.escape(html.unescape(units[i]["main_title"]))}</a>'

  return units_table

def send_response_email(units_data):
  print('Sending response email')
  ses_client = boto3.client("ses")
  CHARSET = "UTF-8"

  good_units = [unit_data for unit_data in units_data if unit_data['predicated_diff'] <= 0]
  bad_units = [unit_data for unit_data in units_data if unit_data['predicated_diff'] > 0]

  html_body = f'''
  <html>
<head>
<style>
table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

td, th {{
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}}

tr:nth-child(even) {{
  background-color: #dddddd;
}}
</style>
</head>
<body>

<h2>New Units!</h2>

<h3>Good Offers</h3>
{tabulate(_get_units_table(good_units), tablefmt='unsafehtml')}

<h3>Bad Offers</h3>
{tabulate(_get_units_table(bad_units), tablefmt='unsafehtml')}

</body>
</html>
'''


  ses_client.send_email(
      Destination={
          "ToAddresses": [
              "alon.stern206@gmail.com",
          ],
      },
      Message={
          "Body": {
              "Html": {
                  "Charset": CHARSET,
                  "Data": html_body,
              }
          },
          "Subject": {
              "Charset": CHARSET,
              "Data": "New units!",
          },
      },
      Source="scraper@realestate-tracker.com",
  )
