# Hyperkalemia Error Detection

## Description
This repository contains notebooks analyzing and modelling [EICU Data](https://eicu-crd.mit.edu/). Demo data can be found [here](https://physionet.org/content/eicu-crd-demo/2.0/). Hyperkalemia is a condition where one's blood potassium levels are higher than normal. Traiditional blood tests are infamously susceptible to false positive hyperkalemia results due to a variety of factors. Through our work, we have developed models that can detect false positives with 80% recall.


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
