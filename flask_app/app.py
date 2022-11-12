from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
   return "Hello, World!"

# For architecture https://medium.com/geekculture/how-to-architect-your-flask-rest-api-abf95637d9f5
# A tutorial https://codigofacilito.com/articulos/api-flask