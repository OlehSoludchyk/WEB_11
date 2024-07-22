from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix='/api')

@app.get('/')
def index():
    return {'message': 'Contact Application'}


@app.get('/api/healthcheker')
def healthcheker(db: Session = Depends(get_db)):
    try:
        #Make request
        result = db.execute(text('SELECT 1'))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail='Database isn\'t confifured correctly')
        return {'message': 'Welcome to FastApi!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Error connecting to the database')