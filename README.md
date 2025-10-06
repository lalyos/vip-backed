## Install

install python version 3
```
pip install -r requirements.txt
```

## server start

```
uvicorn main:app --reload
```

## Build the image

```
docker build --platform linux/amd64  -t lalyos/backend .
docker push lalyos/backend
```

## start a DB

test db
```
docker run -d \
  --name mydb \
  -v vip-test:/var/lib/mysql \
  -v $PWD/sql:/docker-entrypoint-initdb.d   \
  -e MARIADB_ROOT_PASSWORD=secret  \
  mariadb
```

qa db
```
docker run -d \
  --name mydb \
  -v vip-qa:/var/lib/mysql \
  -v $PWD/sql:/docker-entrypoint-initdb.d   \
  -e MARIADB_ROOT_PASSWORD=secret  \
  mariadb
```