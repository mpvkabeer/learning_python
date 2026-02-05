from django.db import models
from django.contrib.auth.models import User

class MyApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    myapp_name = models.CharField(max_length=100)
    myapp_description = models.TextField()
    myapp_image = models.ImageField(upload_to="myapp")
    myapp_view_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.myapp_name