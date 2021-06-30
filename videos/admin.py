from django.contrib import admin
from .models import Video,Cat

# Register your models here.

class videoadmin(admin.ModelAdmin):
    list_display= ('id','title', "is_published","cat")
    list_display_links = ('id','title',"cat")
    list_editable = ('is_published',)
    search_fields = ('id','title','description')

admin.site.register(Video,videoadmin)
admin.site.register(Cat)

