from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    excerpt = models.TextField(max_length=400)
    image_name = models.CharField(max_length=120)
    date = models.DateTimeField()
    slug = models.SlugField()
    content = models.TextField(max_length=4000)

    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="posts")

    tags = models.ManyToManyField("Tag", related_name="posts")
