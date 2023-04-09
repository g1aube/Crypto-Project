from django.contrib import admin
from .models import CustomUser, Category, Post

@admin.register(CustomUser)
class CastomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass