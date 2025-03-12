from flask_restx import fields
from .extensions import api  # Assurez-vous que `api` est bien défini dans votre app

article_model = api.model("Article", {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "uri": fields.Url("api_article_item", absolute=True)
})

comment_model = api.model("Comment", {
    "id": fields.Integer,
    "content": fields.String,
    "article_id": fields.Integer,
    "uri": fields.Url("api_comment_item", absolute=True)
})

article_input_model = api.model("ArticleInput", {
    "title": fields.String,
    "content": fields.String
})

comment_input_model = api.model("CommentInput", {
    "content": fields.String,
    "article_id": fields.Integer
})