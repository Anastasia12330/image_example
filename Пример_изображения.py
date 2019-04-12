from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет, Яндекс! Я - Настя</h1>"


@app.route('/image_sample')
def image_sample():
    return '''<h1>Привет, Яндекс! Смотри картинку</h1>, <img src="{}", alt="здесь должна была быть картинка,
        но не нашлась">'''.format(url_for('static', filename='img/Риана.jpg'))


if __name__ == '__main__':
    app.run(port=8010, host='127.0.0.1')