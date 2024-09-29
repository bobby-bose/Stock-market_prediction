
from django.contrib import admin
from django.urls import path

from stcok_market_prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('chat-board/',views.chat_board,name='chat-board'),
    path('analytical-part/',views.analytical_part,name='analytical-part'),
]
