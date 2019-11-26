from django.http import HttpResponse

# Create your views here.
from blog import testdb


def selectdb(request):
    # return HttpResponse("Hello, world!")
    return testdb.selectdb(request)


def savedb(request):
    # return HttpResponse("Hello, world!")
    return testdb.savedb(request)


def updatedb(request):
    # return HttpResponse("Hello, world!")
    return testdb.updatedb(request)


def deletedb(request):
    # return HttpResponse("Hello, world!")
    return testdb.deletedb(request)
