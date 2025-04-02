from fastapi import FastAPI, HTTPException
import httpx
import time

app = FastAPI()

# API Base URL
BASE_URL = "http://20.244.56.144/evaluation-service"

# Authentication credentials
AUTH_CREDENTIALS = {
    "email": "terminalishere127@gmail.com",
    "name": "anubhav mazumder",
    "rollNo": "22051145",
    "accessCode": "nwpwrZ",
    "clientID": "e9ea7265-0b7d-4ece-8dd3-c804e1639593",
    "clientSecret": "CfgmkCYetZNDXGQF"
}

# Token cache
token_cache = {
    "access_token": None,
    "expires_at": 0
}

async def get_auth_token():
    """Get a valid authentication token, refreshing if expired."""
    current_time = time.time()
    
    # If token exists and is not expired (with 60-second buffer)
    if token_cache["access_token"] and token_cache["expires_at"] > current_time + 60:
        return token_cache["access_token"]
    
    # Get new token
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/auth",
                json=AUTH_CREDENTIALS,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            token_data = response.json()
            
            token_cache["access_token"] = token_data["access_token"]
            token_cache["expires_at"] = token_data["expires_in"]
            
            return token_cache["access_token"]
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Authentication error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Authentication error: {str(e)}")

async def get_headers():
    """Get headers with valid authentication token."""
    token = await get_auth_token()
    return {
        "Authorization": f"Bearer {token}"
    }

@app.get("/users")
async def get_users():
    """Get all users registered on the social media application."""
    try:
        headers = await get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/users", headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}/posts")
async def get_user_posts(user_id: str):
    """Get all posts by a specific user."""
    try:
        headers = await get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/users/{user_id}/posts", headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: str):
    """Get all comments on a specific post."""
    try:
        headers = await get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/posts/{post_id}/comments", headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))