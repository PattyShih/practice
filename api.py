from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "歡迎來到即時地圖系統"}

# 後端 API 準備寫在這裡