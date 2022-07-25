from fastapi import APIRouter
from app.recipe_data import RECIPES

# from typing import Optional
from app.schema import Recipe, RecipeCreate

router = APIRouter()

@router.post('/recipe', status_code=200, response_model= Recipe)
def create_item(*, recipe_in: RecipeCreate) -> dict:
  new_entry_id = len(RECIPES) + 1
  recipe_entry = Recipe(
    id= new_entry_id,
    label=recipe_in.label,
    source=recipe_in.source,
    url=recipe_in.url,
  )
  RECIPES.append(recipe_entry.dict())
  
  return recipe_entry