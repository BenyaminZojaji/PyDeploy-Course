## ToDo App API
- This is an API for ToDo Application powered by FastAPI and SQLite to save tasks.

| ENDPOINT | REQUEST TYPE | REQUIRED PARAMETER | OPTIONAL PARAMETER | DESCRIPTION |
| --- | --- | --- | --- | --- |
| / | GET | - | - | Introduce the API |
| /task | GET | - | id | Return specific task by ID, if no ID is given then return all tasks |
| /task | POST | Task | Task.id, Task.time | Add new task |
| /task | PUT | id, Task | newTask.id, Task.time | Update existing task by ID |
| /task | DELETE | id | - | Delete a specific task by id |

</br>

## Facial Attribute Analyzer API
- This API uses the <a href='https://github.com/serengil/deepface'>Deepface</a> project as the main process for getting information from images and FastAPI to establish API."

| ENDPOINT | REQUEST TYPE | DESCRIPTION |
| --- | --- | --- |
| / | GET | Introduce the API |
| /facial_attribute_analyzer | POST | POST image and get facial attribute (eg. age, gender, race, etc) in result |

