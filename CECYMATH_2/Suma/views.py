from django.shortcuts import render
import json


def addon_suma(request):
    """
    Vista para la calculadora de suma.
    Realiza la suma de dos números reales con validación completa.
    """
    total = None
    error = None
    
    if request.method == "POST":
        try:
            # Obtener valores del formulario
            numero1_str = request.POST.get("numero1", "").strip()
            numero2_str = request.POST.get("numero2", "").strip()
            
            # Validar que los campos no estén vacíos
            if not numero1_str or not numero2_str:
                error = "Por favor, completa todos los campos."
            else:
                # Convertir a float
                numero1 = float(numero1_str)
                numero2 = float(numero2_str)
                
                # Validar que sean números reales válidos
                if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
                    error = "Los valores deben ser números válidos."
                else:
                    # Realizar la suma
                    total = numero1 + numero2
                    
        except ValueError as ve:
            error = "Entrada inválida. Por favor, introduce números válidos (enteros o decimales)."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_suma/suma.html", {
        "total": total,
        "error": error
    })
