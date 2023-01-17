FROM python:3.8-slim-buster

RUN python -m pip install --upgrade pip
# RUN apt-get install -y python3-pip
RUN pip install pipenv
COPY Pipfile ./
COPY main.py ./
RUN pipenv lock && pipenv --clear && pipenv --rm
RUN pipenv install PyGithub
#RUN pipenv install --system --deploy

RUN which python
Run python --version
Run pip --version
Run pipenv run pip list

CMD ["pipenv", "run", "python", "/main.py"]




