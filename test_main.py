
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

register_user_data={
  "email": "test@example.com",
  "username": "normal_user",
  "is_active": True,
  "role": "user",
  "password": "normal_user"
}
login_user_data={
  "username": "gujar",
  "password": "shahid"
}
login_user_admin_data={
  "username": "admin",
  "password": "admin"
}

movie_data={
  "popularity": 12,
  "director": "shahid",
  "genre": [
    "string","string1"
  ],
  "imdb_score": 23,
  "name": "shahid-gujar"
}
movie_update_data={
  "popularity": 8,
  "director": "Alfred Hitchcock",
  "genre": [
    "Horror"," Mystery"," Thriller"
  ],
  "imdb_score": 88,
  "name": "Psycho"
}

def get_access_token() -> str:
  response=client.post("/test-login",json=login_user_admin_data)
  # response=client.post("/test-login",json=login_user_data) #normal user
  access_token=response.json().get('access_token')
  return access_token


access_token=get_access_token()
headers={'Authorization':f'Bearer {access_token}'}

def test_register_user():
    response=client.post("/register",json=register_user_data)
    assert response.status_code == 201
   
    
def test_get_all_users_admin():
    response=client.get("/users",headers=headers)
    assert response.status_code == 200
 

def test_verify_user():
  url=f"/verify/{access_token}"
  response=client.get(url)
  assert response.status_code == 200
  


def test_login_user():
    response=client.post("/test-login",json=login_user_data)
    assert response.status_code == 200

def test_create_movie():
  response=client.post("/movies",json=movie_data,headers=headers)
  assert response.status_code == 201

def test_get_all_movie():
  response=client.get("/movies/")
  assert response.status_code == 200

def test_get_movie_by_name_movie():
  response=client.get("/movies/shahid-gujar",headers=headers)
  assert response.status_code == 200

def test_get_movie_by_name_anonymous():
  response=client.get("/movies/shahid-gujar")
  assert response.status_code == 200

def test_delete_movie_by_id():
  response=client.delete("/movies/2",headers=headers)
  assert response.status_code == 204
  
def test_update_movie_by_id():
  response=client.put("/movies/4",json=movie_update_data,headers=headers)
  assert response.status_code == 202




