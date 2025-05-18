import time
import logging
from django.http import HttpResponse

class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"Запрос на {request.path} занял {duration:.2f} секунд.")
        return response
    

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Привет, промежуточное ПО!'
        return response
    


class CustomErrorMiddleware(HttpResponse):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, exception):
        logging.getLogger(__name__).error(f"Произошло исключение: {exception}")
        return logging.getLogger(__name__).error(f"Произошло исключение: {exception}")