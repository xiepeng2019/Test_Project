# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/09/06

from flask import Flask
import logging
import redirect

logging .basicConfig(level=logging.INFO ,format='%(asctime)-16s %(levelname)-8s %(message)s')

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'hello admin'

@app.route('/guest')
def hello_guest():
    return 'hello guest'

@app.route('/user/<name>')
def hello_user(name):
    logging.info("[name is]:{}.format(name)")
    if name == 'admin':
        #重定向
        return redirect("http://127.0.0.1:5000/admin")
    if name == 'guest':
        return redirect("http://127.0.0.1:5000/guest")
    else:
        return redirect("http://www.baidu.com")

if __name__=="__main__":
    app.run(debug=True)