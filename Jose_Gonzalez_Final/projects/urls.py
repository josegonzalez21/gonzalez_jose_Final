from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, InstitucionViewSet , InscritoViewSet
from .views import InscritoListCreateAPIView, InscritoDetailAPIView

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('instituciones', InstitucionViewSet)
router.register('inscritos', InscritoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('inscritos/', InscritoListCreateAPIView.as_view(), name='inscrito-list-create'),
    path('inscritos/<int:pk>/', InscritoDetailAPIView.as_view(), name='inscrito-detail'),
]
