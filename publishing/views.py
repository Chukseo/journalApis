from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Journal, Issue, Article, Author
from .serializers import (
    JournalSerializer,
    IssueSerializer,
    ArticleSerializer,
    ArticleDetailSerializer,
    AuthorSerializer,
)

class JournalListView(generics.ListAPIView):
    queryset = Journal.objects.all().prefetch_related("issues")
    serializer_class = JournalSerializer
    permission_classes = [permissions.AllowAny]


class JournalIssuesView(generics.ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        journal_id = self.kwargs["journal_id"]
        return Issue.objects.filter(journal_id=journal_id).select_related("journal")


class IssueArticlesView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        issue_id = self.kwargs["issue_id"]
        return (
            Article.objects.filter(issue_id=issue_id)
            .select_related("issue", "issue__journal")
            .prefetch_related("authors")
        )

class ArticleAuthorsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, article_id):
        authors = Author.objects.filter(articles__id=article_id).distinct().order_by("name")
        serializer = AuthorSerializer(authors, many=True, context={"request": request})
        return Response(serializer.data)

class IssueAuthorsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, issue_id):
        authors = Author.objects.filter(articles__issue_id=issue_id).distinct().order_by("name")
        serializer = AuthorSerializer(authors, many=True, context={"request": request})
        return Response(serializer.data)


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.select_related("issue", "issue__journal").prefetch_related("authors")
    serializer_class = ArticleDetailSerializer
    permission_classes = [permissions.AllowAny]

class IssueDetailView(generics.RetrieveAPIView):
    queryset = Issue.objects.select_related("journal").prefetch_related("articles__authors")
    serializer_class = IssueSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = "issue_id"
    
