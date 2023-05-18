from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.rvfdb4x.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/memberlist", methods=["POST"])
def memberlist_post():
    name_receive = request.form['name_give']
    pros_receive = request.form['pros_give']
    blog_receive = request.form['blog_give']
    mbti_receive = request.form['mbti_give']
    selso_receive = request.form['selso_give']
    coworkst_receive = request.form['coworkst_give']

    doc = {
        'name': name_receive,
        'pros': pros_receive,
        'blog': blog_receive,
        'mbti': mbti_receive,
        'selso': selso_receive,
        'coworkst': coworkst_receive
    }
    db.members.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route("/memberlist", methods=["GET"])
def memberlist_get():
    all_members = list(db.members.find({}, {'_id': False}))
    return jsonify({'result': all_members})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
