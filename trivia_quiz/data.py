import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

response_data = requests.get(url='https://opentdb.com/api.php', params=parameters)
response_data.raise_for_status()
response = response_data.json()

question_data = response['results']