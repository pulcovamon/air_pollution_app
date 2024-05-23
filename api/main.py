from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from air_pollution import endpoints

app = FastAPI()
app.include_router(endpoints.app, prefix="/air_pollution_api")

# setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)