from flask import Flask
app = Flask(__name__)

"""路由参数or接口名称"""
@app.route('/')
def say_hello():
    return 'hello Word +str(a) '

if __name__=="__main__":
    app.run(debug=True)
""" debug：调试模式，设置为true的时候改动代码Ctrl+s会自动生效不用重新启动
    host：地址，监听
    port：端口
"""