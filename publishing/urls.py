from django.urls import path
from .views import (
    JournalListView,
    JournalIssuesView,
    IssueArticlesView,
    IssueAuthorsView,
    ArticleDetailView,
    IssueDetailView,
    ArticleAuthorsView,
)

urlpatterns = [
    # Journals
    path("journals/", JournalListView.as_view(), name="journal-list"),
    path("journals/<int:journal_id>/issues/", JournalIssuesView.as_view(), name="journal-issues"),

    # Issues
    path("issues/<int:issue_id>/", IssueDetailView.as_view(), name="issue-detail"),
    path("issues/<int:issue_id>/articles/", IssueArticlesView.as_view(), name="issue-articles"),
    path("issues/<int:issue_id>/authors/", IssueAuthorsView.as_view(), name="issue-authors"),

    # Articles
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/<int:article_id>/authors/", ArticleAuthorsView.as_view(), name="article-authors"),
]