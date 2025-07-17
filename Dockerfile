FROM python:3.12-bullseye AS base
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

RUN mkdir /code

WORKDIR /code

COPY requirements.txt requirements.prod.txt ./

FROM base as development

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

COPY . .

EXPOSE 8000


ENTRYPOINT ["/code/on-start-django.sh"]

FROM base AS production

RUN pip install --no-cache-dir -r requirements.prod.txt

COPY . .

EXPOSE 8000


ENTRYPOINT ["/code/on-start-django.sh"]