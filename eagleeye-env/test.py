from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/eagleeye_db")

try:
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Connection successful:", result.fetchone())
except Exception as e:
    print("Connection failed:", e)
