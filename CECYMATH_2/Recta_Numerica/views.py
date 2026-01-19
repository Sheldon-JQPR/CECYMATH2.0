from django.shortcuts import render


def addon_recta(request):
    """
    Vista para generar una recta numérica interactiva.
    Muestra números desde un inicio hasta un fin especificado.
    """
    numeros = []
    error = None
    
    if request.method == "POST":
        try:
            inicio_str = request.POST.get("inicio", "").strip()
            fin_str = request.POST.get("fin", "").strip()
            
            if not inicio_str or not fin_str:
                error = "Por favor, completa ambos valores."
            else:
                inicio = int(inicio_str)
                fin = int(fin_str)
                
                if inicio >= fin:
                    error = "El valor inicial debe ser menor que el valor final."
                elif (fin - inicio) > 100:
                    error = "El rango es demasiado grande. Máximo 100 números."
                else:
                    numeros = list(range(inicio, fin + 1))
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce números enteros válidos."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_recta/recta.html", {
        "numeros": numeros,
        "error": error
    })
