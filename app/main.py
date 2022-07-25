from fastapi import FastAPI
from app.routes import getAllItem, getById, postItem, deleteItem, putItem
# import uvicorn

app = FastAPI()

# Configura CORS

if __name__ == "__main__":
  # Use this for debugging purposes only
  import uvicorn

# Assignment Part 1: GET endpoint
app.include_router(getAllItem.router)
app.include_router(getById.router)
# Assignment Part 2: POST endpoint  
app.include_router(postItem.router)
# Assignment Part 3: DELETE endpoint
app.include_router(deleteItem.router)
# Assignment Part 4: PUT endpoint
app.include_router(putItem.router)
