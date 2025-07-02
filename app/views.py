from django.http import HttpResponse


def home(request):
    return HttpResponse("New Project! With a new request!")

