from django.urls import path
from . import views


app_name = 'offers'

urlpatterns = [
    path('', views.offers_list, name='offers_list'),
    path('<slug:category_slug>/', views.offers_list,
         name='offers_list_by_category'),
    path('<int:id>/<slug:slug>/', views.offers_detail,
         name='offers_detail'),
]
