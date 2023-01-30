from django.contrib import admin
from .models import Categorie,Book,LigneCommande,Paiment,Commande

# Register your models here.
# admin.site.register(User);
# admin.site.register(Admin);
# admin.site.register(Client);
admin.site.register(Categorie);
admin.site.register(Paiment);
admin.site.register(Commande);
admin.site.register(Book);
admin.site.register(LigneCommande);