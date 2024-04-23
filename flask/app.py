from flask import Flask, request, json

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/")
def hello_world_post():
    data:dict = request.get_json()
    nome = data.get("nome")
    return {"Nome":nome}


@app.put("/")
def hello_world_put():
    data:dict = request.get_json()
    nome = data.get("nome")
    return {"Nome atualizo":nome}

# app.run()