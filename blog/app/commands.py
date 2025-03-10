from .extensions import db
from .models import Article, Comment
from .myapp import app

@app.cli.command()
def syncdb():
    """Synchronise la base de données et insère des données initiales."""
    
    # Création des tables si elles n'existent pas
    db.create_all()

    # Suppression des anciennes données pour éviter les doublons
    db.session.query(Article).delete()
    db.session.query(Comment).delete()
    
    # Ajout de nouveaux articles
    article1 = Article(title="Premier Article", content="Ceci est mon premier article.")
    article2 = Article(title="Second Article", content="Ceci est mon second article.")

    db.session.add(article1)
    db.session.add(article2)
    db.session.commit()  # On commit ici pour s'assurer que les articles ont un ID

    # Ajout de commentaires associés aux articles
    comment1 = Comment(content="Super article", article_id=article1.id)
    comment2 = Comment(content="Merci pour l'article", article_id=article2.id)

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.commit()

    print("Base de données synchronisée avec succès et données initialisées !")
