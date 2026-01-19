from django.urls import path
from .views import addon_resta

urlpatterns = [
    path("addon_/resta", addon_resta, name='addon_resta'),
]
