from flask import Flask, jsonify
from main import app, con

@app.route('/livro',methods=['GET'])
def get_livro():
    cur = con.cursor()
    cur.execute("select id_livro, titulo, autor, ano_publicacao from livro")
    livros = cur.fetchall()
    livros_dic = []
    for livro in livros:
        livros_dic.append({
            'id_livro': livro[0],
            'titulo': livro[1],
            'autor': livro[2],
            'ano_publicacao': livro[3]
        })
        return jsonify(mensagem='listas de livros', livros=livros_dic)