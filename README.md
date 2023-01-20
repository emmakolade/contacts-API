# ContactList-API

Contalist API is a RESTful API that allows user to manage and access a list of contacts. With this API, you can perform CRUD (Create, Read, Update, and Delete) operations on your contacts.

## Features
Register and Login
Create, Read, Update and Delete Contacts
User authentication and authorization

### Register and Login
Endpoints are provided for registration and login. Users can create an account by providing their email, first name, last name, username and password.

#### Register
* **URL**: /register/
* **Method**: POST
* **Data parameters**:
   * username (required)
   * password (required)
   * first_name (required)
   * last_name (required)
   * email (required)
* **Success response**
  * Code: 201 CREATED
  *Content: The created user object
  
### Login
* **URL**: /login/
* **Method**: POST
* **Data parameters**:
  * username (required)
  * password (required)
* **Success response**
  * Code: 200 OK
  * Content: The user object and JWT token
* **Error response**
  * Code: 401 UNAUTHORIZED
  
## Endpoints
The ContaList API has the following endpoints:

* **GET /contacts**: Retrieve a list of all contacts
* **GET /contacts/<id>**: Retrieve a specific contact by ID
* **POST /contacts**: Create a new contact
* **PUT /contacts/<id>**: Update an existing contact
* **DELETE /contacts/<id>**: Delete a contact

## Contact Model
A contact has the following fields:

* **user**: A foreign key to the user who owns the contact.
* **country_code**: A string representing the country code of the contact's phone number.
* **first_name**: A string representing the first name of the contact.
* **last_name**: A string representing the last name of the contact.
* **phone_number**: A string representing the phone number of the contact.
* **email**: The email address of the contact
* **address**: The mailing address of the contact
* **contact_picture**: A URL for the contact's picture.
* **is_favorite**: A boolean indicating whether the contact is marked as a favorite.

## Example usage
```python
# Retrieve a list of all contacts
GET /contacts

# Retrieve a specific contact
GET /contacts/123

# Create a new contact
POST /contacts
{
    "user":1,
    "country_code":"+1",
    "first_name": "John",
    "last_name":"Doe",
    "phone_number": "555-555-5555",
    "email": "johndoe@example.com", 
    "address": "123 Main St, Anytown USA 12345"
    "contact_picture": "https://example.com/johndoe.jpg",
    "is_favourite": true
}

# Update an existing contact
PUT /contacts/123
{
    "user":1,
    "country_code":"+1",
    "first_name": "Jane",
    "last_name":"Doe",
    "phone_number": "555-555-5555",
    "email": "johndoe@example.com", 
    "address": "123 Main St, Anytown USA 12345"
    "contact_picture": "https://example.com/janedoe.jpg",
    "is_favourite": true
}

# Delete a contact
DELETE /contacts/123

```
