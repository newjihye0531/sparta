from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/myshop', methods=['POST'])
def write_review():
    info1 = request.form['info1']
    exampleFormControlSelect1 = request.form['exampleFormControlSelect1']
    info2 = request.form['info2']
    info3 = request.form['info3']

    ordered_dict = {
        'info1': info1,
        'exampleFormControlSelect1' : exampleFormControlSelect1,
        'info2': info2,
        'info3': info3
    }
    print(ordered_dict)

    db.myshop.insert_one(ordered_dict)

    return jsonify({'result':'success', 'msg': '주문정보가 잘 저장되었습니다'})


@app.route('/myshop', methods=['GET'])
def read_reviews():
    stored_reviews =  list(db.myshop.find())
    myshop = []

    for stored_review in stored_reviews:
        myshop.append({
            'info1': stored_review['info1'],
            'exampleFormControlSelect1' : stored_review['exampleFormControlSelect1'],
            'info2': stored_review['info2'],
            'info3': stored_review['info3']
        })
    print(myshop)



    return jsonify({'result':'success', 'msg': '잘 연결되었음!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)