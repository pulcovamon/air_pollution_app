FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5050

ENV DATABASE_URL="sqlite:///./db/air_quality.db"

CMD ["python", "main.py"]

