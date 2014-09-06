#-*-coding:utf8-*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return u"InnoMVA: 주식회사 이노지투비"

if __name__ == "__main__":
    app.run()