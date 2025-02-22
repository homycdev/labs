![ci workflow](https://github.com/homycdev/labs/actions/workflows/ci.yaml/badge.svg?style=for-the-badge)


## Overview

This is Python web application written using [FastAPI framework](https://fastapi.tiangolo.com) and [WorldTimeAPI](http://worldtimeapi.org) showing current Moscow time.

## Getting Started
### Local installation
Before running the application, please install its prerequisites:
* [Python 3.7+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)

To run from the master branch, follow the instructions below:
1. Clone web application repository locally.
    ```bash
    git clone https://github.com/homycdev/labs
    cd labs/app_python/
    ```
2. Create virtual environment.
    ```bash
    python3 -m virtualenv venv 
    source venv/bin/activate
    ```
3. Install packages.
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application. Web app will open at [http://localhost:8000/](http://localhost:8000/).
    ```bash
    uvicorn moscow_time.main:app --reload
    ```
   

### Docker installation
Before running the application, please install its prerequisites:
* [Docker 20.10.7+](https://docs.docker.com/get-docker/)

To run from the master branch, follow the instructions below:
1. Clone web application repository locally.
    ```bash
    git clone https://github.com/homycdev/labs
    cd labs/app_python/
    ```
2. [Optional] Build the image.
    ```bash
    docker build -t homycdev/labs .
   ```
3. Run the container. Web app will open at [http://localhost:8000/](http://localhost:8000/).
    ```
    docker run -p 8000:8000 -v data:/home/app/data homycdev/labs
    ```

### Unit Testing
1. Make sure that you are in the application directory:
    ```bash
    cd labs/app_python
    ```
2. Run the tests:
    ```bash
    pytest tests
    ```
