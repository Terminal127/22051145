from fastapi import FastAPI, HTTPException
import httpx
import time

app = FastAPI()

BASE_URL = "http://20.244.56.144/evaluation-service"

AUTH_CREDENTIALS = {
    "email": "terminalishere127@gmail.com",
    "name": "anubhav mazumder",
    "rollNo": "22051145",
    "accessCode": "nwpwrZ",
    "clientID": "e9ea7265-0b7d-4ece-8dd3-c804e1639593",
    "clientSecret": "CfgmkCYetZNDXGQF"
}

token_cache = {
    "access_token": None,
    "expires_at": 0
}

windows = {
    "p": [],
    "f": [],
    "e": [],
    "r": []
}

async def get_auth_token():
    current_time = time.time()

    if token_cache["access_token"] and token_cache["expires_at"] > current_time + 60:
        return token_cache["access_token"]
    
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
            token_cache["expires_at"] = current_time + token_data["expires_in"]
            
            return token_cache["access_token"]
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Authentication error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Authentication error: {str(e)}")

async def get_headers():
    token = await get_auth_token()
    return {
        "Authorization": f"Bearer {token}"
    }

@app.get("/numbers/{numberid}")
async def get_numbers(numberid: str):

    API_URLS = {
        "p": f"{BASE_URL}/primes",
        "f": f"{BASE_URL}/fibo",
        "e": f"{BASE_URL}/even",
        "r": f"{BASE_URL}/rand",
    }
    
    if numberid not in API_URLS:
        raise HTTPException(status_code=400, detail="Invalid numberid. Use 'p', 'f', 'e', or 'r'.")
    
    headers = await get_headers()
    
    WINDOW_SIZE = 10
    global windows  
    
    window = windows[numberid]

    if window:
        window_prev_state = window.copy()  
    else:
        window_prev_state = []  
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URLS[numberid], headers=headers, timeout=0.5)
            response.raise_for_status()
            numbers = response.json().get("numbers", [])
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"API error: {e.response.text}")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="API request timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching numbers: {str(e)}")
    

    for num in numbers:
        if num not in window:
            window.append(num)
        if len(window) > WINDOW_SIZE:
            window.pop(0)  
    

    windows[numberid] = window.copy()
    
    avg = sum(window) / len(window) if window else 0
    
    return {
        "windowPrevState": window_prev_state,
        "windowCurrState": window,
        "numbers": numbers,
        "avg": round(avg, 2)
    }
