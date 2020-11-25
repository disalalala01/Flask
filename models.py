from app import db #импорт склалкхими
from datetime import datetime #для таблицы керек нарсе ол
import re #чтобы норм слаги делать параметры ставим какие слаги можно какие нельзя


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s) #тут указывается что меняем переменная патерн на что на дифисы и на патрны мы указали что меняем пробелы потом меняем с помощью локальной переменной что мы передали снизу когда вызывали этот класс

class Post(db.Model):#создаетм таблицу
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now() ) #время тут

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):#генерировать ссылки еогда мы пишем тайтл то то все идет в ссылку но это сылка через слаги фай редактируется убирается пробелы и заменяются дифизами
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):#чтобы нормально создавалась таблица и можно было понимать его
        return '<Post id:{}, title: {}>'.format(self.id, self.title)
