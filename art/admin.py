from django.contrib import admin
from .models import Art


class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'medium',
        'product_type',
        'price',
        'image',
    )

    ordering = ('title',)


admin.site.register(Art, ArtAdmin)
