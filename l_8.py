from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def fst():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/carousel')
def carousel():
    return '''<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{}" />
                            <title>Отбор астронавтов</title>
                        </head>
                          <body>
                            <h1>Пейзажи Марса</h1>
                            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src={} width=300 height=300 alt="...">
    </div>
    <div class="carousel-item">
      <img src={} width=300 height=300 alt="...">
    </div>
    <div class="carousel-item">
      <img src={} width=300 height=300 alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</body>
</html>'''.format(url_for('static', filename='css/style.css'),
                  url_for('static', filename='img/mars_1.jpg'),
                  url_for('static', filename='img/mars_2.jpg'),
                  url_for('static', filename='img/mars_3.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')