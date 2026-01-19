from django.shortcuts import render


def addon_polinomios(request):
    """
    Vista para evaluar polinomios.
    Evalúa polinomios de la forma: ax² + bx + c
    """
    resultado = None
    error = None
    
    if request.method == "POST":
        try:
            a_str = request.POST.get("a", "").strip()
            b_str = request.POST.get("b", "").strip()
            c_str = request.POST.get("c", "").strip()
            x_str = request.POST.get("x", "").strip()
            
            if not a_str or not b_str or not c_str or not x_str:
                error = "Por favor, completa todos los campos."
            else:
                a = float(a_str)
                b = float(b_str)
                c = float(c_str)
                x = float(x_str)
                
                resultado = a * (x ** 2) + b * x + c
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce números válidos."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_polinomios/polinomios.html", {"resultado": resultado, "error": error})
