## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
```
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable 

### Endpoints 
#### GET /categories
- Returns all categories and a success value
- Sample: `curl http://127.0.0.1:5000/categories`

``` {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```
#### GET /questions

- Returns a list of question objects, all categories, success value and total number of questions
- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions?page=1`

``` {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": "",
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": "2",
            "difficulty": 4,
            "id": 24,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Apollo 13",
            "category": "4",
            "difficulty": 5,
            "id": 44,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": "4",
            "difficulty": 5,
            "id": 45,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": "3",
            "difficulty": 5,
            "id": 46,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": "3",
            "difficulty": 6,
            "id": 47,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "4",
            "difficulty": 6,
            "id": 48,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "2",
            "difficulty": 4,
            "id": 49,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": "2",
            "difficulty": 3,
            "id": 50,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 51,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "2",
            "difficulty": 3,
            "id": 52,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 23
}
```
#### DELETE /questions/{questionid}
- Deletes the question of the given ID if it exists. Returns the id of the deleted question and a success value. 
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/66`
```
{
    "deleted_questionid": 66,
    "success": true
}
```

#### POST /questions
- Add a new question using the submitted question, answer, difficulty and category. Returns a success value. 
- `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Fun question", "answer":"Fun answer", "difficulty":"5", "category":"3"}'`
```
{
  "success": true
}
```

#### POST /questions
- Returns a list of question objects, success value and total number of questions if the question matches the given search word. 
- `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "which"}'`
```
{
    "current_category": "",
    "questions": [
        {
            "answer": "Brazil",
            "category": "3",
            "difficulty": 6,
            "id": 47,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "4",
            "difficulty": 6,
            "id": 48,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 51,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "2",
            "difficulty": 3,
            "id": 52,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": "1",
            "difficulty": 2,
            "id": 53,
            "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Jackson Pollock",
            "category": "2",
            "difficulty": 2,
            "id": 56,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "Scarab",
            "category": "4",
            "difficulty": 4,
            "id": 60,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "total_questions": 22
}
```

#### GET /categories/{categoryid}/questions
- Returns current category, total questions, success value and all questions based on the given category ID.
- Sample: `curl http://127.0.0.1:5000/categories/2/questions`

``` 
{
    "current_category": "Art",
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": "2",
            "difficulty": 4,
            "id": 24,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "George Washington Carver",
            "category": "2",
            "difficulty": 4,
            "id": 49,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": "2",
            "difficulty": 3,
            "id": 50,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "Agra",
            "category": "2",
            "difficulty": 3,
            "id": 52,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Jackson Pollock",
            "category": "2",
            "difficulty": 2,
            "id": 56,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
    ],
    "success": true,
    "total_questions": 22
}
```

#### POST /quizzes
- Returns random questions based on the given category if it exists and a success value. 
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category": {"id":"2", "type": "Art"}}'`
```
{
    "question": {
        "answer": "Jackson Pollock",
        "category": "2",
        "difficulty": 2,
        "id": 56,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    "success": true
}
```

