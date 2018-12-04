# Import flask with the requests object
from flask import Flask, request

# Create the web server
app = Flask(__name__)

# This bot lols at every thing it gets sent!
def lol_bot():
    text = request.form.get('text')
    return f'lol {text}'

# You can message lol_bot via <your website>/lol
app.route('/lol', methods=['GET', 'POST'])(lol_bot)
