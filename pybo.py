from flask import Flask, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = './predict_image'
SPRINGBOOT_API_URL = "http://localhost:8080/predict"


@app.route('/predict', methods=['POST'])
def predict():
    # Java에서 보낸 파일이나 데이터를 받습니다.
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    #Todo 모델 추가해서 모델이 예측한 값 json으로 보내기

    file = request.files['file']
    # 파일을 처리하는 로직 (퍼스널 컬러 예측 등)

    # 예시: 처리 결과를 자바로 다시 보냅니다.
    result = {"예측한 결과": "결과값", "예측한 확률": 42.5}

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)