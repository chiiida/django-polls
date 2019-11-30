import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import List

def get_links(url: str) -> List[str]:
    """Find all links on page at the given url.
        Return a list of all link addresses, as strings.
    """
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    browser.get(url)
    tags_element = browser.find_elements_by_tag_name('a')
    links = [link.get_attribute('href')
            for link in tags_element if link.get_attribute('href') != None]
    browser.close()
    return links


def invalid_urls(urllist: List[str]) -> List[str]:
    """Find all invalid links on page at the given url.
        Return a list of all invalid  link addresses, as strings.
    """
    invalid_links = []
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    for link in urllist:
        res = requests.head(link)
        if res.status_code == 404 or res.status_code == 500:
            invalid_links.append(link)
    return invalid_links


def main():
    links = get_links('https://cpske.github.io/ISP/')
    invalid_links = invalid_urls(links)
    print('All valid link addresses on https://cpske.github.io/ISP/ page:')
    [print(link) for link in links]
    print('\nAll invalid link addresses on https://cpske.github.io/ISP/ page:')
    [print(link) for link in invalid_links]


if __name__ == "__main__":
    main()
