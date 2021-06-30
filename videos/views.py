from django.shortcuts import get_object_or_404, render
from .models import Video

# Create your views here.

def videopage(request,video_id) :

    videos = get_object_or_404(Video,pk=video_id)
    listings = Video.objects.order_by('-video_date').filter(is_published=True)[:6] 

    context = {
        "videos" :videos ,
        'listings':listings
    }

    return render(request,'video-page.html',context)