# Hyperkalemia Error Detection

## Setup
1. Install virtualenv on your machine
```pip install virtualenv```

2. Clone repo

    ```git clone https://github.com/wirooo/bwest.git```
    
    ```cd bwest```

3. Setup virtualenv 
```virtualenv venv```

4. Activate venv

    Windows:
    ```venv\Scripts\activate```

    Linux:
    ```source venv/bin/activate```

5. Install requirements
```pip install -r requirements.txt```

6. [Install ODBC drivers](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15)


## Contribution
1. Pull before you start working
    
    ```git checkout master```
    
    ```git pull```

2. Create a new branch for each feature
    ```git checkout -b name/feature_title```

3. Push and create pull request when complete
    ```git push origin```
    You may come across some ```--set-upstream``` crap, just copy what it says
4. Don't push to master
