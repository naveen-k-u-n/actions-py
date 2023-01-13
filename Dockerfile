FROM python:3.8-slim-buster

ENV WORKON_HOME /github/home
ENV PIPENV_PIPFILE /Pipfile

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
# RUN apt-get install -y python3-pip
RUN pip install pipenv

COPY main.py ./
CMD ["pipenv", "run", "python", "/main.py"]

# CMD [ "python", "/main.py"]
# RUN pipenv run python main.py

