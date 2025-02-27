from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from typing import List
from ..repository import task



get_db = database.get_db

router = APIRouter(
    prefix="/task",
    tags=[" Task"],
)

@router.get("/",response_model=List[schemas.ShowTask])
def get_tasks(db: Session = Depends(get_db)):
    return task.get_all(db)

##CREATE
@router.post("/" , status_code=status.HTTP_201_CREATED)
def create_task(request : schemas.Task, db : Session = Depends(get_db)):
    return task.create(request, db)

##READ
@router.get("/{id}", response_model=schemas.ShowTask,status_code=status.HTTP_200_OK)
def read_task(id , db : Session = Depends(get_db)):
    return task.read(id, db)

##UPDATE
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_task(id, request : schemas.Task, db : Session = Depends(get_db)):
    return task.update(id, request, db)

##DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id, db : Session = Depends(get_db)):
    return task.delete(id, db)