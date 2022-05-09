FROM python:3.6.4-slim-jessie

RUN pip install json
RUN pip install CherryPy
RUN pip install tkinter
RUN pip install random
RUN pip install time
RUN pip install numpy
RUN pip install Pillow
COPY score.py .
COPY ws.py .
COPY game.py .
COPY movies.txt .
EXPOSE 8080
ENTRYPOINT ["python", "ws.py"]