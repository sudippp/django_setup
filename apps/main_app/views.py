from django.shortcuts import render, HttpResponse
from django.views import View

from django.conf import settings
# Create your views here.

class Index(View):

    def get(self, request, *args, **kwargs):
        settings.LOGGER.info("Index GET Start")
        settings.LOGGER.info("Index GET End")
        return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        settings.LOGGER.info("Index POST Start")
        settings.LOGGER.info("Index POST End")
        return render(request, 'index.html')
    
    
def index(request):
    settings.LOGGER.info("index Start")
    settings.LOGGER.info("index End")
    return HttpResponse("Index!!")