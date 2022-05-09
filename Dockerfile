FROM python:3.6.4-slim-jessie

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY score.py .
COPY ws.py .
COPY game.py .
COPY scores.txt .

EXPOSE 8080
ENTRYPOINT ["python", "ws.py"]