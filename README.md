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
    git checkout advanced
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


## CI/CD with Github using Heroku Deployment

* CI/CD is a practice used by organizations to ship applications to customers faster and without common errors.

  - Setup CI/CD using github actions work workflows
    https://github.com/harishdots/csv_to_nested_json/actions
    Once we click on that link it provides the workflow template list where we can choose according to our tech. requirment and click setup work flow it will automatic create .yml file where we need to define jobs, steps and run related configurations.

  - Go to the heroku cloud (https://dashboard.heroku.com/)
    - Create new app (https://dashboard.heroku.com/apps) python-csv-to-json
    - Generate new API Key (https://dashboard.heroku.com/account)

  - Create new Secret env variable for heroku connectivity.
    - Go to the setting (https://github.com/harishdots/csv_to_nested_json/settings)
    - Add new secret (https://github.com/harishdots/csv_to_nested_json/settings/secrets/actions/new)
      - HEROKU_API_TOKEN:- API Token
      - HEROKU_APP_NAME:- APP Name

* Lets explains what each of the lines does.

    -name: CI
        -This is just specifying a name for the workflow
    -on: [push] The on command is used to specify an event that will trigger the workflow, this event can be push, pull_request etc.
        ```
        # Use an array when using more than one event
        on: [push, pull_request] 
        ```
    -jobs: Here we are specifying the job we want to run, in this case, we are setting up a build job.
        ```
            runs-on: ubuntu-latest
        ```
    -Steps: just indicate the various steps you want to run on that job        
        ```
        uses: actions/checkout@v1
        ```
        - it will use the actions/checkout github action with the ref @v1. This ref only refers to the github action version (nothing to do with your repo).
    -Run fetch --prune --unshallow
        -It will convert the shallow clone to the regular one.
    -Run Install Dependencies
        -It will install all the dependencies
    -Run Lint with flake8
        -It will install flake8 and stop the build if there are Python syntax errors or undefined names
    -Run Tests
        -It will run all the test cases which is created into the app.
    -Deploy to Heroku
        -This action run to deploy build to heroku.
    -Post action actions/checkout@v1
    -Complete job