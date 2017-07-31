from django.contrib import admin
from .models import Post
from .models import About
from .models import Category
admin.site.register(Post)


class AboutAdmin(admin.ModelAdmin):
    model = About
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

admin.site.register(About, AboutAdmin)
admin.site.register(Category)