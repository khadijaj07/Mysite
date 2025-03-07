from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import ProduitForm, FournisseurForm, CommandeForm, UserRegistrationForm
from .models import Produit, Fournisseur, Commande
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie, Produit
from magasin.serializers import CategorySerializer ,ProduitSerializer
from rest_framework import viewsets



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('vitrine')
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('vitrine')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})




def index(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)

def form(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # create empty form
    return render(request, 'magasin/majProduits.html', {'form': form})


def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine/vitrine.html',{'list':list})

@login_required
def acceuil(request):
    context={'val':"Menu Acceuil"}
    return render(request,'magasin/acceuil.html',context )
  
  

def formFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm()  
    return render(request, 'magasin/fournisseur.html', {'form': form})

def Fournisseur(request):
    list=Fournisseur.objects.all()
    print(list)
    return render(request,'magasin/fournisseur.html',{'list':list})



def commande(request):
    commandes = Commande.objects.all()

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CommandeForm()

    context = {'form': form, 'commandes': commandes}
    return render(request, 'magasin/Commande.html', context)






def logoutview(request):
    logout(request)  
    return render(request, 'magasin/acceuil.html')
  
def acceuil1(request):
    
    return render(request, 'magasin/acceuil.html')
    
class CategoryAPIView(APIView):
  def get(self, *args, **kwargs):
    categories = Categorie.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
  
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
      queryset = Produit.objects.all()
      category_id = self.request.GET.get('category_id')
      if category_id:
        queryset = queryset.filter(categorie_id=category_id)
      return queryset


