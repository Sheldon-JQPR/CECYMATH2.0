from django.shortcuts import render


def addon_factorizacion(request):
    """
    Vista para encontrar factores de números.
    Encuentra todos los divisores de un número entero positivo.
    """
    factores = None
    error = None
    
    if request.method == "POST":
        try:
            numero_str = request.POST.get("numero", "").strip()
            
            if not numero_str:
                error = "Por favor, ingresa un número."
            else:
                numero = int(numero_str)
                
                if numero <= 0:
                    error = "Por favor, ingresa un número positivo mayor que cero."
                else:
                    # Encontrar todos los factores
                    factores_lista = []
                    for i in range(1, numero + 1):
                        if numero % i == 0:
                            factores_lista.append(i)
                    factores = factores_lista
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce un número entero válido."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_factorizacion/factorizacion.html", {"factores": factores, "error": error})
