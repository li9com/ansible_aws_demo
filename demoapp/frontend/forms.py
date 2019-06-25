from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


exams = (
  ( 'linux', 'Linux Expert' ),
  ( 'docker', 'Docker Professional' ),
  ( 'ansible', 'Ansible Advanced' ),
  ( 'openshift', 'OpenShift Expert' )
)

class AddItemForm(FlaskForm):
  token = StringField('Token value', validators=[ DataRequired() ])
  initiator_email = StringField('Initiator email', validators=[ DataRequired() ])
  participant_email = StringField('Participant email', validators=[ DataRequired() ])
  participant_refid = StringField('Participant ref ID')
  exam_name = SelectField('Exam name', choices=exams)
  submit = SubmitField('Submit record')


class GetItemForm(FlaskForm):
  token = StringField('Enter token', validators=[ DataRequired() ])
  submit = SubmitField('Retrieve record')
  pass

