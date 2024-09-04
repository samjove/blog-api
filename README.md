# Blog API

This is a Django-based RESTful API for managing blog posts. The API allows users to create, retrieve, update, delete, and search for blog posts.

## Getting Started
Follow the instructions below to set up and run the Blog API on your local machine.

### Prerequisites 

Python 3.x
Postgres

### Installation
Clone the repository:

`git clone https://github.com/samjove/blog-api.git`

cd blog-api

Create a virtual environment. I use virtualenvwrapper but the following is more straightforward:

`python -m venv venv`
`source venv/bin/activate`   # On Windows: `venv\Scripts\activate`

Install dependencies:

`pip install -r requirements.txt`

Apply migrations:

`python manage.py migrate`

### Configuration

Edit settings.py or create a .env file with your values for a secret key, along with information needed to connect with your postgres database.
Ensure settings.py is correctly configured to use your values.

### Running the API
Start the development server:

`python manage.py runserver`

The API will be available at http://127.0.0.1:8000/posts/.

### API Endpoints
#### List All Posts
URL: /posts/
Method: GET
Description: Retrieve a list of all blog posts.
Response:
200 OK: Returns a list of posts.

Example:
    [
        {
            "id": 1,
            "title": "First post",
            "content": "New content",
            "category": "Communication",
            "tags": [
                "Communication, Technology"
            ],
            "createdAt": "2024-09-04T01:55:07.111315Z",
            "updatedAt": "2024-09-04T01:55:07.111315Z"
        },
        {
            "id": 2,
            "title": "Latest post",
            "content": "Latest content",
            "category": "Strategy",
            "tags": [
                "Business, Revenue"
            ],
            "createdAt": "2024-09-04T02:01:13.783677Z",
            "updatedAt": "2024-09-04T02:01:13.783677Z"
        }
    ]

#### Create a New Post
URL: /posts/
Method: POST
Description: Create a new blog post.

Request Body:

    {
        "title": "New Post",
        "content": "This is the content of the new post.",
        "category": "Strategy",
        "tags": ["Tech", "Business"]
    }
Response:
201 Created: Returns the created post.

#### Retrieve a Single Post
URL: /posts/{id}/
Method: GET
Description: Retrieve a specific post by ID.
Response:
200 OK: Returns the requested post.

#### Update a Post
URL: /posts/{id}/
Method: PUT or PATCH
Description: Update an existing post.

Response:

200 OK: Returns the updated post.

#### Delete a Post
URL: /posts/{id}/
Method: DELETE
Description: Delete a post by ID.
Response:
204 No Content: Post deleted successfully.

#### Search Posts
URL: /posts/?term=search_term
Method: GET
Description: Search posts by title, content, or category.
Response:
200 OK: Returns a list of posts matching the search term.

See project requirements [here](https://roadmap.sh/projects/blogging-platform-api).
