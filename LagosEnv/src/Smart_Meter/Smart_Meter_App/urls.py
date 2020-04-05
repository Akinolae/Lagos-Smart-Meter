from django.urls import path
from Smart_Meter_App import views
from Stakeholder_Dashboard.views import stakeholder
from administrator.views import register, login, logout, dashboard
from Subscriber_Dashboard.views import subscriber_page


urlpatterns = [
    path('', views.index, name='index'),
    path('stakeholder_Dashboard/', stakeholder, name='stakeholder'),
    path('administrator/', login, name='login'),
    path('administrator/', logout, name='logout'),
    path('administrator/', dashboard, name='dashboard'),
    path('administrator/', register, name='register'),
    path('subscriber/', subscriber_page, name='subscriber'),

]
