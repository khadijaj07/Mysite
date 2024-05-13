from django.urls import path,include
from . import views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView


router = routers.SimpleRouter()

router.register('category', ProductViewset, basename='category')
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
path('index/', views.index, name='index'),
path('majProduit/', views.form, name='majProduit'),
path('vitrine/', views.vitrine, name='vitrine'),
path('', views.acceuil1, name='acceuil'),
path('acceuil/', views.acceuil, name='acceuil'),

path('nouvFournisseur/', views.formFournisseur, name='Fournisseur'),

path('commande/',views.commande, name='commande'),
path('register/',views.register, name = 'register'),

    path('login/', views.user_login, name='login'), 
    path('logout/', views.logoutview, name='logout'), 
    path('api/category/', CategoryAPIView.as_view()),

    path('api/', include(router.urls))

]