import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def add_format_groups(group_names, value_bets):

    group_names = [group_names[i]+'-'+group_names[i + 1] for i in range(0, len(group_names), 2)]
    value_bets = [value_bets[i:i + 2] for i in range(0, len(value_bets), 2)]

    result = []
    for j, names in enumerate(group_names):
        tmp_bets = []
        for i in range(0 + j * 10, 10 + j * 10):
            tmp_bets.append(value_bets[i])
        result.append({
            'name': names,
            'bets': tmp_bets
        })
    return result


def get_all_bets(html):

    soup = BeautifulSoup(html, 'html.parser')
    all_bets = soup.find(class_='eventLines')

    group_names = []
    value_bets = []
    for item in all_bets:
        for name in item.select('a'):
            if name.text != 'eventLink':
                group_names.append(name.text)
        for bet in item.select('b'):
            value_bets.append(bet.text)

    return add_format_groups(group_names, value_bets)


def main(url):
    all_bets = get_all_bets(get_html(url))
    return all_bets
