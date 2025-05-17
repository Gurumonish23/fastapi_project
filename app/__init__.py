from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

# Import and include routers from different modules
from .routes import user_routes, item_routes

# Include routers
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(item_routes.router, prefix="/items", tags=["items"])

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

# Additional application setup can be done here