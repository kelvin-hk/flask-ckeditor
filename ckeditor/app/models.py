from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, UnicodeText
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
class TestTest(Model):
    __tablename__ = 'test_test'
    id = Column(Integer, primary_key=True)
    content= Column(UnicodeText, nullable=True)

    def __repr__(self):
      return self.id

