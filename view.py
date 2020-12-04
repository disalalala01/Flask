from app import app
from flask import render_template #это чтобы мы могли иметь доступ на шаблоны



#шаблоны нужны для того чтобы было человеку видно
# @app.route('/')#начальная страница будет возвращять хелло уорл а слэш это просто путь начальный
# def index():
#     return '<h1>Hello World</h1>'
@app.route('/')
def index():
    # name = 'Alish'
    return render_template('index.html')#мы вызвали рендер темплейт чтобы он смог индекс воспроизвести а вот откуда он найдет индекс мы указали снизу
                                         #n=name это мы присваеваем переменную с этого файла на шаблон с шаблона на сайт сам переменная пишется рядом с надписью с {{ n }} такими скобками

@app.errorhandler(404)        
def page_not_found(e):
    return render_template('404.html'), 404
