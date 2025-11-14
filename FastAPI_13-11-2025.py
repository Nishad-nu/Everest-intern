from fastapi import FastAPI

app = FastAPI()


@app.post("/data")
def read_root(data: dict):
    print(">>>>>>>>>>>>>",data)
    return data