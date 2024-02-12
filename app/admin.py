from django.contrib import admin
from .models import Article, Home, Next, About, Authors, Tag, ServiceNext, Service, Blog


# Register your models here.

@admin.register(Authors)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'authors_name', 'profession', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'authors_name')
    search_fields = ['title', 'authors_name']


admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Home)
admin.site.register(Next)
admin.site.register(Service)
admin.site.register(ServiceNext)
admin.site.register(Blog)
