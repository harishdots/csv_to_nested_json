# CSV to Nested Json Tree

## Introduction
This project is developed using python flask web application for convert CSV parent child structure to nested json tree.
This project contains the simple UI to upload CSV file and submit. After that uploaded csv file read data using pandas lib and convert into any level of hierarchy nested json tree.

# For Beginner

## Uses local run using virtual environment

- First clone the respository on your local system using below commands
```
    git clone https://github.com/harishdots/csv_to_nested_json.git
    go to project directory  cd csv_to_json
    git checkout beginner
```

- For local run after clone the repository.
* Create virtual environment and activate it.
    ```
    python -m venv venv
    source venv/bin/activate
    ```
* Install required packages using below command
    ```
    pip install -r requirements.txt
    ```
* Project Run on the local system use the below command.
    ```
    python main.py    
    ```
* After that hit the URL on browser and upload csv to convert into nested json tree.
    ```
    http://127.0.0.1:5000/  
    ```

## Test Case Run Local
```
python -m pytest csv_to_json/tests
```

# For Intermediate

### Pre requisites
- `git` protocol client installed
- Repository management client like `SourceTree` or something that helps in the `git` workflow
- Docker desktop

## Steps project using docker

* Build the project into development mode.
    ```
    docker-compose -f docker-compose.yml up
    ```
- In order to see the start up logs execute the following command
    ```
    docker-compose -f docker-compose.yml logs -f
    ```

## Test Case Run on docker
```
docker run csv_to_json_web sh -c "python -m pytest csv_to_json/tests"
```
