from flask import render_template, Blueprint, current_app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    current_app.logger.info('Отрисовка шаблона главной страницы')
    return render_template('index.html')

@main.route('/board')
def board():
    current_app.logger.info('Отрисовка шаблона телефонной книги')
    return render_template('board.html')
