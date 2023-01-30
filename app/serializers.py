from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer
from .models import Categorie,Book,LigneCommande,Paiment,Commande
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken, Token 
# User = get_user_model()
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
user = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = user
        fields = ('id', 'email', 'first_name', 'last_name', 'password','is_staff')



# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#        model = User
#        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        
        # fields = ('id', 'email', 'first_name', 'last_name', 'password')


#  added for Unauthorized api problem
# class UserSerializerWithToken(UserCreateSerializer):
#     token = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name','password', 'token']

#     def get_token(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token.access_token)

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model =user
        fields = '__all__'

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model =Client
#         fields = '__all__'
        
# class AdminSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model =Admin
#         fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Categorie
        fields = '__all__'
        
        

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Book
        fields = ('id_book', 'titre', 'author', 'description', 'img', 'price', 'id_categorie','updated_at','created_at')

class CommandeSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Commande
        fields = ('id_commande', 'Commande_price', 'id_paiment', 'id_user', 'nbr_produit','updated_at','created_at','etat')
        

class LigneCommandeSerializer(serializers.ModelSerializer):
    class Meta: 
        model =LigneCommande
        fields = ('id_book', 'id_commande', 'book_quantity')

class PaimentSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Paiment
        fields =  ('id_paiment', 'some_paiment', 'id_user')