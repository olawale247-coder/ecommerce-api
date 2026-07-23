
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import ProductViewSet, CategoryViewSet
from store.auth_views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse, request

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce API",
        "endpoints": {
            "products": "/api/products/",
            "categories": "/api/categories/",
            "register": "/api/auth/register/",
            "login": "/api/auth/login/",
            "token_refresh": "/api/auth/token/refresh/"
        },
        "status": "Running"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]