from django.urls import path
from .views import form_general

urlpatterns = [
    path("addon_/formula_general", form_general, name='formula_general'),
]
