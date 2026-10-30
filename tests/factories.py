import factory
from factory.fuzzy import FuzzyChoice
from service.models import Product, Category

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    
    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    description = factory.Faker("text")
    price = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    available = factory.Faker("boolean")
    category = FuzzyChoice(choices=[c.name for c in Category])