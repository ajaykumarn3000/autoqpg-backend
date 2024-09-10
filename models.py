from sqlalchemy import Column, Integer, String, ARRAY, LargeBinary

from database import Base, engine


class Question(Base):
    __tablename__ = 'questions'

    qid = Column(Integer, primary_key=True, autoincrement=True)
    serial_no = Column(Integer)
    subject = Column(String)
    para = Column(ARRAY(String))
    image = Column(ARRAY(LargeBinary))
    co = Column(Integer)
    bl = Column(Integer)
    marks = Column(ARRAY(Integer))
    count = Column(Integer)


# Create all tables (if not already present)
Base.metadata.create_all(engine)
