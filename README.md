# Emergency Vitals Simulator

A Python project to simulate and inject rare critical vitals scenarios into Kafka streams.

## Usage

1.  Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run the simulator:

    ```bash
    python src/vitals_simulator.py
    ```

## Docker

1.  Build the Docker image:

    ```bash
    docker build -t emergency-vitals-simulator .
    ```

2.  Run the Docker container:

    ```bash
    docker run emergency-vitals-simulator
    ```


Make sure you have Kafka running on `localhost:9092` or change the `KAFKA_BOOTSTRAP_SERVERS` variable in `src/vitals_simulator.py`.
