import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "OK", "service": "kong-gateway-app"}


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
