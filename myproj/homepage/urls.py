from django.urls import path, re_path, register_converter
from . import views
from django.views.generic import TemplateView

app_name = 'homepage'


class YearConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value):
    	value = int(value)
    	if value < 2000:
    		raise ValueError
    	return int(value)

    def to_url(self, value):
    	return '%04d' % value

register_converter(YearConverter, 'year')

urlpatterns = [
    # path('', views.index_page, name='index'),
    path('', views.IndexPageView.as_view(), name='index'),
    # path('articles/', views.atricles, name='articles'),
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    # re_path(r'articles/(?P<year>[0-9]{4})/$',
    #         views.atricles_year, name='articles'),
    path('articles/<year:year>/',  views.atricles_year, name='articles_year')
]
