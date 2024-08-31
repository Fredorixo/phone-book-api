from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", get_users),
    path("name/", search_user_by_name),
    path("phone_number/", search_user_by_phone_number),
]