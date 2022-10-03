from django.contrib import admin

# Register your models here.
from .models import Account, Comment, Post, Question, Choice
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'age']

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user_id', 'title', 'short_description')
    list_filter = ('user_id')
    list_filter = ('text', 'user_id__username')

class CommentAdmin(admin.ModelAdmin):
    list_display =('id', 'text', 'user', 'pub_date', 'post_id')
    list_filter = ('user_id', 'post_id', )
    search_fields = ('text', )
admin.site.register(Account, AccountAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
