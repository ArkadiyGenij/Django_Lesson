import json

from django.core.management import BaseCommand

from shop.models import Product, Category


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('shop_data.json', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def json_read_products():
        with open('shop_data.json', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        category_for_create = []
        product_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in self.json_read_categories():
            category_for_create.append(
                Category(name=category["name"], description=category["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in self.json_read_products():
            product_for_create.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    image=product["image"],
                    category=Category.objects.get(name=product["category"]),
                    price=product["price"],
                    created_at=product["created_at"],
                    updated_at=product["updated_at"]
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
