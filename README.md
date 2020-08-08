# udplatforms assignment

This repository presents the assignment I have received from udplatforms. 
This is a Django Rest Framework App where I have created RESTFul API. For creating the APIs I have followed the apigee web api design methodology, which basically suggests to make resource based api. The test cases which I have written can be found in api/users/tests.py module. It has been unit tested. For the views I have used ModelViewSet of Django Rest Framework viewsets, which creates all the apis required for CRUD and getting the list for the model, thus maintaining DRY principle. The configuration of the application can be found in the project/settings.py module. I have created two models using ORM with sqlite3 for the application. The models can be found in base/models.py module. There are two models, one is Parent model and the other is Child model. The Parent model is related to the Child model with a one to many relationship. With due time I could not manage to add docstrings which would have made all the functions, classes and module easier to understand. 

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
5. To see the score and corrections of linting which was done with pylint-django, which scored 7.47/10, the following command can be used:
```
$ pylint --load-plugins pylint_django project base api manage.py
```


# Technoligies used

  - Python 3.6.9
  - Pytest Django 3.9.0
  - Django 3.1
  - Django REST Framework 3.11.1
  - Factory - boy 2.12.0
  - sqlite3
  - Pylint Django 2.3.0

### APIs:

#### API Request examples

##### To see the list of the parents with their children this is the api used:


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

##### To create a parent this is the api used:

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

##### For updating a parent this is the api used:

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

##### For partial updating a parent this is the api used:

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

##### For Deleting a parent this is the api used:

**URL** : "/api/parents/<parent_id>/"
**Method** : DELETE

**Responses** : 
**204** 

##### For getting the list of the children a parent has this is the api used:

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

##### For creating a child has this is the api used:

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

##### For updating a child has this is the api used:

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

##### For partial updating a child has this is the api used:

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

##### For Deleting a child has this is the api used:

**URL** : "/api/parents/<parent_id>/children/<child_id>/"
**Method** : DELETE

**Responses** : 
**204** 

# Brief Test Cases Explanation

1) test_get_parent_list: 
This checks whether we get the correct response and data from the url "/api/parents/"
2) test_create_parent: 
This checks whether we can correctly create a parent model in the url "/api/parents/" with correct responses
3) test_create_parent_validation_error_keeping_field_city_empty:
This checks if validation error is raised if one of the field is missing
4)  test_create_parent_validation_error_sending_empty_field:
This checks if validation error is raised if one of the field is kept empty
5) test_create_parent_validation_error_sending_more_than_256_characters:
This checks if validation error is raised if one of the field exceeds more than 256 characters
6) test_update_parent:
This checks if the parent model can update with correct response in the url "/api/parents/<parent_id>/"
7) test_partial_update_parent:
This checks if the parent model can partially update with correct response in the url "/api/parents/<parent_id>/"
8) test_delete_parent:
This checks if the parent model can delete with correct response in the url "/api/parents/<parent_id>/"
9) test_get_children_list:
This checks whether we get the correct response and data from the url "/api/parents/<parent_id>/children/"
10) test_get_children_list_does_not_exist:
This checks whether we get http 404 response when the parent_id is does not exist in the url "/api/parents/<parent_id>/children/"
11) test_create_child:
This checks whether we can correctly create a child model in the url "/api/parents/<parent_id>/children/" with correct responses
12) test_create_child_validation_error:
13) test_create_child_cant_find_parent
14) test_delete_child:
This checks if the child model can delete with correct response in the url "/api/parents/<parent_id>/children/<child_id>/"
15) test_update_child:
This checks if the child model can update with correct response in the url "/api/parents/<parent_id>/children/<child_id>/"
16) test_partial_update_child:
This checks if the child model can partially update with correct response in the url "/api/parents/<parent_id>/children/<child_id>/"
