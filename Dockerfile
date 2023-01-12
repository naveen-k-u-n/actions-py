FROM python:3.8-slim-buster
WORKDIR /

# Install & use pipenv
#COPY Pipfile Pipfile.lock ./
RUN python3 -m pip install --upgrade pip
RUN apt-get update && apt-get install -y python3-pip
RUN pip install pipenv
RUN pipenv install PyGithub
# RUN pip3 install PyGithub

COPY main.py ./
# CMD [ "python", "/main.py"]
CMD ["pipenv", "run", "python", "/main.py"]
# RUN pipenv run python main.py