FROM python:3.8-slim-buster

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy

COPY main.py ./
CMD ["pipenv", "run", "python", "/main.py"]


