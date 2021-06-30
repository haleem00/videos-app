from django.shortcuts import render,get_object_or_404
from videos.models import Video,Cat
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

# Create your views here.


def index(request) :



    category = request.GET.get('category')
    if category == None :
        videos = Video.objects.order_by('-video_date').filter(is_published=True)
    else :
        videos = Video.objects.order_by('-video_date').filter(cat__name=category)

    
    paginator = Paginator(videos, 6)
    page = request.GET.get("page")
    paged_videos = paginator.get_page(page)


    
    
    categories = Cat.objects.all()
    


    context = {
        'videos' :paged_videos,
        'categories':categories,

    }

    return render(request,"index.html",context)

def about(request):

    return render(request,'about.html')

