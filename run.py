
from flask import Flask, request

from app.translator import translate_doc

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the translator API.'

@app.route('/translate', methods=['GET'])
def translate():
    try:
        # Get the parameters from the query string
        source_file = request.args.get('source_file')
        source_lang = request.args.get('source_lang')
        target_lang = request.args.get('target_lang')
        target_file = request.args.get('target_file', '')

        if not source_file or not source_lang or not target_lang:
            return 'Invalid parameter, please check your input.', 400

        msg = translate_doc(source_file, source_lang, target_lang, target_file)

        return msg, 200

    except Exception as e:        
        return f'Error: {e}', 500
    

if __name__ == '__main__':    
    app.run('0.0.0.0', 8000, debug=True)