from django.http import Http404


# lo que dice esto que se si quieres acceder a una vista
# te va a lanzar un error 404 si no pones dentro de la ruta
# /?secret y lo igualas a lo que quieras recibir
# ejm : localhost:8000/?secret=platzi y funcionara
class SecretMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #antes de la vista  
        if not request.GET.get('secret'):
            raise Http404()
        if request.GET.get('secret') != 'platzi':
            raise Http404()

        # punto intermedio
        response = self.get_response(request)
        # punto intermedio

        # despues de la vista
        return response


