class AuditoriaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        usuario = request.user.username if request.user.is_authenticated else 'anonimo'
        print(f'[AUDIT] {request.method} {request.path} usuario={usuario} status={response.status_code}')
        response['X-Auditoria'] = 'activa'
        return response