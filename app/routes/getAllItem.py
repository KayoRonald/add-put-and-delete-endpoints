from fastapi import APIRouter
from app.recipe_data import RECIPES

# from typing import Optional
# from app.schema import Recipe

router = APIRouter()

@router.get('/', status_code=200)
def root() -> dict:
  result = [recipe for recipe in RECIPES]
  # result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
  # result = [for recipe in range(len(RECIPES)) recipe[recipe]]
  return result