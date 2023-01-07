import requests
def rates():
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    with open ('rates.csv', 'w') as file:
        k = 'Валюта, Курс'
        file.write(k)
        file.write('\n')
        for i in res['Valute']:
            a = str(res['Valute'][i]['Name']) + ',' + str(res['Valute'][i]['Value'])
            file.write(a)
            file.write('\n')