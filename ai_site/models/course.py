import enum

from ai_site import db


class Years(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6


class Semesters(enum.Enum):
    FIRST = 1
    SECOND = 2


class CourseRelationship(db.Model):
    one_course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    other_course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

    def __repr__(self):
        return f"CourseRelationship('{self.one_course_id}', '{self.other_course_id}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Enum(Years), default=Years.FIRST)
    semester = db.Column(db.Enum(Semesters), default=Semesters.FIRST)

    def __repr__(self):
        return f"Course('{self.name}', '{self.credits}', '{self.year}', '{self.semester}')"
