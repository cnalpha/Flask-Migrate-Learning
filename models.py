from extensions import db  # 改成從 extensions 匯入 db
from datetime import datetime

# 建立一個簡單的 User 資料庫模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 新增的欄位
    
    def __repr__(self):
        return f'<User {self.name}>'
