FROM python:3.6-alpine
ADD src/requirements.txt /requirements.txt
RUN apk --no-cache add libpq jpeg-dev zlib-dev \
  && apk --no-cache add --virtual build-dependencies postgresql-dev build-base libffi-dev libressl-dev \
#  && pip install -U pip setuptools \
  && LIBRARY_PATH=/lib:/usr/lib pip install -b /tmp --no-cache-dir -r /requirements.txt \
  && apk del build-dependencies

ENV PYTHONUNBUFFERED 1

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD ./src /code/

# uWSGI will listen on this port
EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=project.settings


CMD ["gunicorn", "-c", "/code/project/gunicorn.py", "project.wsgi"]
