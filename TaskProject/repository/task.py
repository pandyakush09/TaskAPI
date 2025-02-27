from fastapi import HTTPException
from ..import schemas, models
from sqlalchemy.orm import Session

def get_all(db: Session):
    tasks_to_delete = db.query(models.Task).filter(models.Task.completed == True).all()

    for task in tasks_to_delete:
        db.delete(task)

    db.commit()
    task = db.query(models.Task).all()
    return task


def create(request : schemas.Task , db : Session):
    new_task = models.Task(title=request.title, description=request.description, completed=request.completed, user_id=1)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def read(id : int, db : Session):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task

def update(id : int, request : schemas.Task , db : Session):
    task = db.query(models.Task).filter(models.Task.id == id).update(request.dict())
    db.commit()
    return "Task Updated"

def delete(id : int, db : Session):
    task = db.query(models.Task).filter(models.Task.id == id).delete(synchronize_session=False)
    db.commit()
    return "Task Deleted"
