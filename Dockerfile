FROM python:3.8-slim-buster
WORKDIR /

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
# RUN pip install PyGithub

# WORKDIR /
COPY test.py ./
CMD [ "python", "/test.py"]
