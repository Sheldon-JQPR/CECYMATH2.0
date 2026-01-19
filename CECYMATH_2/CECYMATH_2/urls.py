"""
URL configuration for CECYMATH_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('', include('Form_General.urls')),
    path('', include('Suma.urls')),
    path('', include('Resta.urls')),
    path('', include('Multiplicacion.urls')),
    path('', include('Divicion.urls')),
    path('', include('Ecuaciones_1er_Grado.urls')),
    path('', include('Polinomios.urls')),
    path('', include('Factorizacion.urls')),
    path('', include('Figuras_Planas.urls')),
    path('', include('Jerarquia_Operaciones.urls')),
    path('', include('Recta_Numerica.urls')),
]
