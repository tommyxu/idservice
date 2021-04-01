FROM python:3.8
ENTRYPOINT ["./docker-entrypoint.sh", "-b", "0.0.0.0:8000"]
EXPOSE 8000
