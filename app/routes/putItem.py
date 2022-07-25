from fastapi import APIRouter
from app.recipe_data import RECIPES

from app.schema import Recipe, RecipeUpdateRestricted
# from typing import Optional

router = APIRouter()

@router.put('/recipe/', status_code=200, response_model=Recipe)
def put_item(*,recipe_in: RecipeUpdateRestricted) -> dict:
  """ 
    Atualizar um item (somente na memória) 
  """
  recipe = RECIPES.pop(recipe_in.id - 1)
  recipe["label"] = recipe_in.label
  RECIPES.append(recipe)

  return recipe