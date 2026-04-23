from django.http import HttpResponse

def website(request):
    return HttpResponse("This is the home page")