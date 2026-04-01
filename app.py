from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark():
    name = request.form['name']
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("attendance.txt", "a") as f:
        f.write(f"{name} - {date}\n")

    return f"Attendance Marked for {name}"

@app.route('/view')
def view():
    with open("attendance.txt", "r") as f:
        data = f.readlines()
    return "<br>".join(data)

if __name__ == "__main__":
    app.run(debug=True)
