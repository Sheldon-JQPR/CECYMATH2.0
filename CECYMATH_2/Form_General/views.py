from django.shortcuts import render
import math


def form_general(request):
    """
    Vista del módulo de Fórmula General (Ecuaciones Cuadráticas).
    Resuelve ecuaciones de la forma ax² + bx + c = 0
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
                    error = "❌ ERROR: El coeficiente 'a' no puede ser cero. No es una ecuación cuadrática."
                else:
                    discriminante = (b ** 2) - (4 * a * c)
                    
                    if discriminante > 0:
                        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                        resultado = {
                            'a': a,
                            'b': b,
                            'c': c,
                            'discriminante': discriminante,
                            'x1': x1,
                            'x2': x2
                        }
                    elif discriminante == 0:
                        x1 = -b / (2 * a)
                        resultado = {
                            'a': a,
                            'b': b,
                            'c': c,
                            'discriminante': discriminante,
                            'x1': x1
                        }
                    else:
                        resultado = {
                            'a': a,
                            'b': b,
                            'c': c,
                            'discriminante': discriminante
                        }
                        
        except ValueError:
            error = "❌ Entrada inválida. Por favor, introduce números válidos."
        except Exception as e:
            error = f"❌ Error inesperado: {str(e)}"
    
    return render(request, "addon_form/formula_general.html", {"resultado": resultado, "error": error})

