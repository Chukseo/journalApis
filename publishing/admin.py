from django.contrib import admin
from .models import Journal, Issue, Author, Article

class IssueInline(admin.TabularInline):
    model = Issue
    extra = 0


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)
    inlines = [IssueInline]


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    fields = ("title", "pdf_file")
    show_change_link = True


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "journal", "year")
    list_filter = ("journal", "year")
    search_fields = ("title", "journal__title")
    inlines = [ArticleInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "affiliate", "email")
    search_fields = ("name", "affiliate", "email")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "issue")
    list_filter = ("issue__journal", "issue__year")
    search_fields = ("title", "keywords", "authors__name")
    filter_horizontal = ("authors",)
    readonly_fields = ("created_at", "updated_at")