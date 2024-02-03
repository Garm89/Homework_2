from flask import Flask, render_template, request, make_response, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']

    # Создаем куки файлы с именем и электронной почтой
    response = make_response(render_template(
        'output.html', name=name, email=email))
    response.set_cookie('name', name)
    response.set_cookie('email', email)

    return response


@app.route('/output')
def output():
    name = request.cookies.get('name')
    email = request.cookies.get('email')

    return render_template('output.html', name=name, email=email)


@app.route('/logout')
def logout():
    # Удаление данных пользователя из сессии
    session.clear()
    session.pop('name', None)
    session.pop('email', None)
    # Перенаправление на главную страницу или страницу входа
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
