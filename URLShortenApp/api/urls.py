from django.urls import path
from django.urls import path
from URLShortenApp.api.views import GetURL,CreateURL

app_name = 'URLShortenApi'

urlpatterns = [
    path('create/', CreateURL.as_view(), name='createlink-view'),
    path('<str:short>/', GetURL, name='getlink-view'),
]
