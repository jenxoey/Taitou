from flask import Flask, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/run_py_file">点击这里运行 Python 文件</a>'

@app.route('/run_py_file')
def run_py_file():
    # 运行你的 Python 文件，这里假设你要运行的文件名为 example.py
    subprocess.Popen(["python", "code2_final.py"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)