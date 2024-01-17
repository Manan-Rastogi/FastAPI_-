# 1. Import Libraries
import uvicorn                                 # ASGI
from fastapi import FastAPI

# 2. Create app
app= FastAPI()

# 3. Index Route
@app.get('/')
def index():
    return {
        'message': 'Welcome to your journey on FastAPI.'
    }

# 4. Routing with Parameter
@app.get('/Welcome')
def get_name(name: str):
    return{
        'message': f'Hi {name}, Let\'s Get Started!'
    }

# 5. Run with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
