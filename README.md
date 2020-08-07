# udplatforms assignment

This repository presents the assignment I have received from udplatforms. 
This is a Django Rest Framework App where I have created RESTFul API. The test cases which I have written can be found in api/users/tests.py module. For the views I have used ModelViewSet of Django Rest Framework viewsets, which creates all the apis required for CRUD and getting the list for a model, thus maintaining DRY principle. The configuration of the application can be found in the project/settings.py module. I have created two models using ORM with sqlite3 for the application. The models can be found in base/models.py module. There are two models, one is Parent model and the other is Child model. The Parent model is related to the Child model with a one to many relationship.  

The Parent model has the following fields with validation:
- id primary key uuid field
- first_name, max length can be 256 and cannot be empty
- last_name, max length can be 256 and cannot be empty
- street_address, max length can be 256 and cannot be empty
- city, max length can be 256 and cannot be empty
- state, max length can be 256 and cannot be empty
- zip, max length can be 256 and cannot be empty

The Child model has the following fields with validation:
- id primary key uuid field
- first_name, max length can be 256 and cannot be empty
- last_name, max length can be 256 and cannot be empty
- parent_id, foreign key beloning to Parent

Here are the steps to run the test cases and the application:
1)  A python virtual environment is needed. 
2. To ensure the correct packages are used to run the test cases, the packages can be installed using the command:

```
$ pip install -r requirements.txt
```
3. Now the test cases can be ran using the command:

```
$ pytest --nomigrations --create-db
```
4. The Application can be run locally using:
```
$ python manage.py runserver
```

# Technoligies used

  - Python 3.6.9
  - Pytest Django 3.9.0
  - Django 3.1
  - Django REST Framework 3.11.1
  - Factory - boy 2.12.0
  - sqlite3

### APIs:

#### API Request examples

**URL** : "/api/parents/"
**Method** : GET
**Responses** : 
​
**200** : 

```json 
[
    {
        "id": "8438f290-dff9-4dce-a8ab-7dad988c6156",
        "first_name": "Kimberly",
        "last_name": "Ayala",
        "street_address": "Hope Street 4532",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97046",
        "children": [
            {
                "id": "0bf4a6cb-8638-4b8a-81d9-06d840893e02",
                "first_name": "Michelle",
                "last_name": "Short"
            },
            {
                "id": "5583a50b-201d-4fce-a17d-88febd205359",
                "first_name": "Jason",
                "last_name": "Cortez"
            },
            {
                "id": "003b70fb-68ae-40b5-955b-44eddb2b95d8",
                "first_name": "Terri",
                "last_name": "Murphy"
            },
            {
                "id": "8ea0f547-def5-4d6f-ac04-0ada33a0e3f2",
                "first_name": "Bryan",
                "last_name": "Holt"
            },
            {
                "id": "f83981df-9a2c-4b34-8126-f178bb0082ed",
                "first_name": "Holly",
                "last_name": "Hall"
            },
            {
                "id": "6966de1b-b968-4af5-b82d-df148d6ebc32",
                "first_name": "Daren Jr.",
                "last_name": "domino"
            }
        ]
    },
    {
        "id": "7e3ce60c-a47f-4060-8734-39a07a94e2da",
        "first_name": "Jason",
        "last_name": "Street",
        "street_address": "West Street 4512",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97042",
        "children": [
            {
                "id": "929ad974-f0a3-49dd-8658-ce9dfe3567fa",
                "first_name": "Jason",
                "last_name": "Street Jr"
            },
            {
                "id": "ce636734-28a2-4c93-85e8-769f38111e3f",
                "first_name": "Jason",
                "last_name": "Street Sr"
            }
        ]
    }
]
```

**URL** : "/api/parents/"
**Method** : POST
**Request Data** : 

```json 
{
        "first_name": "Jason",
        "last_name": "Street",
        "street_address": "West Street 4512",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97042"
}
```
**Responses** : 
​
**201** : 

```json 
{
    "id": "dc74cc7c-1e7d-4fcc-8a59-18a9d650212d",
    "first_name": "Jason",
    "last_name": "Street",
    "street_address": "West Street 4512",
    "city": "Portland",
    "state": "Oregon",
    "zip": "97042",
    "children": []
}
```

**URL** : "/api/parents/<parent_id>/"
**Method** : PUT
**Request Data** : 

```json 
{
        "first_name": "Jason",
        "last_name": "Borne",
        "street_address": "East Street 4512",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97042"
}
```
**Responses** : 
​
**200** : 

```json 
{
    "id": "dc74cc7c-1e7d-4fcc-8a59-18a9d650212d",
    "first_name": "Jason",
    "last_name": "Borne",
    "street_address": "East Street 4512",
    "city": "Portland",
    "state": "Oregon",
    "zip": "97042",
    "children": []
}
```

**URL** : "/api/parents/<parent_id>/"
**Method** : PATCH
**Request Data** : 

```json 
{
        "first_name": "Jamil"
}
```
**Responses** : 
​
**200** : 

```json 
{
    "id": "dc74cc7c-1e7d-4fcc-8a59-18a9d650212d",
    "first_name": "Jamil",
    "last_name": "Borne",
    "street_address": "East Street 4512",
    "city": "Portland",
    "state": "Oregon",
    "zip": "97042",
    "children": []
}
```

**URL** : "/api/parents/<parent_id>/"
**Method** : DELETE

**Responses** : 
**204** 


**URL** : "/api/parents/<parent_id>/children/"
**Method** : GET
**Responses** : 

**200** : 

``` json
[
    {
        "id": "0bf4a6cb-8638-4b8a-81d9-06d840893e02",
        "first_name": "Michelle",
        "last_name": "Short"
    },
    {
        "id": "5583a50b-201d-4fce-a17d-88febd205359",
        "first_name": "Jason",
        "last_name": "Cortez"
    },
    {
        "id": "003b70fb-68ae-40b5-955b-44eddb2b95d8",
        "first_name": "Terri",
        "last_name": "Murphy"
    },
    {
        "id": "8ea0f547-def5-4d6f-ac04-0ada33a0e3f2",
        "first_name": "Bryan",
        "last_name": "Holt"
    },
    {
        "id": "f83981df-9a2c-4b34-8126-f178bb0082ed",
        "first_name": "Holly",
        "last_name": "Hall"
    },
    {
        "id": "6966de1b-b968-4af5-b82d-df148d6ebc32",
        "first_name": "Daren Jr.",
        "last_name": "domino"
    }
]
```

**URL** : "/api/parents/<parent_id>/children/"
**Method** : POST
**Request Data** : 

```json 
{
        "first_name": "Julia",
        "last_name" : "Becky"
}
```
**Responses** : 
​
**201** : 

```json 
{
    "id": "1ea82c6a-b09d-4db2-9258-1de40d36db40",
    "first_name": "Julia",
    "last_name": "Becky"
}
```

**URL** : "/api/parents/<parent_id>/children/<child_id>/"
**Method** : PUT
**Request Data** : 

```json 
{
        "first_name": "Julia",
        "last_name" : "Claude"
}
```
**Responses** : 
​
**200** : 

```json 
{
    "id": "1ea82c6a-b09d-4db2-9258-1de40d36db40",
    "first_name": "Julia",
    "last_name": "Claude"
}
```

**URL** : "/api/parents/<parent_id>/children/<child_id>/"
**Method** : PATCH
**Request Data** : 

```json 
{
        "first_name": "Emily"
}
```
**Responses** : 
​
**200** : 

```json 
{
    "id": "1ea82c6a-b09d-4db2-9258-1de40d36db40",
    "first_name": "Emily",
    "last_name": "Claude"
}
```

**URL** : "/api/parents/<parent_id>/children/<child_id>/"
**Method** : DELETE

**Responses** : 
**204** 

# Test Cases

1) test_get_parent_list
2) test_create_parent
3) test_create_parent_validation_error_keeping_field_city_empty
4)  test_create_parent_validation_error_sending_empty_field
5) test_create_parent_validation_error_sending_more_than_256_characters
6) test_update_parent
7) test_partial_update_parent
8) test_delete_parent
9) test_get_children_list
10) test_get_children_list_does_not_exist
11) test_create_child
12) test_create_child_validation_error
13) test_create_child_cant_find_parent
14) test_delete_child
15) test_update_child
16) test_partial_update_child

