from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from extensions import db
from models import User # 導入模型
from flask import jsonify

app = Flask(__name__)

# 設定資料庫 (使用 SQLite 進行示範)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 資料庫 & 遷移工具初始化
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return 'Hello, Flask-Migrate!'
    
if __name__ == '__main__':
    app.run(debug=True)

