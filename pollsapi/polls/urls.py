from django.contrib import admin
from django.urls import path
from .apiviews import PollList, PollDetail 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', PollList.as_view(), name = 'polls_list'),
    path('polls/<int:pk>', PollDetail.as_view(), name = 'polls_detail')
]