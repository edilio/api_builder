import requests

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

ABERRANT_PLURAL_MAP = {
    'appendix': 'appendices',
    'barracks': 'barracks',
    'cactus': 'cacti',
    'child': 'children',
    'criterion': 'criteria',
    'deer': 'deer',
    'echo': 'echoes',
    'elf': 'elves',
    'embargo': 'embargoes',
    'focus': 'foci',
    'fungus': 'fungi',
    'goose': 'geese',
    'hero': 'heroes',
    'hoof': 'hooves',
    'index': 'indices',
    'knife': 'knives',
    'leaf': 'leaves',
    'life': 'lives',
    'man': 'men',
    'mouse': 'mice',
    'nucleus': 'nuclei',
    'person': 'people',
    'phenomenon': 'phenomena',
    'potato': 'potatoes',
    'self': 'selves',
    'syllabus': 'syllabi',
    'tomato': 'tomatoes',
    'torpedo': 'torpedoes',
    'veto': 'vetoes',
    'woman': 'women',
    }

VOWELS = set('aeiou')


def pluralize(singular):
    """Return plural form of given lowercase singular word (English only). Based on
    ActiveState recipe http://code.activestate.com/recipes/413172/

    >>> pluralize('')
    ''
    >>> pluralize('goose')
    'geese'
    >>> pluralize('dolly')
    'dollies'
    >>> pluralize('genius')
    'genii'
    >>> pluralize('jones')
    'joneses'
    >>> pluralize('pass')
    'passes'
    >>> pluralize('zero')
    'zeros'
    >>> pluralize('casino')
    'casinos'
    >>> pluralize('hero')
    'heroes'
    >>> pluralize('church')
    'churches'
    >>> pluralize('x')
    'xs'
    >>> pluralize('car')
    'cars'

    """
    if not singular:
        return ''
    plural = ABERRANT_PLURAL_MAP.get(singular)
    if plural:
        return plural
    root = singular
    try:
        if singular[-1] == 'y' and singular[-2] not in VOWELS:
            root = singular[:-1]
            suffix = 'ies'
        elif singular[-1] == 's':
            if singular[-2] in VOWELS:
                if singular[-3:] == 'ius':
                    root = singular[:-2]
                    suffix = 'i'
                else:
                    root = singular[:-1]
                    suffix = 'ses'
            else:
                suffix = 'es'
        elif singular[-2:] in ('ch', 'sh'):
            suffix = 'es'
        else:
            suffix = 's'
    except IndexError:
        suffix = 's'
    plural = root + suffix
    return plural


def get_rest_snippets(model_name):
    tpl_serializer = """
    from . import models

    class LanguageSerializer(serializers.ModelSerializer):
    &nbsp;&nbsp;&nbsp;&nbsp;class Meta:
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model = models.Language
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fields = '__all__'
    """
    serializer = tpl_serializer.replace('Language', model_name).replace('\t', '&nbsp;')

    tpl_view = """
    from rest_framework import serializers
    from django_filters.rest_framework import DjangoFilterBackend
    from . import models
    
    class LanguageViewSet(viewsets.ModelViewSet):
    &nbsp;&nbsp;&nbsp;&nbsp;model = models.Language
    &nbsp;&nbsp;&nbsp;&nbsp;serializer_class = serializers.LanguageSerializer
    &nbsp;&nbsp;&nbsp;&nbsp;queryset = models.Language.objects.all()
    &nbsp;&nbsp;&nbsp;&nbsp;filter_backends = (DjangoFilterBackend, )
    &nbsp;&nbsp;&nbsp;&nbsp;filter_fields = ('example_field', )
"""

    view_set = tpl_view.replace('Language', model_name)

    tpl_urls = """
    from rest_framework import routers
    
    router.register(r'languages', views.LanguageViewSet)
    
    urlpatterns = []  # add more paths

    urlpatterns += router.urls
    """
    url = pluralize(model_name.lower())
    new_urls = tpl_urls.replace('languages', url).replace('Language', model_name)

    return serializer, view_set, new_urls


def create_api(request):
    model_name, serializer, view_set, url = "Sample", "", "", ""
    if request.method == 'POST':
        model_name = request.POST.get('model_name') or model_name
        serializer, view_set, url = get_rest_snippets(model_name)
    c = {'model_name': model_name, 'serializer': serializer, 'view_set': view_set, 'url': url}
    return render(request, context=c, template_name='index.html')


def proxy(request):
    qry = request.GET.get('query')
    data = request.GET.copy()
    del data['query']
    r = requests.get(qry, params=data)
    ret = HttpResponse(content=r.content, status=r.status_code)
    # ret['access_control_allow_origin'] = '*'
    # ret["access-control-allow-methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return ret


