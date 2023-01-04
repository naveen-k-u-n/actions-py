FROM python:3.8-slim-buster
WORKDIR /
# COPY main.py ./

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install
RUN pip install PyGithub
# RUN pipenv run python main.py

# WORKDIR /
COPY main.py ./
CMD [ "python", "/main.py"]
# RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
