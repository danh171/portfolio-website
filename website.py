from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Daniel Horrigan',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_created': 'Sunday, 19th April'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'This is a guest blog post',
        'date_created': 'Monday, 2nd April'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home")

@app.route('/projects')
def blog():
    return render_template("projects.html", posts=posts, title="Projects")

if __name__ == "__main__":
    app.run(debug=True)
 