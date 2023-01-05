FROM python:3.8-slim-buster

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pip install PyGithub
RUN pip install requests



WORKDIR /
COPY main.py ./
# CMD [ "python", "/main.py"]
CMD ["pipenv", "run", "python", "/main.py"]
# RUN pipenv run python main.py


# RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
