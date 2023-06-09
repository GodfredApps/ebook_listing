from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

ebooks = [
    {
        'title': 'Book 1',
        'author': 'Author 1',
        'description': 'This is the description of Book 1.',
        'price': 9.99
    },
    {
        'title': 'Book 2',
        'author': 'Author 2',
        'description': 'This is the description of Book 2.',
        'price': 14.99
    },
    {
        'title': 'Book 3',
        'author': 'Author 3',
        'description': 'This is the description of Book 3.',
        'price': 19.99
    }
]

@bp.route('/')
def index():
    return render_template('index.html', ebooks=ebooks)
