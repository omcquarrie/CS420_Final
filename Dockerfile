FROM python:3.8

RUN pip --disable-pip-version-check

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY score.py .
COPY ws.py .
COPY game.py .
COPY scores.txt .

EXPOSE 8080
ENTRYPOINT ["python", "ws.py"]