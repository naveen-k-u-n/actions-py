# Container image that runs your code
FROM alpine:3.10

# ADD script.py /
# Copies your code file from your action repository to the filesystem path `/` of the container
COPY script.py /script.py
# COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD ["python", "/script.py"]

# ENTRYPOINT ["/entrypoint.sh"]