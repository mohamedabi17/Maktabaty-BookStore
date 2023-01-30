
from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Categorie,Book,Commande,LigneCommande,Paiment,UserAccount
import requests
from rest_framework import status
from . import urls

# from .serializers import ClientSerializer,BookSerializer
# from rest_framework import status
from .serializers import CategorieSerializer,BookSerializer,CommandeSerializer,LigneCommandeSerializer,PaimentSerializer,UserCreateSerializer
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# import requests
# from django.shortcuts import render
# from django.db import connection
# from django.http import HttpResponse
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


def index(request):
    return render(request,'index.html')


# @api_view(['GET'])
# @permission_classes([AllowAny])
# class AddPostView(APIView):
#     def post(self, request, format=None):
#         user = self.request.user

#         if not user.is_business:
#             return Response(
#                 {'error': 'Not business account'},
#                 status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([AllowAny])
def getproducts(request):
    if (request.method =='GET'):
        allBooks = Book.objects.all()
        serilize = BookSerializer(allBooks,many=True)
        content = {
        'status': 'request was permitted'
    }
        return Response(serilize.data)
@api_view(['GET'])
@permission_classes([AllowAny])
def getcategories(request):
    if (request.method =='GET'):
        allcotegories = Categorie.objects.all()
        serilize = CategorieSerializer(allcotegories,many=True)
        return Response(serilize.data)
# @api_view(['GET','PUT','DELETE'])
# @permission_classes([AllowAny]) 
# def insertproduct(request):
#     if request.method=="POST":
#         id_book=request.POST.get('id_book')
#         titre=request.POST.get('titre')
#         id_categorie=request.POST.get('id_categorie')
#         description=request.POST.get('description')
#         img=request.POST.get('img')
#         price=request.POST.get('price')
#         data ={'id_book':id_book,'titre':titre,'id_categorie':id_categorie,'description':description,'img':img,'price':price}
#         headers={'Content-Type': 'application/json'}
#         requests.post('http://127.0.0.1:8000/Insertproduitapi',json=data,headers=headers)
#         return render(request,'Addproduct.js')
#     else:
#         return render(request,'Addproduct.js')

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def products(request):
    if (request.method =='GET'):
        books = Book.objects.all()
        serilizer = BookSerializer(books,many=True)
        return Response(serilizer.data)
    if (request.method =='POST'):
        serilizer = BookSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def users(request):
    if (request.method =='GET'):
        users= UserAccount.objects.all()
        serilizer = UserCreateSerializer(users,many=True)
        return Response(serilizer.data)
    if (request.method =='POST'):
        serilizer = UserCreateSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])
def product_detail(request,id):
    try:
        book=Book.objects.get(id_book=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET','PUT','DELETE'])
# @permission_classes([AllowAny])
# def commande_detail(request,id_command,id_book):
#     try:
#         LigneCommand=LigneCommande.objects.get(id_commande=id,id_book=id_book)
#     except LigneCommand.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = LigneCommandeSerializer(LigneCommand)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer=LigneCommandeSerializer(LigneCommand,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         LigneCommand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def LignesCommandes(request):
    if (request.method =='GET'):
        lignes = LigneCommande.objects.all()
        serilizer = LigneCommandeSerializer(lignes,many=True)
        return Response(serilizer.data)
    if (request.method =='POST'):
        serilizer = LigneCommandeSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def Commandes(request):
    if (request.method =='GET'):
        commandes = Commande.objects.all()
        serilizer = CommandeSerializer(commandes,many=True)
        return Response(serilizer.data)
    if (request.method =='POST'):
        serilizer = CommandeSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def Payments(request):
    if (request.method =='GET'):
        paiments = Paiment.objects.all()
        serilizer =PaimentSerializer(paiments,many=True)
        return Response(serilizer.data)
    if (request.method =='POST'):
        serilizer = PaimentSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])
def command_detail(request,id):
    try:
        commande=Commande.objects.get(id_commande=id)
    except Commande.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CommandeSerializer(commande)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=CommandeSerializer(commande,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','PUT','DELETE'])
# @permission_classes([AllowAny])
# def command_by_user(request,id):
#     try:
#         commandes=Commande.objects.filter(id_user=id)
#     except commandes.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = CommandeSerializer(commandes)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer=CommandeSerializer(commandes,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         commandes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([AllowAny])
def command_by_user(request,id):
    if (request.method =='GET'):
        commandes=Commande.objects.filter(id_user=id)
        serilize = CommandeSerializer(commandes,many=True)
        content = {
        'status': 'request was permitted'
    }
        return Response(serilize.data)