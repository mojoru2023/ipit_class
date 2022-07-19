
from flask import Flask,render_template
app = Flask(__name__)#修改静态文件夹的目录


@app.route('/')
def home():
    return render_template('index.html')#homepage.html在static文件夹下


if __name__ == "__main__":
    app.run(debug=True)
