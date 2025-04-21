from fastapi import FastAPI
import uvicorn

def main():
    print("Hello from uv-concepts!")
    uvicorn.run(app, host="127.0.0.1", port=8008)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello uv Code!"}

if __name__ == "__main__":
    main()
