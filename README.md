# Wg_forge_backend tests

## Initial setup:

- Install Python version 3.6 or higher with the [pip](https://pypi.org/project/pip/) and [virualenv](https://pypi.org/project/virtualenv/) packages.
- Install Docker CE version 18.09 or higher.
- Run the following commands to install WG databa
se cantainer:
```shell
$ docker pull yzh44yzh/wg_forge_backend_env:1.1
$ docker run -p 5432:5432 -d yzh44yzh/wg_forge_backend_env:1.1
```
## Tasks `1-2`:

The solution for the first and the second tasks are implemented in the `color_statistics` and `math_statistics` functions, located in the `cat_statistics.py` file. To run these function use the following commands (the result of the function calls will be saved to the `wg_forge_db` database):

```shell
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install psycopg2-binary
$ python3 cat_statistics.py
```

## Tasks `3-6`:
The solution for the task three - six is relised in the Django application `cat_service`.

To start the application use the following commands:

```shell
$ docker build . -t cat_service_image:latest

$ docker run --rm -d --net=host -p 8080:8080 cat_service_image:latest
```

To test the solution against the corresponding tasks, use the following commands: 

- Task 3 

  ```shell
  $ curl -X GET http://localhost:8080/ping
  ```
- Task 4

  1. List cats:
        ```shell
        $ curl -X GET http://localhost:8080/cats
        ``` 
  2. Sort by any attribute (e.g. `name`) in asc/desc order:
      ```shell
        $ curl -X GET http://localhost:8080/cats?attribute=name&order=asc
      ```
  3. List cats with the offset and limit:
      ```shell
        $ curl -X GET http://localhost:8080/cats?offset=10&limit=10
      ```
  4. All the attributes included:
        ```shell
        $ curl -X GET http://localhost:8080/cats?attribute=color&order=asc&offset=5&limit=2
        ```
- Task 5

    ```shell
    $ curl -X POST http://localhost:8080/cat \
    -d "{\"name\": \"Tihon The Second\", \"color\": \"red & white\", \"tail_length\": 15, \"whiskers_length\": 12}"
    ```
- Task 6

    The condition set by the Task 6 is met via the usage of the [nginx](https://nginx.org/) service with the parameter `limit_req_zone` set in the `cat_service_nginx.conf` configuration file. 