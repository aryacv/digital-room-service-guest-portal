from django.contrib import admin
from django.urls import path
from kiosk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.check_in, name='check_in'),
    path('menu/', views.menu, name='menu'),
    path('request/<int:item_id>/', views.request_item, name='request_item'),
    path('ledger/', views.room_ledger, name='room_ledger'),
    path('checkout/', views.check_out, name='check_out'),
]