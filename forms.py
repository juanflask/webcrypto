from wtforms import Form, StringField, EmailField, TextAreaField, SubmitField, DateTimeField, validators

class formulario(Form):
    name = StringField("name", [validators.Length(min=3, max=25)])
    email = EmailField("email", [validators.Length(min=3, max=25)])
    text = TextAreaField("Mensaje", [validators.Length(min=3, max=200)])

class form_crea_articulos(Form):
    titulo = StringField("titulo", [validators.Length(min=3, max=25)])
    autor = StringField("autor", [validators.Length(min=3, max=25)])
    articulo = TextAreaField("articulo")
    button = SubmitField("Enviar artículo")


