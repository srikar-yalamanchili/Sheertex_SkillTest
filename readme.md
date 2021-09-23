**SHEERTEX DATA ENGINEERING SKILLS CHALLENGE**

1. Load the data into the database using api\_v1.py.

2. Using REST API to retrieve the data using GET method using
api\_v1.py.

3. Write the data to the Datawarehouse using Data\_ingestion.py

-   API provided in the document has only one entry of data for which I
    may not be able to provide the real time usable code. So, I have
    written a python script using flask just for the demonstration
    process to run a server with some information.

-   I have created a real time orders data in CSV file, which in real
    world will be from the E-commerce website and thereby loaded the
    data into the database. Also, created a GET API to query the orders
    based on the given input dates. This is nothing but the sheertex api
    which keeps the date up to date with orders and new stock.

-   Next, this API is used to load the real time data to
    the datwarehouse.
    ![Alt archdiagram](img/img1.png?raw="true", "Flow digram")
    
-   Basically, API is a secured interface that allows applications to
    communicate within each other and main purpose is for information
    retrieval and updating without the need of manual intervention.

-   REST API's are commonly used commonly as it defines how the
    applications communicate within over HTTP for the transfer
    of information. We use GET, POST, PUT and DELETE methods to
    communicate with the webserver.

-   A virtual environment is created to run this, and all the
    requirements are listed in the **requirements.txt**.

-   **api\_v1.py** script mainly does the initialize a database, load
    the csv data to the database and API is exposed on the server to
    retrieve the data from the database.

-   Once the data is loaded, I retrieve the data using get method from
    the API through **data\_ingestion.py**

-   **data\_ingestion.py** script mainly used to extract the data from
    the API using GET method and ingest it to a sample Datawarehouse
    created using SQLite.

**RUNNING GUIDE:**

-   A specific virtual environment was created to manage dependencies
    and running things at one place using pyenv package of python. To
    download this activate

    **python -m venv dev **

    **dev\\Scripts\\activate.bat**

-   There is a **requirements.txt** file added to replicate the exact
    same dependencies on your machine without the need of specifying one
    after the other download.

    **pip install -r requirements.txt**

-   We will first create a database and write the data from
    the data.csv. Once we have the database, now we will start the API
    part using flask. This whole thing is done by running the
    api\_v1.py script. Run the following command.

    **python api\_v1.py**


-   This should open the local browser on port 5000 and the data appears
    on the screen in the JSON format.



-   Now we must extract the data from the REST API and ingest it into
    the Datawarehouse. I have created a SQLite database to save the
    fetched data from the API and ingesting it into the datawarehouse
    with the tables **orders** and **order\_items.** It is done just by
    running the **data\_ingestion.py** script with the
    following command.

    **Python data\_ingestion.py**



-   Now a **datawarehouse.db** file is generated with **orders** and
    **order\_items** table. We must use the SQLite to access the DB. Use
    the following commands.

