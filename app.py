from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi
import pandas as pd
import os

TITULO = os.getenv("TITULO")

app = Flask(__name__)
class Livro:
    def __init__(self, titulo, autor, categoria, ano, editora='Sem editora'):
        self.Titulo = titulo
        self.Autor = autor
        self.Categoria = categoria
        self.Ano = ano
        self.Editora = editora
        self.Ativo = False

@app.route("/inicio")
def home():
    df = pd.read_csv("tabela - livros.csv")
    lista_de_livros = []
    for index, row in df.iterrows():
        livro = Livro(
            row["Titulo do Livro"],
            row["Autor"],
            row["Categoria"],
            row["Ano de Publicação"],
        )
        lista_de_livros.append(livro)
# lista = df["Titulo do Livro"].tolist()
    return render_template("lista.html", titulo=TITULO, lista_de_livros=lista_de_livros)

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run()