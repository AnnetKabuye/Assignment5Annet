from django.contrib import admin
from myblog.models import myBlog, Category
from myblog.models import myBlog, Category
class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(myBlog)
admin.site.register(Category)
