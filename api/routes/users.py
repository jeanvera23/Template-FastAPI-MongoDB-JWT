from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from bson import ObjectId
import logging
from api.middlewares.auth import AuthHandler

# services
import services.users as service

router = APIRouter()
auth_handler = AuthHandler()


@router.get("/")
def get_all_users(tokenUser=Depends(auth_handler.auth_wrapper)):
    users = service.get_all()
    return users


@router.get("/{id}")
def get_user(id: str, tokenUser=Depends(auth_handler.auth_wrapper)):
    print(tokenUser)
    user = service.get_by_id(id)
    return user


@router.post('/login')
def login(body=Body()):
    email = body["email"]
    password = body["password"]
    token = service.login(email, password)
    return {"token": token}


@router.post("/signup")
def create_user(body=Body()):
    firstName = body["firstName"]
    lastName = body["lastName"]
    email = body["email"]
    password = body["password"]
    user = service.signup(email, password, firstName, lastName)
    return user


@router.put("/{id}")
def update_user(id: str, body=Body()):
    user = service.update_by_id(id, body)
    return user


@router.delete("/{id}")
def delete_user(id: str):
    result = service.delete_by_id(id)
    return {"result": result}
