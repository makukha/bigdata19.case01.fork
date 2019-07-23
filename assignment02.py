"""
Assignment 02
=============

The goal of this assignment is to implement synchronous scraping using standard python modules,
and compare the scraping speed to asynchronous mode.

Run this code with

    > fab run assignment02.py
"""
from tqdm import tqdm
from urllib.request import Request, urlopen

from yahoo import read_symbols, YAHOO_HTMLS


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    }


def scrape_descriptions_sync():
    """Scrape companies descriptions synchronously."""

    YAHOO_HTMLS.mkdir(parents=True, exist_ok=True)

    for symbol in tqdm(read_symbols()):
        with urlopen(Request(f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}', headers=HEADERS)) as response:
            with (YAHOO_HTMLS / f'{symbol}.html').open('wb') as f:
                f.write(response.read())


def main():
    scrape_descriptions_sync()


if __name__ == '__main__':
    main()
