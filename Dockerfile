FROM python:3.8

RUN mkdir -p /app
WORKDIR /app

ADD ./build/release/app /app/

EXPOSE 8000
ENTRYPOINT ["./app", "-b", "0.0.0.0:8000"]
