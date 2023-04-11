# airflow2.0-demo

Slide Deck:

https://speakerdeck.com/srinidhi/getting-started-with-apache-airflow-srinidhi



# Airflow 2.0 Demo

This is a demo project for Apache Airflow 2.0. It showcases how to set up an Airflow environment using Docker Compose, and how to create and run a simple DAG (Directed Acyclic Graph).

## Prerequisites

Before running this project, ensure that you have the following software installed on your machine:

- Docker
- Docker Compose

## Getting Started

1. Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/Sri-nidhi/airflow2.0-demo.git
    ```

2. Navigate to the project directory:

    ```
    cd airflow2.0-demo
    ```

3. Run the following command to start the Airflow environment:

    ```
    docker-compose up -d
    ```

4. Once the environment is up and running, you can access the Airflow web interface at `http://localhost:8080`. The default login credentials are:

    - Username: `airflow`
    - Password: `airflow`

5. To run the sample DAG, open a new terminal window and run the following command:

    ```
    docker-compose exec airflow airflow dags unpause example_dag
    ```

6. Then, trigger the DAG by running the following command:

    ```
    docker-compose exec airflow airflow dags trigger example_dag
    ```

7. You can monitor the progress of the DAG in the Airflow web interface.

## Project Structure

The project has the following structure:

```
airflow2.0-demo/
├── dags/
│   ├── example_dag.py
│   └── ...
├── docker-compose.yml
└── README.md
```

- `dags/`: This directory contains the DAG definition files.
- `docker-compose.yml`: This file defines the Docker services and configurations for the Airflow environment.
- `README.md`: This file contains the project documentation.

## Contributing

If you want to contribute to this project, feel free to fork this repository and submit a pull request.

