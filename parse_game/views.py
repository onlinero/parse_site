from django.shortcuts import render
from .tools import main
from datetime import datetime
from .models import ParseData
import json


def index(request):
    return render(request, template_name='parse_game/index.html')


def parse_site(request):
    url = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/'
    content = main(url)

    result = []
    result.append({
        'published': datetime.now(),
        'content': content
    })
    return render(request, template_name='parse_game/index.html', context={'data_db': result})


def upload_db(request):

    try:
        url = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/'
        content = main(url)
        p = ParseData(content=json.dumps(content))
        p.save()
    except Exception as e:
        return render(request, template_name='parse_game/index.html', context={'message': 'Error {}'.format(e)})

    result = []
    result.append({
        'published': datetime.now(),
        'content': content
    })
    return render(request, template_name='parse_game/index.html', context={'data_db': result,
                                                                           'message': 'Upload successfully!'})


def download_from_db(request):
    items = ParseData.objects.all()
    result = []
    for item in items:
        result.append({
            'published': item.published,
            'content': json.loads(item.content)
        })
    return render(request, template_name='parse_game/index.html', context={'data_db': result})
