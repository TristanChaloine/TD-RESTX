from flask_restx import *
from .api_models import *
from .models import *

# Création du namespace, racine de tous les endpoints
ns = Namespace("api")

# Définition d’une route
@ns.route("/hello")  # Pas d'espace après les guillemets
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}

@ns.route("/articles")
class ArticleCollection(Resource):
    @ns.marshal_list_with(article_model)
    def get(self):
        return get_all_articles()
    
    @ns.expect(article_input_model)
    @ns.marshal_with(article_model)
    def post(self):
        article = create_article(title=ns.payload["title"], content=ns.payload["content"])
        return article,201
    
    

@ns.route("/articles/<int:id>")
@ns.response(404, "Article not found")
class ArticleItem(Resource):
    @ns.marshal_with(article_model)
    def get(self, id):
        """Récupère un article par son ID."""
        article = get_article(id)
        if article is None:
            abort(404, "Article not found")
        return article
    
    ns.expect(article_input_model)
    @ns.marshal_with(article_model)
    def put(self, id):
        article = modify_article(id, ns.payload["title"], content=ns.payload["content"])
        if article is None:
            abort(404, "Article not found")
        return article, 200
    
    @ns.marshal_with(article_model)
    def delete(self, id):
        article = delete_article(id)
        if article is None:
            abort(404, "Article not found")
        return article, 204

    
@ns.route("/comments")
class CommentCollection(Resource):
    @ns.marshal_list_with(comment_model)
    def get(self):
        return get_all_comments()
    
    @ns.expect(comment_input_model)
    @ns.marshal_with(comment_model)
    def post(self):
        if get_article(ns.payload["article_id"]) is None:
            abort(404, "Article not found") 
        comment = create_comment(content=ns.payload["content"], article_id=ns.payload["article_id"])
        return comment,201
    
@ns.route("/comments/<int:id>")
@ns.response(404, "Comment not found")
class CommentItem(Resource):
    @ns.marshal_with(comment_model)
    def get(self, id):
        """Récupère un commentaire par son ID."""
        comment = get_comment(id)
        if comment is None:
            abort(404, "Comment not found")
        return comment
    
    ns.expect(comment_input_model)
    @ns.marshal_with(comment_model)
    def put(self, id):
        comment = modify_comment(id, ns.payload["content"])
        if comment is None:
            abort(404, "Comment not found")
        return comment, 200
    
    @ns.marshal_with(comment_model)
    def delete(self, id):
        comment = delete_comment(id)
        if comment is None:
            abort(404, "Comment not found")
        return comment, 204
    
@ns.route("/articles/<int:id>/comments")
class ArticleCommentCollection(Resource):
    @ns.marshal_list_with(comment_model)
    def get(self, id):
        article = get_article(id)
        if article is None:
            abort(404, "Article not found")
        return article.comments
    
    @ns.expect(comment_input_model)
    @ns.marshal_with(comment_model)
    def post(self, id):
        article = get_article(id)
        if article is None:
            abort(404, "Article not found")
        comment = create_comment(content=ns.payload["content"], article_id=id)
        return comment,201