from django.urls import path
from Smart_Meter_App.views import index
# from Stakeholder_Dashboard.views import stakeholder
from Administrative_Dashboard.views import admin_page, about

from administrator.views import register, login, logout, dashboard

from Subscriber_Dashboard.views import subscriber_page


urlpatterns = [
    path('', index, name='index'),
    # path('stakeholder_Dashboard/', stakeholder, name='stakeholder'),
    # path('admin_Dashboard/', admin_page, name='administrator'),
    path('subscriber/', subscriber_page, name='subscriber'),
    path('administrator/about', about, name='admin about'),
    path('administrator/login', login, name='login'),
    path('administrator/logout', logout, name='logout'),
    path('administrator/dashboard', dashboard, name='dashboard'),
    path('administrator/register', register, name='register'),
    path('subscriber/', subscriber_page, name='subscriber'),
]
