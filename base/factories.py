import factory

from base.models import Parent
from base.models import Child


class ParentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Parent

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    street_address = factory.Sequence(lambda n: 'Hope Street 453%d' % n)
    city = 'Portland'
    state = 'Oregon'
    zip = '97045'


class ChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = Child

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    parent = factory.SubFactory(ParentFactory)

