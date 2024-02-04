import requests
from datetime import datetime


def logging_to_file(text_str: str):
    with open("report_file.txt", "a", encoding="utf-8") as file:
        file.write(text_str + "\n")


response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
sys_datetime = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
if response.status_code != 200:
    print("Виникла помилка при отриманні даних!")
else:
    logging_to_file(f"Date: {sys_datetime}")
    i = 1
    for x in response.json():
        logging_to_file(f"{i}. {x['txt']} to UAH: {x['rate']}")
        i += 1
    logging_to_file("-" * 20 + "END" + "-" * 20)
    print("Додані дані у файлі report_file.")
