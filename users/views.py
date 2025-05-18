from django.http import HttpResponse

def middleware_test(request):
    raise Exception("test") 