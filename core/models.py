from django.db import models



# Category
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


# Post
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(max_length=255, blank=False,)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

# Comments
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} on {self.post}'
