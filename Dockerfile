# # Container image that runs your code
# FROM alpine:3.10

# # ADD script.py /
# # Copies your code file from your action repository to the filesystem path `/` of the container
# COPY script.py /script.py
# # COPY entrypoint.sh /entrypoint.sh

# # Code file to execute when the docker container starts up (`entrypoint.sh`)
# CMD ["python", "/script.py"]

# # ENTRYPOINT ["/entrypoint.sh"]

################# two ##############

# FROM python:3-slim AS builder
# ADD . /app
# WORKDIR /app

# # We are installing a dependency here directly into our app source dir
# RUN pip install --target=/app requests

# # A distroless container image with Python and some basics like SSL certificates
# # https://github.com/GoogleContainerTools/distroless
# FROM gcr.io/distroless/python3-debian10
# COPY --from=builder /app /app
# WORKDIR /app
# ENV PYTHONPATH /app
# CMD ["/app/script.py"]



#######################  three #############################

# #Deriving the latest base image
# FROM python:latest

# # ADD . /app
# # WORKDIR /app
# # ENV PYTHONPATH /app
# # CMD ["/app/script.py"]

# #to COPY the remote file at working directory in container
# COPY script.py ./
# # Now the structure looks like this '/usr/app/src/test.py'


# #CMD instruction should be used to run the software
# #contained by your image, along with any arguments.

# CMD [ "python", "/script.py"]

###################################
FROM python:3.8-slim-buster
WORKDIR /
RUN pip install --target=/
COPY script.py ./
CMD [ "python", "/script.py"]
