import os
from flask import Flask, request, abort, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from forms import QuestionForm
import os
from models import Questions, setup_db, rollback



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def index():
  	return render_template('pages/home.html')

  @app.route('/questions/1')
  def show_question():
    return render_template('pages/show_question.html')

  @app.route('/questions/create')
  def create_question_form():
  	form = QuestionForm()
  	return render_template('forms/new_question.html', form= form)

  @app.route('/questions/search',methods=['POST'])
  def search_questions():
    search_term = request.form.get('search_term','')
    results = Questions.query.filter(Questions.title.ilike(f'%{search_term}%'))

    response = results
    return render_template('pages/search_questions.html',results = response)

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)