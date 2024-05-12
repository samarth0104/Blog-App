# Blog API Project

This project implements a simple Blog API using FastAPI and MongoDB. It allows users to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

## Features

- **Create Post**: Users can create a new blog post by providing a title and content.
- **Get Post**: Users can retrieve a specific blog post by its ID.
- **Update Post**: Users can update an existing blog post's title and content.
- **Delete Post**: Users can delete a blog post by its ID.

## Technologies Used

- **FastAPI**: FastAPI is used to create the RESTful API endpoints.
- **MongoDB**: MongoDB is used as the database to store the blog posts.
- **Pydantic**: Pydantic is used for data validation and serialization/deserialization of Python data structures.

## Directory Structure
└── templates # Directory containing HTML templates for frontend
    └── index.html # HTML file with forms to interact with the API
├── main.py # FastAPI application containing the API endpoints
├── requirements.txt # List of Python dependencies

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/blog-api.git
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

4. Access the API documentation and frontend interface in your browser at `http://127.0.0.1:8000`.

## API Endpoints

- **GET /posts/**: Get all blog posts.
- **POST /posts/**: Create a new blog post.
- **GET /posts/{post_id}**: Get a specific blog post by its ID.
- **PUT /posts/{post_id}**: Update an existing blog post by its ID.
- **DELETE /posts/{post_id}**: Delete a blog post by its ID.
