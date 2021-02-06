from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import pytube as p



# Create your views here.
def index(request):
    return render(request, "index.html")

def download(request):
    if request.method == "POST":
        youtube = p.YouTube(request.POST['video_link'])
        youtube = youtube.streams.get_highest_resolution()

        youtube.download()
    return render(request, "index.html")

def send_file(response, link):
    file = open(link, "rb")

    response = FileResponse(file)

    return response
