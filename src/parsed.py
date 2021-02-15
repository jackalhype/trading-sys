import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def get_financials(url):
    page_source = requests.get(url)

    soup_html = bs(page_source.text, 'html.parser')
    tabelle_soup = soup_html.find('div', class_="M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)")


    # Get Title Row
    überschriften = tabelle_soup.find('div', class_="D(tbr) C($primaryColor)")
    überschriften = überschriften.findAll('span')
    title_row = list()
    for u in überschriften:
        title_row.append(u.text)

    tabelle = pd.DataFrame(None, columns=title_row)
    restliche_zeilen = tabelle_soup.findAll('div', class_="D(tbr) fi-row Bgc($hoverBgColor):h")
    for zeile in restliche_zeilen:
        spalten = zeile.findChildren('div', recursive=False)
        zeilenwerte = list()
        for spalte in spalten:
            zeilenwerte.append(spalte.text)
        tabelle.loc[len(tabelle)] = zeilenwerte
    tabelle = tabelle.set_index(title_row[0])
    return tabelle


def get_income_statement(symbol):
    url = 'https://finance.yahoo.com/quote/' + symbol + '/financials'
    return get_financials(url)


def get_balance_sheet(symbol):
    url = 'https://finance.yahoo.com/quote/' + symbol + '/balance-sheet'
    return get_financials(url)


def get_cashflow(symbol):
    url = 'https://finance.yahoo.com/quote/' + symbol + '/cash-flow'
    return get_financials(url)


if "__main__" == __name__:
    symbol = 'BA'
    # Functions return dataframe
    income_statement = get_income_statement(symbol)
    balance_sheet = get_balance_sheet(symbol)
    cash_flow = get_cashflow(symbol)

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


    # print('income_statement: ')
    # print(income_statement)
    print('balance_sheet:')
    print(balance_sheet)
    # print('cash_flow: ')
    # print(cash_flow)
    # print(type(cash_flow.))     # class 'pandas.core.frame.DataFrame'

