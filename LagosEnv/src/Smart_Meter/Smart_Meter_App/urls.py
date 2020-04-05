from django.urls import path
from Smart_Meter_App.views import index
from Stakeholder_Dashboard.views import stakeholder
from Administrative_Dashboard.views import admin_page, about
from Subscriber_Dashboard.views import subscriber_page

urlpatterns = [
    path('', index, name='index'),
    path('stakeholder_Dashboard/', stakeholder, name='stakeholder'),
    path('admin_Dashboard/', admin_page, name='administrator'),
    path('subscriber/', subscriber_page, name='subscriber'),
    path('admin_Dashboard/about', about, name='admin about')
]
