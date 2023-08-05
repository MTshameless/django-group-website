from django.contrib import admin
from .models import Instruments, category, ResearchArea, ResearchDetails, RepresentativePublications, Publications, Members, Positions, News

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(category)
admin.site.register(ResearchArea)
admin.site.register(ResearchDetails)
admin.site.register(RepresentativePublications)
admin.site.register(Publications)
admin.site.register(Members)
admin.site.register(Positions)
admin.site.register(Instruments)
admin.site.register(News, NewsAdmin)