from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Definition of model blog post (an object)
    \nPost = name of the model

    Args:
        models (Django Model): models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # a link to another model
    title = models.CharField(max_length=200)                                        # define text with a limited number of characters
    text = models.TextField()                                                       # long text without a limit
    created_date = models.DateTimeField(default=timezone.now)                       # 
    published_date = models.DateTimeField(blank=True, null=True)                    # 

    def publish(self):
        """ Publish the blog post
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Get the post title

        Returns:
            string: Blog post Title
        """
        return self.title