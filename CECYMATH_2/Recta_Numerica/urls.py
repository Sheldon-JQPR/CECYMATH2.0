from django.urls import path
from .views import addon_recta

urlpatterns = [
    path("addon_/recta_numerica", addon_recta, name='addon_recta'),
]
