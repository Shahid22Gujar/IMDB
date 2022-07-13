"""IMDB Project Using FastAPI and SQLite """
comand to run server => uvicorn main:app --reload
while register user=> username should be unique
test_main.py => file of testcase
pytest=> comand all run all testcase at once
to run specific function test => pytest -k test_function_name
eg:pytest test_get_movie_by_name_anonymous =>testcase without authentication

<===========Oveflow================>

User=register,verify,login
Movie
=>Read(By All User)=>Return data only upto 100
=>Search(By All User)
=>Update(By Admin Only)
=>Create(By Admin Only)
=>Delete(By Admin Only)
