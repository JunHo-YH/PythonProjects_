from flask import Flask
app = Flask(__name__) #__name__이라는 변수는 모듈의 이름이 저장된다.
                      # 실행하는 코드에서는 __main__값이 들어간다.
                      # 현재 위치를 flask객체에 알려준다.

@app.route('/hello')  # hello로 접속시 아래 함수 실행
def hello():
    return "<h1>Hello Flask!</h1>" # 출력

if __name__ == "__main__":     # 모듈이 아니라면 웹서버를 실행해라
                               # 모듈을 import해서 사용하는 경우인지 직접 실행한 경우인지를 구분하기 위한 것
                               # 이 name이 main이라는 값을 가지게 되면 해당 모듈이 주 프로그램이라는 소리고,
                               # 해당 모듈을 실행시키지 않고 import했을때는 모듈 이름이name으로 들어가게 된다는 의미이다.
    app.run(host="127.0.0.1", port=6060, debug=True)