from django.db import models


class Post(models.Model):

    """
    BlogPost model created for the DRF demo project
    title (str) - BlogPost title
    content (str) - BlogPost content
    created (dateTime) - Creation dateTime stamp
    owner (foreignKey) - Owner of the BlogPost (userObject)
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

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        db_table = 'comments'

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    content = models.TextField(
        blank=False,
        null=False
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.author.username) + ' ' + str(self.post.title) + ' ' + str(self.created)
