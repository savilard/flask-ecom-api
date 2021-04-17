# Api delivery service

<p align="center">
    <img width="500"
         src="https://www.business.ru/images/001/2-43.jpg"
         alt="Books library restyle" />
</p>

## Description
![Platform](https://img.shields.io/badge/platform-linux-brightgreen)
![Python_versions](https://img.shields.io/badge/Python-3.7%7C3.8-brightgreen)
![GitHub](https://img.shields.io/github/license/velivir/books-library-restyle)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


The repository contains the api for the delivery service.

Technologies used:
- Python
- Flask
- Postgresql
- Docker


## Table of content

- [Installation](#installation)
- [How to run](#how-to-run)
- [License](#license)


## Installation

* Install [Poetry](https://python-poetry.org/), make and [Direnv](https://direnv.net/);
* Register to  [Elephantsql](https://www.elephantsql.com/), create a database;
* Clone github repository:
```bash
git clone https://github.com/savilard/flask-ecom-api
```
* Go to folder with project:
```bash
cd flask-ecom-api
```

## How to run
* Install [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/);
* Create .env.prod file and fill it with the following data
```env
FLASK_ENV='production'
FLASK_RUN_PORT=port on which the flask will be available
DATABASE_URL='Elephantsql database URL'(replace postgres with postgresql)
APP_SETTINGS='flask_ecom_api.config.ProductionConfig'
SECRET_KEY='your site strong secretkey' (you can generate it [here](https://djecrety.ir/))
JWT_TOKEN_LIFETIME=jwt token lifetime in hours
```

Run the command:
```bash
docker-compose -f docker-compose.prod.yaml up --build
```

## License

Project is licensed under the MIT License. See [LICENSE](https://github.com/savilard/flask-ecom-api/blob/main/LICENSE) for more information.
