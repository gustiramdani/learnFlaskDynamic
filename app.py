from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bogor',
        'salary': '10.000.000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bandung',
        'salary': '12.000.000'
    },
    {
        'id': 3,
        'title': 'Frontend',
        'location': 'Jakarta',
        'salary': '4.000.000'
    },
    {
        'id': 4,
        'title': 'DevOps',
        'location': 'Bekasi',
        'salary': '10.000.000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)