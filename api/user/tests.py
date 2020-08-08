import uuid

from django.urls import reverse

from rest_framework.test import APITestCase

from base.factories import *


class GetParentAPITestCase(APITestCase):
    def setUp(self):
        super(GetParentAPITestCase, self).setUp()
        self.parent = ParentFactory()

    def test_get_parent_list(self):
        child1 = ChildFactory(parent=self.parent)
        child2 = ChildFactory(parent=self.parent)
        child3 = ChildFactory(parent=self.parent)
        url = reverse('api_user:parent-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()[0].get('children')), 3)
        self.assertEqual(len(response.json()), 1)


class CreateParentAPITestCase(APITestCase):
    def setUp(self):
        super(CreateParentAPITestCase, self).setUp()

    def test_create_parent(self):
        data = {
            'first_name': 'Jamil',
            'last_name': 'Ahmed',
            'street_address': 'Hope Street 4534',
            'city': 'Portland',
            'state': 'Oregon',
            'zip': '97045'
        }
        url = reverse('api_user:parent-list')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), data['last_name'])
        self.assertEqual(response.json().get('street_address'), data['street_address'])
        self.assertEqual(response.json().get('city'), data['city'])
        self.assertEqual(response.json().get('state'), data['state'])
        self.assertEqual(response.json().get('zip'), data['zip'])

    def test_create_parent_validation_error_keeping_field_city_empty(self):
        data = {
            'first_name': 'Jamil',
            'last_name': 'Ahmed',
            'street_address': 'Hope Street 4534',
            'state': 'Oregon',
            'zip': '97045'
        }
        url = reverse('api_user:parent-list')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_parent_validation_error_sending_empty_field(self):
        data = {
            'first_name': '',
            'last_name': 'Ahmed',
            'street_address': 'Hope Street 4534',
            'state': 'Oregon',
            'zip': '97045'
        }
        url = reverse('api_user:parent-list')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_parent_validation_error_sending_more_than_256_characters(self):
        data = {
            'first_name': 'G5yDxLItsKXNeavEeDlI076ipQbsmA1BfvOiaDv4ek' +
                          'DWkC71s5b8uIwlxEuBbhoRBEitEFco0y5H2RtKVtpT' +
                          '5MEvBtmEbeA08s5dMnxU3DwBojKKw0FNupDf8e5FfI' +
                          'uykf4BdKNyFkn9YYsH1lTDn8hfd0Ehz1JB65epLfV9' +
                          'GWePD41YY6xs6GJBjS6MhGVBK4NtmSfKTbzBcbh41w' +
                          'ks08ULnrt8pECgQfAY8OCmRbgTh5FUN2T9QyIaA2na5k6uS',
            'last_name': 'Ahmed',
            'street_address': 'Hope Street 4534',
            'state': 'Oregon',
            'zip': '97045'
        }
        url = reverse('api_user:parent-list')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)


class UpdateParentAPITestCase(APITestCase):
    def setUp(self):
        super(UpdateParentAPITestCase, self).setUp()
        self.parent = ParentFactory()

    def test_update_parent(self):
        data = {
            'first_name': 'Jamil',
            'last_name': 'Ahmed',
            'street_address': 'Hope Street 4534',
            'city': 'Portland',
            'state': 'Oregon',
            'zip': '97045'
        }
        url = reverse('api_user:parent-detail', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), data['last_name'])
        self.assertEqual(response.json().get('street_address'), data['street_address'])
        self.assertEqual(response.json().get('city'), data['city'])
        self.assertEqual(response.json().get('state'), data['state'])
        self.assertEqual(response.json().get('zip'), data['zip'])

    def test_partial_update_parent(self):
        data = {
            'first_name': 'Jamil'
        }
        url = reverse('api_user:parent-detail', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), self.parent.last_name)
        self.assertEqual(response.json().get('street_address'), self.parent.street_address)
        self.assertEqual(response.json().get('city'), self.parent.city)
        self.assertEqual(response.json().get('state'), self.parent.state)
        self.assertEqual(response.json().get('zip'), self.parent.zip)


class DeleteParentAPITestCase(APITestCase):
    def setUp(self):
        super(DeleteParentAPITestCase, self).setUp()
        self.parent = ParentFactory()

    def test_delete_parent(self):
        url = reverse('api_user:parent-detail', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)


class GetChildAPITestCase(APITestCase):
    def setUp(self):
        super(GetChildAPITestCase, self).setUp()
        self.parent = ParentFactory()

    def test_get_children_list(self):
        child1 = ChildFactory(parent=self.parent)
        child2 = ChildFactory(parent=self.parent)
        child3 = ChildFactory(parent=self.parent)
        url = reverse('api_user:child-list', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_get_children_list_does_not_exist(self):
        child1 = ChildFactory(parent=self.parent)
        child2 = ChildFactory(parent=self.parent)
        child3 = ChildFactory(parent=self.parent)
        url = reverse('api_user:child-list', kwargs={'parent_id': str(uuid.uuid4())})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)


class CreateChildAPITestCase(APITestCase):
    def setUp(self):
        super(CreateChildAPITestCase, self).setUp()
        self.parent = ParentFactory()

    def test_create_child(self):
        data = {
            'first_name': 'Jamil Jr.',
            'last_name': 'Ahmed'
        }
        url = reverse('api_user:child-list', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), data['last_name'])

    def test_create_child_validation_error(self):
        data = {
            'first_name': '',
            'last_name': 'Ahmed'
        }
        url = reverse('api_user:child-list', kwargs={'parent_id': str(self.parent.id)})
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_child_cant_find_parent(self):
        data = {
            'first_name': '',
            'last_name': 'Ahmed'
        }
        url = reverse('api_user:child-list', kwargs={'parent_id': str(uuid.uuid4())})
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 404)


class DeleteChildAPITestCase(APITestCase):
    def setUp(self):
        super(DeleteChildAPITestCase, self).setUp()
        self.parent = ParentFactory()
        self.child = ChildFactory(parent=self.parent)

    def test_delete_child(self):
        url = reverse('api_user:child-detail', kwargs={'parent_id': str(self.parent.id), 'child_id' : str(self.child.id)})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)


class UpdateChildAPITestCase(APITestCase):
    def setUp(self):
        super(UpdateChildAPITestCase, self).setUp()
        self.parent = ParentFactory()
        self.child = ChildFactory(parent=self.parent)

    def test_update_child(self):
        data = {
            'first_name': 'Jamil',
            'last_name': self.child.last_name
        }
        url = reverse('api_user:child-detail', kwargs={'parent_id': str(self.parent.id), 'child_id' : str(self.child.id)})
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), self.child.last_name)

    def test_partial_update_child(self):
        data = {
            'first_name': 'Jamil'
        }
        url = reverse('api_user:child-detail', kwargs={'parent_id': str(self.parent.id), 'child_id' : str(self.child.id)})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('first_name'), data['first_name'])
        self.assertEqual(response.json().get('last_name'), self.child.last_name)