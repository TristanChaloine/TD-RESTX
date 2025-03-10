from flask_restx import Resource, Namespace

# Création du namespace, racine de tous les endpoints
ns = Namespace("api")

# Définition d’une route
@ns.route("/hello")  # Pas d'espace après les guillemets
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}
