from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String
import numpy as np


class Based(DeclarativeBase):
    pass


class News(Based):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic_id = Column(Integer)


class Topics(Based):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    topic = Column(String)


def add_news_to_storage(database: Session, text: str, topic_id: int):
    database.add(News(text=text, topic_id=topic_id))
    database.commit()


def get_news_by_topics(database:Session, topic_id: int):
    text = database.query(News).filter(News.topic_id == topic_id).all()

    if text is None:
        return

    texts = [x.text for x in text]
    if len(texts) == 0:
        return "I'm sorry there are none of the texts with this topic"
    else:
        idx = np.random.randint(0, len(texts)-1)
        
    return texts[idx]
