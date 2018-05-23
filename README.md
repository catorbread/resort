# Resort
RESTful API test automation tool


![resort logo](https://github.com/againagainst/resort/blob/master/data/icons/resort_edit.png?raw=true)

<sub><sup>[Original Image by Vecteezy](https://www.vecteezy.com/vector-art/146821-palm-tree-collection-vectors)</sup></sub>

## Work in progress!
Development plan is described in the [TODO](TODO.md) list.

### Basic usage:
Let's suppose you have a server with the RESTful API (`test-server`). Now you want to introduce some changes to the `test-server` without modifying the API. And you want to be sure that your changes will not bring a regression to existing functionality. It would be nice `store` the `test-server` responses before the changes and `check` that there is no difference later. That is exactly what the `resort` does.

Create a directory for the resort's Project
```
$ mkdir basic-rest-test
$ cd basic-rest-test
```
Configure the resort and provide an API specification of the test-server
```
$ touch config.json
$ cat config.json
{
    "server": {
        "spec": "basic-apispec.json",
        "url": "http://localhost:8888"
    }
}
$ touch basic-apispec.json
$ cat basic-apispec.json
{
    "swagger": "2.0",
    "paths": {
        "/ping": {...},
        "/echo/?{entity}": {...}
    }
}
```
Now let's memorize the way the test server responds.
```
$ resort --store --config=config.json
```
The application will store some files that represents responses from the test-server, they called `etalons`.
Now you can make some changes in the test-servers's code, restart it, and let's check that everything works as expected:
```
$ resort --check --config=config.json
```

### How to prepare the dev environment:
```
python3 -m venv .venv
./.venv/bin/python3 -m pip install -r reqirements.txt
```

### How to start the REST-test server:
Terminal: 
```
(.venv) $ python ./basic_rest/app.py
```

VSCode: `F5 (Run Task...) -> "Basic REST Server"`


