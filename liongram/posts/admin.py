from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    # list_editable = ('content', )
    list_filter = ('created_at', )
    search_fields = ('id', 'writer__username')
    # search_help_text 버전 안됨..;
    inlines = [CommentInline]
    
    actions = []
    
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리'
            item.save()
    
#admin.site.register(Comment)
