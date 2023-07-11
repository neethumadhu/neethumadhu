from django.http import HttpResponse
# Create your views here.
def demo(request):
    return  HttpResponse("HELLO WORLD")