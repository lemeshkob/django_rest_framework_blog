from django.db import models


class Post(models.Model):

    """
    Post model created for the DRF demo project
    title (str) - Post title
    content (str) - Post content
    created (dateTime) - Creation dateTime stamp
    owner (foreignKey) - Owner of the post (userObject)
    """

    class Meta:
        db_table = 'posts'

    title = models.CharField(
        max_length=350,
        blank=False,
        null=False,
        verbose_name='Post name'
    )

    content = models.TextField(
        blank=False,
        null=False,
        verbose_name='Post content'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation time'
    )

    owner = models.ForeignKey(
        'auth.User',
        related_name='posts',
        on_delete=models.CASCADE
    )
