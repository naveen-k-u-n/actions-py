# # Container image that runs your code
# FROM alpine:3.10

# # ADD script.py /
# # Copies your code file from your action repository to the filesystem path `/` of the container
# COPY script.py /script.py
# # COPY entrypoint.sh /entrypoint.sh

# # Code file to execute when the docker container starts up (`entrypoint.sh`)
# CMD ["python", "/script.py"]

# # ENTRYPOINT ["/entrypoint.sh"]

FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app requests

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/script.py"]