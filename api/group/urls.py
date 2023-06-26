from django.urls import path
from .views import group_list_view, group_detail_view


urlpatterns=[
    path('groups/',group_list_view),
    path('groups/<int:group_id>/',group_detail_view),
]