import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

database_path = os.environ["DATABASE_URL"]
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def rollback():
    db.session.rollback()


class Questions(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    question_field = db.Column(db.String())
    answers = db.Column(db.String())
    grade = db.Column(db.String())
    tags = db.Column(db.String())
    subject = db.Column(db.String())
    puplish_date = db.Column(db.DateTime())


    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "question_field": self.question_field,
            "answers": self.answers,
            "grade": self.grade,
            "tags": self.tags,
            "subject": self.subject,
            "puplish_date": self.puplish_date
            }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
