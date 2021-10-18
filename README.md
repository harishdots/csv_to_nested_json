# CSV to Nested Json Tree

## Introduction
This project is developed using python flask web application for convert CSV parent child structure to nested json tree.
This project contains the simple UI to upload CSV file and submit. After that uploaded csv file read data using pandas lib and convert into any level of hierarchy nested json tree.


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

## Test Case Run
```
python -m pytest csv_to_json/tests
```