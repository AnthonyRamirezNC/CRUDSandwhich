from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, recipe):
    db_recipe = models.Recipe(
        sandwich_id = recipe.sandwich_id,
        resource_id = recipe.resource_id,
        amount = recipe.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh()
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update(db: Session, recipe, recipe_id):
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    update_data = recipe.dict(exclude_unset = True)
    db_recipes.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipes.first()

def delete(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
