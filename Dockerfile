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