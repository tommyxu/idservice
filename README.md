# idservice

`ID-Service` is a distributed ID generator microservice based on FastAPI.

## Installation

```sh
pip3 install idservice
```

## Start Service

```sh
idservice-start
```

> List all available `Gunicorn` options by `idservice-start --help`

## API Endpoint

Several endpoints:

-   `/id/snowflake`
-   `/id/random/64`
-   `/id/uuid`

Browse `/docs` (default to http://localhost:8000/docs) to read all APIs.

## Configuration

Environment variable:

| Environment Vars        | Usage                                  | Default |
| ----------------------- | -------------------------------------- | ------- |
| `ID_SERVICE_MACHINE_ID` | Snowflake Machine ID (10 bits integer) | Random  |
