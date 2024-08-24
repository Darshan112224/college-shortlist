from flask import Flask, request, render_template # type: ignore
from database import create_database
from main import filter_colleges

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    max_tuition = request.form.get('max_tuition', type=float)
    min_acceptance_rate = request.form.get('min_acceptance_rate', type=float)
    location = request.form.get('location')
    program = request.form.get('program')
    
    results = filter_colleges(max_tuition, min_acceptance_rate, location, program)
    return render_template('results.html', colleges=results)

if __name__ == '__main__':
    create_database()  # Ensure database is created
    app.run(debug=True)
