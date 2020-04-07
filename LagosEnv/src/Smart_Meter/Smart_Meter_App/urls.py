from django.urls import path
from Smart_Meter_App.views import index
# from Stakeholder_Dashboard.views import stakeholder
from Administrative_Dashboard.views import admin_page, about

from administrator.views import register, login, logout, dashboard, administrator_index

from Subscriber_Dashboard.views import subscriber_page


urlpatterns = [
    path('', administrator_index, name='adminIndex'),
    path('subscriber/', subscriber_page, name='subscriber'),
    # path('administrator/', administrator_index, name='adminIndex'),
    path('administrator/about', about, name='admin about'),
    path('administrator/login', login, name='login'),
    path('administrator/logout', logout, name='logout'),
    path('administrator/dashboard', dashboard, name='dashboard'),
    path('administrator/register', register, name='register'),
    path('subscriber/', subscriber_page, name='subscriber'),
]
