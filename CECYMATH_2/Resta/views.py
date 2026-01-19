from django.shortcuts import render


def addon_resta(request):
    """
    Vista para la calculadora de resta.
    Realiza la resta de dos números reales con validación completa.
    """
    total = None
    error = None
    
    if request.method == "POST":
        try:
            numero1_str = request.POST.get("numero1", "").strip()
            numero2_str = request.POST.get("numero2", "").strip()
            
            if not numero1_str or not numero2_str:
                error = "Por favor, completa todos los campos."
            else:
                numero1 = float(numero1_str)
                numero2 = float(numero2_str)
                total = numero1 - numero2
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce números válidos (enteros o decimales)."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_resta/resta.html", {"total": total, "error": error})
