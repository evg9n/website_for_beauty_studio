from django.shortcuts import render
from django.views import View
from .models import BaseModel, MainModel, WorksModel, NewsStocksModel, \
    ContactsModel, PositionsPricesModel, HeaderPricesModel, TagPricesModels


def get_base():
    dict_base = {
        'menu': [],
        'logo': {'text': '', 'link': ''},
        'right': '',
        'links': [],
        'button': {},
        'head': [],
    }

    base = BaseModel.objects.filter(flag_active=True)
    for element in base:
        if element.choices_field == 'меню':
            link = element.link
            text = element.text
            dict_base['menu'].append(dict(text=text, link=link))

        elif element.choices_field == 'логотип':
            link = element.link
            text = element.text
            dict_base['logo'] = dict(text=text, link=link)

        elif element.choices_field == 'права':
            text = element.text
            dict_base['right'] = text

        elif element.choices_field == 'ссылки':
            link = element.link
            text = element.text
            dict_base['links'].append(dict(text=text, link=link))
        elif element.choices_field == 'все кнопки записи':
            link = element.link
            text = element.text
            dict_base['button'] = dict(text=text, link=link)

    return dict_base


class MainView(View):

    @classmethod
    def __get_main(cls):
        dict_main = dict(
            header=dict(header='', text='', photo=''),
            advantages=list(),
            masters=list(),
            certificates=list(),
            question_answer=list(),
            head=list(),
        )

        main = MainModel.objects.filter(flag_active=True)

        for element in main:

            if element.choices_field == 'заголовок':
                header = element.header
                text = element.text
                photo = element.photo
                dict_main['header'] = dict(header=header, text=text, photo=photo)

            elif element.choices_field == 'преимущество':
                header = element.header
                text = element.text
                photo = element.photo
                countable = True if len(dict_main['advantages']) % 2 == 0 else False
                dict_main['advantages'].append(dict(header=header, text=text, photo=photo, countable=countable))

            elif element.choices_field == 'мастера':
                header = element.header
                text = element.text
                photo = element.photo
                dict_main['masters'].append(dict(header=header, text=text, photo=photo))

            elif element.choices_field == 'сертификаты':
                photo = element.photo
                number = len(dict_main['certificates']) + 1
                dict_main['certificates'].append(dict(number=number, photo=photo))

            elif element.choices_field == 'вопрос/ответ':
                header = element.header
                text = element.text
                dict_main['question_answer'].append(dict(header=header, text=text))

            elif element.choices_field == 'head':
                text = element.text
                dict_main['head'].append(text)

        return dict_main

    def get(self, request):
        context = get_base()
        dict_main = self.__get_main()

        context['header'] = dict_main.get('header')
        context['advantages'] = dict_main.get('advantages')
        context['masters'] = dict_main.get('masters')
        context['certificates'] = dict_main.get('certificates')
        context['count_certificates'] = len(dict_main.get('certificates'))
        context['question_answer'] = dict_main.get('question_answer')
        context['head'] = dict_main.get('head')

        return render(request, 'main/main.html', context=context)


class WorksView(View):

    @classmethod
    def get_date(cls):
        result = dict(photos=list(), head=list())

        for elem in WorksModel.objects.filter(flag_active=True):
            if elem.choices_field == 'работа':
                result['photos'].append(elem)
            elif elem.choices_field == 'head':
                result['head'].append(elem.text)

        return result

    def get(self, request):
        context = get_base()
        data_work = self.get_date()
        context['photos'] = data_work['photos']
        context['head'] = data_work['head']

        return render(request, 'main/works.html', context=context)


class NewsStocksView(View):

    @classmethod
    def get_date(cls):
        result = dict(news_and_stocks=list(), head=list())

        for elem in NewsStocksModel.objects.filter(flag_active=True):
            if elem.choices_field == 'новость и акция':
                result['news_and_stocks'].append(elem)
            elif elem.choices_field == 'head':
                result['head'].append(elem.text)

        return result

    def get(self, request):
        context = get_base()
        data = self.get_date()
        context['news_and_stocks'] = data['news_and_stocks']
        context['head'] = data['head']

        return render(request, 'main/stock.html', context=context)


class PricesView(View):

    @classmethod
    def get_prices(cls):
        list_positions = PositionsPricesModel.objects.prefetch_related()
        data = list()
        for header in HeaderPricesModel.objects.select_related().filter(flag_active=True):
            positions = list()
            for position in list_positions.filter(header=header, flag_active=True):
                positions.append(position)

            data.append(dict(header=header.header, positions=positions))

        data = dict(
            headers=data[:-1],
            last_header=data[-1]
        )

        return data

    def get(self, request):
        data = self.get_prices()
        context = get_base()

        context['headers'] = data['headers']
        context['last_header'] = data['last_header']
        context['head'] = [elem.text for elem in TagPricesModels.objects.filter(flag_active=True)]

        return render(request, 'main/prices.html', context=context)


class ContactsView(View):

    @classmethod
    def __get_contacts(cls):
        data = ContactsModel.objects.filter(flag_active=True)
        result = dict(
            links_offers=list(),
            vk=dict(),
            wa=dict(),
            contacts=list(),
            descriptions=list(),
            coordinates=dict(),
            head=list()
        )
        for element in data:
            if element.choices_field == 'VK':
                result['vk'] = {'text': element.text, 'link': element.link}
            elif element.choices_field == 'WhatsApp':
                result['wa'] = {'text': element.text, 'link': element.link}
            elif element.choices_field == 'другое':
                result['links_offers'].append({'text': element.text, 'link': element.link})
            elif element.choices_field == 'контакты':
                result['contacts'].append(element.text)
            elif element.choices_field == 'описание':
                result['descriptions'].append(element.text)
            elif element.choices_field == 'координаты точки на карте':
                result['coordinates'] = {'x': element.x, 'y': element.y}
            elif element.choices_field == 'head':
                result['head'].append(element.text)

        return result

    def get(self, request):
        contacts_data = self.__get_contacts()
        context = get_base()
        context['vk'] = contacts_data['vk'] if contacts_data['vk'] else False
        context['wa'] = contacts_data['wa'] if contacts_data['wa'] else False
        context['links_offers'] = contacts_data['links_offers']
        context['contacts'] = contacts_data['contacts']
        context['descriptions'] = contacts_data['descriptions']
        context['coordinates'] = contacts_data['coordinates'] if contacts_data['coordinates'] else {'x': 55.75,
                                                                                                    'y': 37.6167}
        context['head'] = contacts_data['head']

        return render(request, 'main/contacts.html', context=context)
