
import json
from fastapi import HTTPException
from api.middlewares.auth import AuthHandler
from models.user import User

auth_handler = AuthHandler()


def get_all():
    users = User.objects().to_json()
    usersJson = json.loads(users)
    print(usersJson)
    return usersJson


def get_by_id(id):
    user = User.objects.get(id=id).to_json()
    userJson = json.loads(user)
    return userJson


def signup(email, password, firstName, lastName):

    hashed_password = auth_handler.get_password_hash(password)

    user = User(email=email, password=hashed_password,
                firstName=firstName, lastName=lastName)

    user.save()
    userJson = json.loads(user.to_json())
    return userJson


def login(email, password):
    user = User.objects(email=email).first()
    if user:
        isMatch = auth_handler.verify_password(password, user['password'])
        if (isMatch):
            token = auth_handler.encode_token(user)
            return token
        else:
            raise HTTPException(
                status_code=401, detail='Invalid username and/or password')
    else:
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')


def update_by_id(id, body):
    print(id)
    print(body)
    # Find document
    user = User.objects.get(id=id)

    # Update values
    user.firstName = body['firstName']
    user.lastName = body['lastName']

    user.save()
    userJson = json.loads(user.to_json())
    return userJson


def delete_by_id(id):
    result = User.objects(id=id).delete()
    return True if result else False
