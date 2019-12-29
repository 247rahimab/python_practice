from bs4 import BeautifulSoup
import requests
from time import sleep
import json


def get_page_content(page_url):
    max_retry = 5
    page_response = None
    while True:
        try:
            page_response = requests.get(page_url)
            if page_response:
                return page_response.text
            else:
                max_retry -= 1
                sleep(1)
        except Exception as e:
            max_retry -= 1
            sleep(1)
        finally:
            if max_retry == 0:
                return page_response


def get_officer_table(page_response):
    if page_response:
        soup = BeautifulSoup(page_response, 'html.parser')
        return soup.findAll("table", {"class": "officerlist"})[0]
    return None


def get_officers_list(officer_table):
    officers = []
    for officer_data in officer_table.tbody.find_all("tr"):
        cells = officer_data.find_all("td")
        officer = [cells[1].get_text(),
                   cells[2].get_text(),
                   cells[4].get_text(),
                   cells[5].get_text()]
        officers.append(officer)
    return officers


if __name__ == "__main__":
    # page_url = "http://www.sylhet.gov.bd/site/view/dc_officers/%E0%A6%9C%E0%A7%87%E0%A6%B2%E0%A6%BE%20%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%B6%E0%A6%BE%E0%A6%B8%E0%A6%A8%E0%A7%87%E0%A6%B0%20%E0%A6%95%E0%A6%B0%E0%A7%8D%E0%A6%AE%E0%A6%95%E0%A6%B0%E0%A7%8D%E0%A6%A4%E0%A6%BE%E0%A6%AC%E0%A7%83%E0%A6%A8%E0%A7%8D%E0%A6%A6"
    page_url = "http://www.moulvibazar.gov.bd/site/view/dc_officers/%E0%A6%95%E0%A6%B0%E0%A7%8D%E0%A6%AE%E0%A6%95%E0%A6%B0%E0%A7%8D%E0%A6%A4%E0%A6%BE%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%A4%E0%A6%BE%E0%A6%B2%E0%A6%BF%E0%A6%95%E0%A6%BE"
    page_response = get_page_content(page_url)
    officer_table = get_officer_table(page_response)
    officers = get_officers_list(officer_table)
    print(json.dumps(officers, indent=4, ensure_ascii=False))
