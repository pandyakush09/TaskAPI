from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas
from typing import List
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


##GET ALL USERS
@router.get("/",response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all_user(db)

##CREATE USERS
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request : schemas.User, db : Session = Depends(database.get_db)):
    return user.create(request, db)

##READ USERS WITH ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id , db : Session = Depends(database.get_db)):
    return user.read(id, db)
