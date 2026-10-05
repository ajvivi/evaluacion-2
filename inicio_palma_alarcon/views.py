from django.shortcuts import render


TEMAS = [
    {
        "nombre": "Naturaleza",
        "descripcion": (
            "Conoce paisajes naturales, bosques y montañas. "
            "Descubre la importancia de cuidar nuestro entorno."
        ),
        "ruta": "inicio:tema1",
        "portada": "images/naturaleza1.jpg",
        "destacado": True,
        "imagenes": [
            {
                "archivo": "images/naturaleza1.jpg",
                "descripcion": "Paisaje natural con árboles",
            },
            {
                "archivo": "images/naturaleza2.jpg",
                "descripcion": "Paisaje de montañas",
            },
        ],
    },
    {
        "nombre": "Tecnología",
        "descripcion": (
            "Explora herramientas digitales y dispositivos "
            "que forman parte de nuestra vida cotidiana."
        ),
        "ruta": "inicio:tema2",
        "portada": "images/tecnologia1.jpg",
        "destacado": False,
        "imagenes": [
            {
                "archivo": "images/tecnologia1.jpg",
                "descripcion": "Computador y herramientas digitales",
            },
            {
                "archivo": "images/tecnologia2.jpg",
                "descripcion": "Dispositivos tecnológicos",
            },
        ],
    },
]


def inicio(request):
    return render(request, "inicio.html", {"temas": TEMAS})


def tema1(request):
    return render(request, "tema1.html", {"tema": TEMAS[0]})


def tema2(request):
    return render(request, "tema2.html", {"tema": TEMAS[1]})