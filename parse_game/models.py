from django.db import models

class ParseData(models.Model):
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-published']

