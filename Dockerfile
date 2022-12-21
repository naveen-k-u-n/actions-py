FROM python:3.8-slim-buster
WORKDIR /
RUN pip install requests
COPY script.py ./
CMD [ "python", "/script.py"]
