from django.db import models

class Admin(models.Model):
    loginid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.loginid
