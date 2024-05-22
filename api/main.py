from fastapi import FastAPI
import uvicorn

from air_pollution import endpoints

app = FastAPI()
app.include_router(endpoints.app, prefix="/air_pollution_api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5050)