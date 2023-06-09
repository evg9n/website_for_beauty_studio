from django.urls import path
from .views import MainView, WorksView, NewsStocksView, PricesView, ContactsView


urlpatterns = [
    path('', MainView.as_view(), name='главная страница'),
    path('works', WorksView.as_view(), name='работы'),
    path('prices', PricesView.as_view(), name='цены'),
    path('news-and-stocks', NewsStocksView.as_view(), name='новости и акции'),
    path('contacts', ContactsView.as_view(), name='контакты'),
]
