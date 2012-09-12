from sqlalchemy import Column, Integer, String
from Flasktest.database import Base

class Entry(Base):
  __tablename__ = 'entry'
  id = Column(Integer, primary_key=True)
  title = Column(String(20), unique=False)
  text = Column(String(200), unique=False)

  def __init__(self, title=None, text=None):
	self.title = title
	self.text = text

  def __repr__(self):
	'<Entry %r>' % (self.title)
