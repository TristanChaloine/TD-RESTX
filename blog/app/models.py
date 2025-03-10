from .extensions import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    
    # Relation avec Comment
    comments = db.relationship("Comment", back_populates="article", cascade="all, delete-orphan")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    
    # Clé étrangère vers Article
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
    
    # Relation avec Article
    article = db.relationship("Article", back_populates="comments")
