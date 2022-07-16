from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, questions):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    qtns = [question.format() for question in questions]
    return qtns[start:end]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, DELETE"
        )
        return response


    @app.route("/categories")
    def get_categories():
        try:
            categoriesData = {}
            allCategories = Category.query.order_by(Category.id).all()
            for category in allCategories:
                categoriesData.update({category.id: category.type})

            return jsonify(
                {
                    "success": True,
                    "categories": categoriesData
                }
            )
        except:
            abort(422)    


    @app.route("/questions", methods=["GET"])
    def get_questions():
        categoriesData = {}
        allQuestions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, allQuestions)
        if len(current_questions) == 0:
            abort(404)

        allCategories = Category.query.order_by(Category.id).all()
        for category in allCategories:
            categoriesData.update({category.id: category.type})


        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(allQuestions),
                "categories": categoriesData,
                "current_category": ""
            }
        )    


    @app.route("/questions/<int:questionid>", methods=["DELETE"])
    def delete_question(questionid):
        question = Question.query.filter(Question.id == questionid).one_or_none()

        if question is None:
            abort(422)

        question.delete()

        return jsonify(
            {
                "success": True,
                "deleted_questionid": questionid
            }
        )

    
    @app.route("/questions", methods=["POST"])
    def add_search_questions():
        body = request.get_json()
        n_question = body.get("question")
        n_answer = body.get("answer")
        n_difficulty = body.get("difficulty")
        n_category = body.get("category")
        search = body.get("searchTerm")  

        try:
            if search:
                searchQuestions = Question.query.order_by(Question.id).filter(
                    Question.question.ilike("%{}%".format(search))
                )

                r_questions = [question.format() for question in searchQuestions]

                return jsonify(
                    {
                        "success": True,
                        "questions": r_questions,
                        "total_questions": len(Question.query.order_by(Question.id).all()),
                        "current_category": ""
                    }
                )
            else:
                questionObj = Question(question=n_question, answer=n_answer, category=n_category, difficulty=n_difficulty)
                questionObj.insert()

                return jsonify(
                    {
                        "success": True
                    }
                )

        except:
            abort(422)


    @app.route("/categories/<int:categoryid>/questions", methods=["GET"])
    def get_category_questions(categoryid):
        
        category = Category.query.filter(Category.id == categoryid).one_or_none()
        if category is None:
            abort(404)

        questions = Question.query.filter(Question.category == str(categoryid)).all()
        qtns = [question.format() for question in questions]
        
        return jsonify(
            {
                "success": True,
                "questions": qtns,
                "total_questions": len(Question.query.order_by(Question.id).all()),
                "current_category": category.type
            }
        )    

   
    @app.route("/quizzes", methods=["POST"])
    def question_quizzes():
        body = request.get_json()
        categoryData = body.get("quiz_category")
        p_questions = body.get("previous_questions")

        try:
            if(categoryData['id'] == 0):
                questions = Question.query.filter(Question.id.not_in(p_questions)).all()
            else:    
                questions = Question.query.filter(
                                            Question.category == str(categoryData['id'])
                                    ).filter(Question.id.not_in(p_questions)).all()
            
            randomQtnObj = random.choice(questions)
            return jsonify(
                {
                    "success": True,
                    "question": randomQtnObj.format()
                }
            )

        except:
            abort(422)


    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(405)
    def not_allowed(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )    

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

       

    return app

