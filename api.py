from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "歡迎來到即時地圖系統"}


@app.get("/events")
def get_all_events():
    return {"events": ["圖書館沒位子了", "學餐大排長龍"]}
#要寫甚麼其他的 API 嗎？例如新增事件、刪除事件等等？@app.post("/events")
def create_event(event: str):           
    # 這裡可以加入邏輯來儲存事件，例如存到資料庫或是暫存列表
    return {"message": f"事件 '{event}' 已新增"}                            

# 後端 API 準備寫在這裡

@app.get("/nearby")
def get_nearby_users():
    return {"nearby_count": 5, "radius": "500m"}

@app.get("/events")
def get_all_events():
    return {"events": ["圖書館沒位子了", "學餐大排長龍"]}

