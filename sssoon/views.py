
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sssoon/index.html')


def video(request):
    return render(request, 'sssoon/video.html')