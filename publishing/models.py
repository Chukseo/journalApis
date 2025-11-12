from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Journal(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Issue(TimeStampedModel):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="issues")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="issues/", blank=True, null=True)
    year = models.PositiveIntegerField()

    class Meta:
        ordering = ["-year", "title"]
        unique_together = ("journal", "title", "year")

    def __str__(self):
        return f"{self.journal.title} — {self.title} ({self.year})"


class Author(TimeStampedModel):
    name = models.CharField(max_length=255)
    affiliate = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "affiliate", "email")

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=512, help_text="Comma-separated keywords")
    # pdf_file = models.FileField(upload_to="articles/")
    pdf_file = models.URLField(max_length=1024, blank=True, help_text="URL to the PDF file")
    authors = models.ManyToManyField(Author, related_name="articles")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
