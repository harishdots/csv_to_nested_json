# CSV to Nested Json Tree

### Pre requisites
- `git` protocol client installed
- Repository management client like `SourceTree` or something that helps in the `git` workflow
- Docker desktop

## Steps project using docker

- First clone the respository on your local system using below commands
```
    git clone https://github.com/harishdots/csv_to_nested_json.git
    go to project directory  cd csv_to_json
    git checkout intermediate
```

* Build the project into development mode.
    ```
    docker-compose -f docker-compose.yml up
    ```
- In order to see the start up logs execute the following command
    ```
    docker-compose -f docker-compose.yml logs -f
    ```

* After that hit the URL on browser and upload csv to convert into nested json tree.
    ```
    http://127.0.0.1:5000/  
    ```

## Test Case Run on docker 
    ```
    docker run csv_to_json_web sh -c "python -m pytest csv_to_json/tests"
    ```