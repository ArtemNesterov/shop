import unittest

from django.test import TestCase

from shop.models import Product


class ProductModelTest(unittest.TestCase):
    def setUp(self):
        self.tv = Product.objects.create(item='TV', price=125)
        self.phone = Product.objects.create(item='Phone', price=32)

    def test_product_item_and_price(self):
        self.assertEqual(self.tv(), 'The TV should cost 125')
        self.assertEqual(self.phone(), 'The phone should cost 32')


class ProductModelTestCase(TestCase):
    def setUpModelProduct(self):
        Product.objects.create(2, 'Smart', 432, 3, 'life-changing technique')

    def test_description_max_length(self):
        """
        test object receipt
        """
        product = Product.objects.get(item=1)
        """
        Getting the metadata of the field to obtain the required values
        """
        max_length = product._meta.get_field('item').max_length
        """
        Compare the value with the expected result
        """
        self.assertEquals(max_length, 500)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        """
        This will also fail if the urlconf is not defined.
        """
        self.assertEquals(product.get_absolute_url(), '/catalog/product/1')
