import django.http.response


class RemoveCORS:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def process_response(self, request, response: django.http.HttpResponse):
        print('cors remove')
        del response.headers['Allow']
        del response.headers['Cross-Origin-Opener-Policy']
        del response.headers['Referrer-Policy']
        del response.headers['Access-Control-Allow-Headers']
        print(response.headers)
        return response
