FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

COPY . .
RUN pip install -r ./requirements.txt

CMD ["python", "-m", "app"]
