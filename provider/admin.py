

# Django
from django.contrib import admin


# Models
from .models import Articles




@admin.register(Articles)
class provider(admin.ModelAdmin):
    pass



