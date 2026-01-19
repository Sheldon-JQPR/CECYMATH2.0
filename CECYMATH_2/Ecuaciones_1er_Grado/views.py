from django.shortcuts import render


def addon_ecuaciones(request):
    """
    Vista para resolver ecuaciones de primer grado.
    Resuelve ecuaciones de la forma: ax + b = c
    """
    resultado = None
    error = None
    
    if request.method == "POST":
        try:
            a_str = request.POST.get("a", "").strip()
            b_str = request.POST.get("b", "").strip()
            c_str = request.POST.get("c", "").strip()
            
            if not a_str or not b_str or not c_str:
                error = "Por favor, completa todos los campos."
            else:
                a = float(a_str)
                b = float(b_str)
                c = float(c_str)
                
                if a == 0:
                    error = "⚠️ ERROR: El coeficiente 'a' no puede ser cero. La ecuación no sería de primer grado."
                else:
                    resultado = (c - b) / a
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce números válidos."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_ecuaciones/ecuaciones.html", {"resultado": resultado, "error": error})
