import django.http.response

ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"

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
        # print(response.headers)
        del response.headers['Allow']
        del response.headers['Cross-Origin-Opener-Policy']
        del response.headers['Referrer-Policy']
        del response.headers['Access-Control-Allow-Headers']
        # print(response.headers)
        del response[ACCESS_CONTROL_ALLOW_ORIGIN]
        del response[ACCESS_CONTROL_EXPOSE_HEADERS]
        del response[ACCESS_CONTROL_ALLOW_CREDENTIALS]
        del response[ACCESS_CONTROL_ALLOW_HEADERS]
        del response[ACCESS_CONTROL_ALLOW_METHODS]
        del response[ACCESS_CONTROL_MAX_AGE]
        return response
