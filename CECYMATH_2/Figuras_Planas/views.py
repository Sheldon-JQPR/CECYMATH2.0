from django.shortcuts import render
import math


def addon_figuras(request):
    """
    Vista para calcular área y perímetro de figuras geométricas planas.
    Soporta: círculo, cuadrado, rectángulo y triángulo.
    """
    area = None
    perimetro = None
    error = None
    figura = None
    
    if request.method == "POST":
        try:
            figura = request.POST.get("figura", "").strip()
            
            if not figura:
                error = "Por favor, selecciona una figura."
            elif figura == "circulo":
                radio_str = request.POST.get("radio", "").strip()
                if not radio_str:
                    error = "Por favor, ingresa el radio."
                else:
                    radio = float(radio_str)
                    if radio <= 0:
                        error = "El radio debe ser mayor que cero."
                    else:
                        area = round(math.pi * (radio ** 2), 4)
                        perimetro = round(2 * math.pi * radio, 4)
                    
            elif figura == "rectangulo":
                base_str = request.POST.get("base", "").strip()
                altura_str = request.POST.get("altura", "").strip()
                if not base_str or not altura_str:
                    error = "Por favor, completa base y altura."
                else:
                    base = float(base_str)
                    altura = float(altura_str)
                    if base <= 0 or altura <= 0:
                        error = "La base y altura deben ser mayores que cero."
                    else:
                        area = round(base * altura, 4)
                        perimetro = round(2 * (base + altura), 4)
                    
            elif figura == "triangulo":
                base_str = request.POST.get("base", "").strip()
                altura_str = request.POST.get("altura", "").strip()
                lado1_str = request.POST.get("lado1", "").strip()
                lado2_str = request.POST.get("lado2", "").strip()
                lado3_str = request.POST.get("lado3", "").strip()
                
                if not all([base_str, altura_str, lado1_str, lado2_str, lado3_str]):
                    error = "Por favor, completa todos los campos del triángulo."
                else:
                    base = float(base_str)
                    altura = float(altura_str)
                    lado1 = float(lado1_str)
                    lado2 = float(lado2_str)
                    lado3 = float(lado3_str)
                    
                    if any(v <= 0 for v in [base, altura, lado1, lado2, lado3]):
                        error = "Todos los valores deben ser mayores que cero."
                    else:
                        area = round((base * altura) / 2, 4)
                        perimetro = round(lado1 + lado2 + lado3, 4)
                    
            elif figura == "cuadrado":
                lado_str = request.POST.get("lado", "").strip()
                if not lado_str:
                    error = "Por favor, ingresa el lado."
                else:
                    lado = float(lado_str)
                    if lado <= 0:
                        error = "El lado debe ser mayor que cero."
                    else:
                        area = round(lado ** 2, 4)
                        perimetro = round(4 * lado, 4)
            else:
                error = "Figura no reconocida."
                    
        except ValueError:
            error = "Entrada inválida. Por favor, introduce números válidos."
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render(request, "addon_figuras/figuras.html", {
        "area": area,
        "perimetro": perimetro,
        "error": error,
        "figura": figura
    })
