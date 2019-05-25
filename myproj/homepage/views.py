from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from datetime import datetime, timedelta
from random import randint
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request):
        return render(request, self.template_name)


class ArticlesView(TemplateView):
    template_name = 'homepage/articles.html'

    def get_context_data(self, **kwargs):
        my_obj = MyClass()
        my_obj.data = {'spam': 'eggs'}
        my_obj.list = list(range(5, 10))
        art_list = list(range(1, 8))
        args = {
            'articles': art_list,
            'val1': "111",
            'val2': "222",
            'str_for_center': 'hello',
            'str_title': 'string for title filter',
            'f1': '',
            'f2': 0,
            'f3': 'Hi',
            'obj': my_obj,
            'string': ('first line\n'
                       'second line\n'
                       'last line'
                       ),
            'current': datetime.today,
            'dates': get_dates_list(),
            'items': [i for i in range(1, 5)],
            'int_val': 7,
            'str_val': "seven"

        }

        context = super().get_context_data(**kwargs)
        print(context)
        context.update(args)
        return context  

    # def get(self, request):
    #     my_obj = MyClass()
    #     my_obj.data = {'spam': 'eggs'}
    #     my_obj.list = list(range(5, 10))
    #     art_list = list(range(1, 8))
    #     args = {
    #         'articles': art_list,
    #         'val1': "111",
    #         'val2': "222",
    #         'str_for_center': 'hello',
    #         'str_title': 'string for title filter',
    #         'f1': '',
    #         'f2': 0,
    #         'f3': 'Hi',
    #         'obj': my_obj,
    #         'string': ('first line\n'
    #                    'second line\n'
    #                    'last line'
    #                    ),
    #         'current': datetime.today,
    #         'dates': get_dates_list(),
    #         'items': [i for i in range(1, 5)]

    #     }
    #     return render(request, 'homepage/articles.html', args)


def get_dates_list(count=30):
    result = []
    today = datetime.today()
    result.append(today)
    for i in range(count):
        date = today - timedelta(days=i)
        for j in range(randint(1, 4)):
            result.append(date.replace(hour=randint(0, 23)))
    return result


@require_http_methods(['GET', 'POST'])
def index_page(request):
    if request.method == "GET":
        response = render(request, 'homepage/index.html')
        response['MyCustomHeader'] = 'spam eggs'
    else:
        pass
    return response


@require_GET
def atricles(request):
    my_obj = MyClass()
    my_obj.data = {'spam': 'eggs'}
    my_obj.list = list(range(5, 10))
    art_list = list(range(1, 8))
    args = {
        'articles': art_list,
        'val1': "111",
        'val2': "222",
        'str_for_center': 'hello',
        'str_title': 'string for title filter',
        'f1': '',
        'f2': 0,
        'f3': 'Hi',
        'obj': my_obj,
        'string': ('first line\n'
                   'second line\n'
                   'last line'
                   ),
        'current': datetime.today,
        'dates': get_dates_list(),
        'items': [i for i in range(1, 5)]

    }
    return render(request, 'homepage/articles.html', args)


class MyClass(object):
    foo = 42

    def __repr__(self):
        return f'<MyClass foo = {self.foo}>'


def atricles_year(request, year):
    return HttpResponse(f'<h1>Year {year}</h1>')
