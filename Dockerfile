FROM python:3.6.5
RUN pip install pipenv
WORKDIR /app
COPY Pipfile* /app/
COPY main.py /app/
RUN pipenv install --system

CMD ["pipenv", "run", "python", "/app/main.py"]




