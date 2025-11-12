from rest_framework import serializers
from .models import Journal, Issue, Author, Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "affiliate", "email"]


class ArticleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    # expose pdf_file as pdf_url for consistency in API response
    pdf_url = serializers.CharField(source="pdf_file", read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "abstract",
            "keywords",
            "pdf_url",
            "authors",
            "issue",
        ]


class IssueSerializer(serializers.ModelSerializer):
    journal = serializers.StringRelatedField()
    image_url = serializers.SerializerMethodField()
    article_count = serializers.IntegerField(source="articles.count", read_only=True)

    class Meta:
        model = Issue
        fields = ["id", "title", "year", "journal", "image_url", "article_count"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None


class JournalSerializer(serializers.ModelSerializer):
    issue_count = serializers.IntegerField(source="issues.count", read_only=True)

    class Meta:
        model = Journal
        fields = ["id", "title", "description", "issue_count"]


class ArticleDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    pdf_url = serializers.CharField(source="pdf_file", read_only=True)
    issue = IssueSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "abstract",
            "keywords",
            "pdf_url",
            "authors",
            "issue",
            "created_at",
            "updated_at",
        ]


class IssueDetailSerializer(serializers.ModelSerializer):
    journal = JournalSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()
    articles = ArticleSerializer(many=True, read_only=True)
    article_count = serializers.IntegerField(source="articles.count", read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "year",
            "journal",
            "image_url",
            "article_count",
            "articles",
            "created_at",
            "updated_at",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None
