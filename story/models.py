from django.db import models

# Create your models here.

class Story(models.Model):
    storyId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    sold = models.BooleanField(default=False)
    img = models.FileField(upload_to='images/', default='images/None/no-img.jpg')
"""
  id        Int      @id @default(autoincrement())
  title     String
  content   String
  sold     Boolean  @default(false)
  img String @default("")
"""