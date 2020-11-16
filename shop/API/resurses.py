from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from shop.models import MyUser, Buy, Product
from shop.API.serializers import UserSerializer, BuySerialize, ProductSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class BuyViewSet(ModelViewSet):
    serializer_class = BuySerialize
    queryset = Buy.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
