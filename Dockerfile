# FROM python:3.8-slim-buster
# # WORKDIR /
# ENV WORKON_HOME /root
# ENV PIPENV_PIPFILE /Pipfile

# # Install & use pipenv
# COPY Pipfile Pipfile.lock ./
# RUN python3 -m pip install --upgrade pip
# RUN apt-get update && apt-get install -y python3-pip
# RUN pip install pipenv
# ENV PIPENV_PIPFILE /Pipfile
# # RUN pipenv install PyGithub
# # RUN pip3 install PyGithub

# COPY main.py ./
# # CMD [ "python", "/main.py"]
# CMD ["pipenv", "run", "python", "/main.py"]
# # RUN pipenv run python main.py


FROM python:3

ENV WORKON_HOME /root
ENV PIPENV_PIPFILE /Pipfile

COPY main.py /
COPY Pipfile /
COPY Pipfile.lock /

# https://github.com/pypa/pipenv/issues/4273
RUN pip install 'pipenv==2018.11.26'
RUN pipenv install --deploy --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "python", "./main.py"]