FROM python:3
RUN pip install Flask==1.1.1
COPY ./part3 .
CMD ["python" , "./MainScores2.py" , "--host" , "0.0.0.0"]
