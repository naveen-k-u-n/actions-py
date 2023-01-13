# FROM python:3.8-slim-buster

# ENV WORKON_HOME /github/home
# ENV PIPENV_PIPFILE /Pipfile

# COPY Pipfile Pipfile.lock ./
# RUN python -m pip install --upgrade pip
# # RUN apt-get install -y python3-pip
# RUN pip install pipenv

# COPY main.py ./
# CMD ["pipenv", "run", "python", "/main.py"]

# # CMD [ "python", "/main.py"]
# # RUN pipenv run python main.py


FROM python:3


COPY main.py ./
COPY Pipfile ./
COPY Pipfile.lock ./

ENV WORKON_HOME /root
ENV PIPENV_PIPFILE /Pipfile

# https://github.com/pypa/pipenv/issues/4273
# RUN pip install 'pipenv==2018.11.26'
# RUN pipenv install --deploy
RUN python -m pip install --upgrade pip
RUN pip install pipenv

ENTRYPOINT ["pipenv", "run", "python", "/main.py"]

