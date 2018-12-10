# Import flask with the requests object
from flask import Flask, request, jsonify

# Create the web server
app = Flask(__name__)

# You can message lol_bot via <your website>/lol
@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
	# This bot lols at every thing it gets sent!
    text = request.form.get('text')
    return jsonify({
		'response_type': 'in_channel',
		'text': f'lol {text}',
	})

if __name__ == '__main__':
	app.run()
