import requests
from datetime import datetime

response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

if response.status_code != 200:
    print("Виникла помилка при отриманні даних!")
else:
    result = f"Date: {datetime.today().strftime('%d-%m-%Y %H:%M:%S')}\n"
    i = 1
    for x in response.json():
        result += f"{i}. {x['txt']} to UAH: {x['rate']}\n"
        i += 1
    with open("report_file.txt", "a", encoding="utf-8") as file:
        file.write(result + "\n")
    print("Додані дані у файлі report_file.")
