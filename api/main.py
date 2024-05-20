from fastapi import FastAPI
from air_pollution import endpoints

app = FastAPI()
app.include_router(endpoints.router, prefix="/air_pollution_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)