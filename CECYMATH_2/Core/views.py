from django.shortcuts import render


def core_view(request):
    """
    Vista del módulo Core de CECYMATH 2.0.
    Página principal que enlaza todos los módulos educativos.
    """
    return render(request, "addon_form/index.html")
