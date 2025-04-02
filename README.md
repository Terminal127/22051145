> **Note:** In a production environment, sensitive credentials should be stored in environment variables. However, for testing purposes, credentials were hardcoded in this implementation to simplify development and debugging.
> 
>  **Note:** Screenshots would take some time to load so please be patient.

# FIRST CODE
# FastAPI Number Service

## Overview
This FastAPI-based service fetches numbers from an external API and maintains a sliding window for each type of number. The supported number types are:

- **Prime Numbers (`p`)**
- **Fibonacci Numbers (`f`)**
- **Even Numbers (`e`)**
- **Random Numbers (`r`)**

It maintains a sliding window of the last 10 numbers for each category and calculates their average.

---

## Features
- **Authentication**: Uses a token-based authentication system to interact with the external API.
- **Sliding Window**: Maintains a window of the last 10 numbers for each type.
- **FastAPI Integration**: Uses asynchronous requests to fetch numbers efficiently.
- **Error Handling**: Handles HTTP errors and timeouts gracefully.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Terminal127/22051145
   cd 22051145
   ```
2. Install dependencies:
   ```bash
   pip install fastapi httpx uvicorn
   ```
3. Run the server:
   ```bash
   uvicorn cal:app --host 127.0.0.1 --port 9876 --reload
   ```

---

## API Endpoints
### 1. Fetch Numbers
#### Endpoint:
```http
GET /numbers/{numberid}
```
#### Parameters:
- `numberid`: Can be one of the following:
  - `p` (Prime Numbers)
  - `f` (Fibonacci Numbers)
  - `e` (Even Numbers)
  - `r` (Random Numbers)

#### Response:
```json
{
    "windowPrevState": [...],
    "windowCurrState": [...],
    "numbers": [...],
    "avg": 12.34
}
```
#### Example:
Fetching **even numbers (`e`)**:
```http
GET /numbers/e
```
#### Sample Response:
```json
{
    "windowPrevState": [2, 4, 6, 8],
    "windowCurrState": [2, 4, 6, 8, 10, 12],
    "numbers": [10, 12],
    "avg": 7
}
```

---

## Authentication
The API requires authentication to fetch numbers. The authentication request is handled automatically in the background. The token is cached and refreshed when needed.

---

## Example Responses
### Prime Numbers (`p`)
![Prime Numbers](https://github.com/user-attachments/assets/6a3ed858-7163-4644-a233-cd55d64855f8)

### Even Numbers (`e`)
![Even Numbers](https://github.com/user-attachments/assets/abe147a9-face-4bb5-9865-02505d37e155)
![Even Numbers 2](https://github.com/user-attachments/assets/f5753ae5-1bb9-429f-8962-81d9dccfd701)

### Random Numbers (`r`)
![Random Numbers](https://github.com/user-attachments/assets/0f2925ee-74fe-4b08-81de-ee147c3fe1bc)

---

## Error Handling
- **400 Bad Request**: If an invalid `numberid` is provided.
- **500 Internal Server Error**: If the authentication or API call fails.
- **504 Gateway Timeout**: If the API request times out.

---

## Contributing
Feel free to open an issue or submit a pull request if you find any bugs or have suggestions.

---

## License
This project is licensed under the MIT License.

# SECOND CODE
# FastAPI User Service

## Overview
This FastAPI-based service fetches user data, user posts, and post comments from an external API with authentication. The supported endpoints allow:

- **Fetching all users**
- **Fetching posts of a specific user**
- **Fetching comments on a specific post**

The service uses token-based authentication for secure API access.

---

## Features
- **Authentication**: Uses a token-based authentication system with caching.
- **FastAPI Integration**: Fully asynchronous API for efficient requests.
- **Error Handling**: Handles HTTP errors and timeouts gracefully.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Terminal127/22051145
   cd 22051145
   ```
2. Install dependencies:
   ```bash
   pip install fastapi httpx uvicorn
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

---

## API Endpoints
### 1. Get All Users
#### Endpoint:
```http
GET /users
```
#### Response:
```json
[
    {"id": "1", "name": "John Doe"},
    {"id": "2", "name": "Jane Smith"}
]
```
#### Example Request:
```http
GET /users
```
#### Example Response:
![Users Response](https://github.com/user-attachments/assets/8855737b-88b5-4aa3-8aa3-373f72992fa8)

---

### 2. Get Posts of a Specific User
#### Endpoint:
```http
GET /users/{user_id}/posts
```
#### Parameters:
- `user_id`: The unique ID of the user.

#### Response:
```json
[
    {"post_id": "101", "title": "My first post"},
    {"post_id": "102", "title": "Another post"}
]
```
#### Example Request:
```http
GET /users/1/posts
```
#### Example Response:
![User Posts](https://github.com/user-attachments/assets/0d7670c8-1ad0-46e6-9168-5bb1f970c4cf)

---

### 3. Get Comments on a Specific Post
#### Endpoint:
```http
GET /posts/{post_id}/comments
```
#### Parameters:
- `post_id`: The unique ID of the post.

#### Response:
```json
[
    {"comment_id": "1001", "text": "Great post!"},
    {"comment_id": "1002", "text": "Very helpful!"}
]
```
#### Example Request:
```http
GET /posts/101/comments
```

### Example response
![image](https://github.com/user-attachments/assets/2cfd2a81-1f19-43b0-bfdd-6e8cf3e292f2)

---

## Authentication
The API requires authentication to access user and post data. The authentication request is handled automatically in the background, and the token is cached for efficient use.

---

## Error Handling
- **400 Bad Request**: If an invalid request is made.
- **500 Internal Server Error**: If authentication or API calls fail.
- **504 Gateway Timeout**: If the API request times out.


