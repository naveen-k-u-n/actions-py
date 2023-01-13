FROM python:3.8-slim-buster

COPY Pipfile Pipfile.lock ./
RUN python3 -m pip install --upgrade pip
RUN apt-get install -y python3-pip
RUN pip install pipenv
ENTRYPOINT ["echo $GITHUB_SHA"]

COPY main.py ./
CMD ["pipenv", "run", "python", "/main.py"]

# CMD [ "python", "/main.py"]
# RUN pipenv run python main.py

