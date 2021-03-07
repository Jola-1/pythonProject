from django.contrib import admin
from django.urls import path
from .views import polls_list, polls_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', polls_list, name = 'polls_list'),
    path('polls/<int:pk>', polls_detail, name = 'polls_detail')
]