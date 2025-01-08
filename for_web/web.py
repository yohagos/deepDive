# Python for Web
# Python is a general purpose programming language and it can be used for many places.
# In this section, we will see how we use Python for the web. There are many Python web
# frame works. Django and Flask are the most popular ones. Today, we will see how to
# use Flask for web development.


# Flask
#
# Flask is a web development framework written in Python. Flask uses Jinja2 template engine.
# Flask can be also used with other modern front libraries such as React.
#
# If you did not install the virtualenv package yet install it first. Virtual environment
# will allows to isolate project dependencies from the local machine dependencies.

from flask import Flask, render_template, request, redirect, url_for
import os

from matplotlib.pyplot import title

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)








