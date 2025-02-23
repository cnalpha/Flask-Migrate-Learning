from flask_sqlalchemy import SQLAlchemy

# 單獨創建資料庫實例 (避免循環匯入)
db = SQLAlchemy()
