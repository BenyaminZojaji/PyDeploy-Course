## Beginner APP
- In this project, I'm working with Sqlalchemy in FastAPI and SQLite database[^1].




## Expert App
- In this project, I'm working with Sqlalchemy in FastAPI and PostgreSQL database[^1] and then deploy the project to <a href="https://console.liara.ir">Liara</a>.
- Note that the tutorial[^1] that was mentioned is `one-to-many` relationship but since I replaced User and Items with Student and Course it's `many-to-many` relationship.

Run PostgreSQL locally:
```
docker run -p 5432:5432 --name [NAME] -e POSTGRES_PASSWORD=[PASSWORD] -e POSTGRES_USER=[USER] -e POSTGRES_DB=[DB_NAME] -d postgres
```
Note that you must add the URL in `database.py`:
```
SQLALCHEMY_DATABASE_URL = "postgresql://[USER]:[PASSWORD]@localhost:5432/[DB_NAME]"
```
![Untitled-2023-11-05-1710](https://github.com/BenyaminZojaji/PyDeploy-Course/assets/77120507/3e4788b6-8ebd-475f-9d78-6f765e3d6e3f)

usage:
```
uvicorn app.main:app --reload
```

[^1]: <a href="https://fastapi.tiangolo.com/tutorial/sql-databases">Tutorial Link</a>
