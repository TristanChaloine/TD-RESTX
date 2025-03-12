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

def get_all_articles():
    return Article.query.all()

def get_article(id) :
    return Article.query.get(id)

def get_all_comments():
    return Comment.query.all()

def get_comment(id) :
    return Comment.query.get(id)

def create_article(title, content) :
    article = Article(title=title, content=content)
    db.session.add(article)
    db.session.commit()
    return article

def create_comment(content, article_id) :
    comment = Comment(content=content, article_id=
    article_id)
    db.session.add(comment)
    db.session.commit()
    return comment

def modify_article(id, title, content) :
    article = get_article(id)
    if article is None:
        return None
    if title is not None:
        article.title = title
    if content is not None:
        article.content = content
    db.session.commit()
    return article

def modify_comment(id, content) :
    comment = get_comment(id)
    if comment is None:
        return None
    comment.content = content
    db.session.commit()
    return comment

def delete_article(id) :
    article = get_article(id)
    if article is None:
        return None
    db.session.delete(article)
    db.session.commit()
    return article

def delete_comment(id) :
    comment = get_comment(id)
    if comment is None:
        return None
    db.session.delete(comment)
    db.session.commit()
    return comment 
