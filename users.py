from typing import List
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
import passwrd
from fastapi import APIRouter
from database import get_db
from pydantic import EmailStr

#create api endpoint/ url/ router
router = APIRouter(
    prefix='/generate-password',
    tags=['Users']
)

#checking purpose get request for inserted user login table data
@router.get('/')
def test_users(db: Session = Depends(get_db)):
    user = db.query(models.UserLogin).all()
    return  user


@router.post('')
#EmailStr a email validation formate from pydantic 
def post_req(email:EmailStr, length:int, db:Session = Depends(get_db)):
    if length<6:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Password is too short and not secure")
    else:
        passw=passwrd.genpass(length)#password generator function call using length parameter
        #print(passw)
        #query for data inserted in Login table
        login_info = models.UserLogin(email=email, password=passw)
        db.add(login_info)
        db.commit()
        db.refresh(login_info)
    return {'Email':email, 'password':passw,'length':length}
