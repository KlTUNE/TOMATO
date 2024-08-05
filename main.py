from flask import Flask, request, render_template, jsonify
import json

# natuki  登録してある人の名前一覧
# haruka
# takumi
# mei
# sora
# yuto
# ayaka
# kaito
# sakura
# tomo

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

with open('data.json','r', encoding="utf-8") as f:
    user_datas = json.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/get_song' , methods=['POST'])
def get_song():
    p_name = request.form.get('name', None)
    print (p_name)

    for user_data in user_datas:
        if user_data["name"] == p_name:
            return jsonify(user_data)
    return jsonify("not found")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True, port=8888)