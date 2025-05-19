from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return redirect("https://forms.gle/LyRxD6ppe9NvfjPEA")

if __name__ == '__main__':
    app.run(debug=True)