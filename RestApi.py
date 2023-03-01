from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import db
app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록



@api.route('/route_info')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def post(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        results=db.readsql("SELECT id,route_name,route,travel_time,Enterprise_name FROM route_info")
        
        return {'results':[{'id':result[0],'route_name':result[1],'route':result[2],'travel_time':result[3],'Enterprise_name':result[4]} for result in results]}
            

        





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5544)
