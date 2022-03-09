from wtforms import Form, StringField, EmailField, TextAreaField, validators

class formulario(Form):
    name = StringField("name", [validators.Length(min=3, max=25)])
    email = EmailField("email", [validators.Length(min=3, max=25)])
    text = TextAreaField("Mensaje", [validators.Length(min=3, max=200)])



