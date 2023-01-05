FROM python:3.8-slim-buster
RUN python -m pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pip install PyGithub
# WORKDIR /
# COPY main.py ./

# Install & use pipenv


RUN pipenv run python main.py


# RUN pipenv run python main.py

# WORKDIR /
# COPY main.py ./
# CMD [ "python", "/main.py"]
# RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
