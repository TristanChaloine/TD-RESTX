from flask_restx import fields
from .extensions import api  # Assurez-vous que `api` est bien défini dans votre app

article_model = api.model("Article", {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String
})
