from django.contrib import admin
from .models import Art

# Register your models here.

class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'medium',
        'type',
        'price',
        'image',

    )

    ordering = ('title',)

admin.site.register(Art, ArtAdmin)