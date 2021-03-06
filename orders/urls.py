from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    # /orders/
    url(r'^$', views.sauce, name='sauce'),
    url(r'^sauce/$', views.SauceView.as_view(), name = 'sauce'),
    url(r'^pasta/$', views.PastaView.as_view(), name = 'pasta'),
    url(r'^ingredients/$', views.ingredients, name = 'ingredients'),
    url(r'^addingredients/$', views.add_ingredients, name = 'addingredients'),
    url(r'^overview/$', views.overview , name='overview'),
    url(r'^order/$', views.order , name = 'order'),
    # ^-begginning $ - end of regular expression
    #url(r'^(?P<sauce_id>[0-9]+)$',  views.pasta, name='pasta'),
]