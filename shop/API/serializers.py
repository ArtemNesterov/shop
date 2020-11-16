from rest_framework import serializers

from shop.models import Product, Buy, Return, MyUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['count', 'item', 'price', 'in_stock', 'description']


class BuySerialize(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ['user', 'product', 'count', 'purchase_time']


class ReturnSerialize(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = ['buy', 'return_time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'cash']
