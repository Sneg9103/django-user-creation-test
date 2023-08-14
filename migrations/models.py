from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model, which replaces Django's default User model.
    
    This model uses `email` as the primary identifier, instead of the default `username`.

    Attributes:
        login (CharField): The login of the user.
        email (EmailField): The email address of the user.
    """

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']
    login = models.CharField('login', max_length=150)
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return f"{self.login}"


class Good(models.Model):
    id = models.AutoField(primary_key=True)
    good_name = models.CharField(max_length=255)
    good_code = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.TextField()
    supplier_phone = models.CharField(max_length=50)
    supplier_contact = models.CharField(max_length=255)
    is_bulk = models.BooleanField()
    price = models.PositiveIntegerField()
    dt_of_license = models.DateField()

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return f'Good: {self.good_name}'

