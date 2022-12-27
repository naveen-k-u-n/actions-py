FROM python:3.8-slim-buster
WORKDIR /

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy
# RUN pipenv run python

# WORKDIR /
COPY main.py ./
CMD [ "python", "/main.py"]
