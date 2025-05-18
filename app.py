from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    # In a real app, this would handle form submission
    return "https://forms.gle/LyRxD6ppe9NvfjPEA"

if __name__ == '__main__':
    app.run(debug=True)