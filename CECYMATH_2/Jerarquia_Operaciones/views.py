from django.shortcuts import render


def addon_jerarquia(request):
    """
    Vista para evaluar expresiones matemáticas respetando la jerarquía de operaciones.
    Utiliza PEMDAS (Paréntesis, Exponentes, Multiplicación/División, Adición/Sustracción)
    """
    resultado = None
    error = None
    expresion = None
    
    if request.method == "POST":
        try:
            expresion = request.POST.get("expresion", "").strip()
            
            if not expresion:
                error = "Por favor, ingresa una expresión matemática."
            else:
                # Caracteres permitidos en la expresión
                caracteres_permitidos = set("0123456789+-*/.() ")
                
                if not all(c in caracteres_permitidos for c in expresion):
                    error = "La expresión contiene caracteres no permitidos. Usa: +, -, *, /, **, (), números y espacios."
                else:
                    # Evaluar la expresión con seguridad limitada
                    try:
                        resultado = eval(expresion)
                        # Limitar el resultado a 10 decimales
                        if isinstance(resultado, float):
                            resultado = round(resultado, 10)
                    except ZeroDivisionError:
                        error = "⚠️ ERROR: División entre cero detectada en la expresión."
                    except SyntaxError:
                        error = "La expresión tiene un error de sintaxis. Verifica la estructura."
                    except NameError:
                        error = "La expresión contiene variables no definidas."
                    
        except Exception as e:
            error = f"Error al procesar: {str(e)}"

    return render(request, "addon_jerarquia/jerarquia.html", {
        "resultado": resultado,
        "error": error,
        "expresion": expresion
    })
