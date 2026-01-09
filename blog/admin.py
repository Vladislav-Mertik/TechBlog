from django.contrib import admin
from django.utils.translation import ngettext
from .models import Tag, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'likes', 'is_featured', 'published_at']
    list_filter = ['is_featured', 'published_at', 'author', 'tags']
    search_fields = ['title', 'content', 'author__username']
    list_editable = ['is_featured']
    filter_horizontal = ['tags']
    readonly_fields = ['views', 'likes', 'published_at']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'author', 'content')
        }),
        ('Метадані', {
            'fields': ('tags', 'is_featured')
        }),
        ('Статистика', {
            'fields': ('views', 'likes', 'published_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_featured', 'unmark_featured', 'reset_views', 'export_articles']

    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, ngettext(
            '%d стаття позначена як рекомендована.',
            '%d статей позначено як рекомендовані.',
            updated,
        ) % updated)
    mark_as_featured.short_description = "Позначити як рекомендовані"

    def unmark_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, ngettext(
            '%d стаття видалена з рекомендованих.',
            '%d статей видалено з рекомендованих.',
            updated,
        ) % updated)
    unmark_featured.short_description = "Видалити з рекомендованих"

    def reset_views(self, request, queryset):
        updated = queryset.update(views=0)
        self.message_user(request, ngettext(
            'Лічильник переглядів скинут для %d статті.',
            'Лічильник переглядів скинут для %d статей.',
            updated,
        ) % updated)
    reset_views.short_description = "Скинути лічильник переглядів"

    def export_articles(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Заголовок', 'Автор', 'Переглядів', 'Лайків', 'Рекомендована', 'Дата публікації'])
        
        for article in queryset:
            writer.writerow([
                article.title,
                article.author.username,
                article.views,
                article.likes,
                'Так' if article.is_featured else 'Ні',
                article.published_at.strftime('%Y-%m-%d %H:%M:%S')
            ])
        
        return response
    export_articles.short_description = "Експортувати обрані статті в CSV"
