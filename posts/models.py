from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here

class Post(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'media/', blank=True, null=True)
    body = RichTextUploadingField('body')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
