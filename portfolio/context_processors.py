"""
Context processors globales del portafolio.
Datos disponibles en todos los templates.
"""


def global_context(request):
    return {
        'developer': {
            'name':          'Juan Manuel Márquez Jiménez',
            'title':         'Backend Developer con Python y Django',
            'role':          'Backend Developer · Python · Django REST Framework',
            'email':         'juanmanuelmarquezjimenez9@gmail.com',
            'github':        'https://github.com/jmarquezdev20',
            'linkedin':      'https://www.linkedin.com/in/juan-manuel-marquez-jimenez-36765a2b3/',
            'location':      'Barranquilla, Colombia',
            'english_level': 'Básico (A2)',
            'available':     True,
        }
    }