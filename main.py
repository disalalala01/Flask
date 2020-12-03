from app import app
#импортировал так как надо было использовать фдаск а вызвал и использовал я этот класс в папке app
from app import db
from posts.blueprint import posts
import view



app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':                #чтобы в общем запустить сайт и запустить сервере фласк
    app.run()                       #app это переменная на которую мы привизали
