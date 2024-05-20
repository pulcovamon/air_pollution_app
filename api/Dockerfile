FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

ENV DATABASE_URL="sqlite:///./db/air_quality.db"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

