from fastapi import FastAPI


from api.router import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")

@app.get("/")
def main():
    """At root you find this message"""
    return {"message": "Hello from backend!"}

