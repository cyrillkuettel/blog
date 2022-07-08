FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

WORKDIR /code

COPY .fast/app/requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# because we're not using nginx in local build, copy the directory instead of using volumes.
# COPY ./app /code/app

ENV MODULE_NAME="app.main"
ENV VARIABLE_NAME="app"
ENV PORT="8000"
ENV BIND="0.0.0.0:8000"
