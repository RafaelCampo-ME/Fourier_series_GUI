from django.db import models

# Create your models here.

class documentation(models.Model):
    """_documentation_

    Args:
        models (_type_): This database model creates a table where the documentation will be storage
    """
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.TextField(max_length=250)
    title = models.TextField(max_length=250)
    body = models.TextField(max_length=2000)

def __str__(self):
    """__str__

    Returns:
        _type_: This metod contains the name that is show in the admin
    """
    return self.title

