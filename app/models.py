from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.isactive = True
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,password=password, **extra_fields)
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
# Create your models here.


# class User(models.Model):
#     id_user= models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=30)
#     prenom = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     phone =  models.CharField(max_length=14)
#     username = models.CharField(max_length=30)
#     password = models.TextField(max_length=30)
#     created_at = models.DateField(("Date"), default=datetime.date.today)
#     updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
#     class Meta:
#         db_table='app_user'
        
# class Admin(models.Model):
    
#     id_admin = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
#     surname = models.CharField(max_length=30)
#     created_at = models.DateField(("Date"), default=datetime.date.today)
#     updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
#     class Meta:
#         db_table='app_admin'
        
# class Client(models.Model):
    
#     id_client = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
#     niv_fidélité = models.IntegerField(default=1)
#     created_at = models.DateField(("Date"), default=datetime.date.today)
#     updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
#     class Meta:
#         db_table='app_client'
    

class Categorie(models.Model):
    
    id_categorie = models.AutoField(primary_key=True)
    titre_category = models.CharField(max_length=400)
    nbr_book = models.IntegerField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_categorie'
    
class Paiment(models.Model):
    
    id_paiment = models.AutoField(primary_key=True)
    some_paiment = models.FloatField()
    id_user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_paiment'
        
    
class Book(models.Model):
    
    id_book = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    id_categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    price=models.FloatField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_book'
    



class Commande(models.Model):
    
    id_commande = models.AutoField(primary_key=True)
    Commande_price = models.FloatField() ##
    id_paiment =  models.OneToOneField(Paiment,on_delete=models.PROTECT)
    id_user =  models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='LigneCommande')
    nbr_produit =models.IntegerField()  ##
    etat = models.CharField(max_length=100,default="pending",editable=True)
    created_at = models.DateField(("Date"), default=datetime.date.today)##
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today) ##
    class Meta:
        db_table='app_commande'


class LigneCommande(models.Model):
    
    id_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    id_commande= models.ForeignKey(Commande,on_delete=models.CASCADE)
    book_quantity = models.IntegerField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_lignecommande'

