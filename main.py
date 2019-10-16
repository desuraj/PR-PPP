#c:/Users/De_Suraj/flaskDemo/env/Scripts/activate.bat
print("hello")
# import flask
# print("flask.__version__")
#import pandas
from flask import Flask,render_template,request, redirect, url_for
import apriori
import showitem
import pos
project = Flask(__name__)


@project.route('/')
def menu():
    return render_template('layout.html')


@project.route('/contact/')
def contact():
    return render_template('contact.html')

@project.route('/about/')
def about():
    return render_template('about.html')

@project.route('/pos1/', methods =['GET','POST'])
def pos1():
    if request.method == 'POST':
        p_name1 = request.form['p_name1']
        l = pos.f3(p_name1)
        print("type of l")
        print(type(l))
        return render_template('matrix.html',p_name1 = p_name1, l= l)
    else:
        return render_template('pos1.html')

@project.route('/show/', methods =['GET','POST'])
def show():
    if request.method == 'POST':
        p_name = request.form['p_name']
        s = showitem.f2(p_name)
        print("typeof s")
        print(type(s))
       # print(s[:4])
        # return ("YOU SELECT THE PRODUCT : %s  _____________AND YOU CAN ALSO BUY :  %s"%(p_name.upper()," ,".join(s)))
        return render_template('display.html', p_name=p_name, s = s)
    else:
        return render_template('main.html')


if __name__ == '__main__':
    project.run(debug = True)