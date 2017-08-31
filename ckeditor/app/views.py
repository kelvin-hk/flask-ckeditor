from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ckedit import CKTextAreaField, CKTextAreaWidget

from models import TestTest


"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


class TestMView(ModelView):
  datamodel = SQLAInterface(TestTest)
  add_template = 'ckadd.html'
  edit_template = 'ckedit.html'

  add_form_extra_fields = {
    'content': CKTextAreaField('Content')
  }
  edit_form_extra_fields = {
    'content': CKTextAreaField('Content')
  }

  add_columns = ['content']
  edit_columns = ['content']
  list_columns = ['content']
  show_columns = ['content']




"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

appbuilder.add_view(TestMView, "Test Test", label=("test test"), icon="fa-folder-open-o",
  category="Test", category_label=('test test'),  category_icon='fa-users')



