
import time
import json
import random
from faker import Faker
from kafka import KafkaProducer
from critical_scenarios import critical_vitals_scenarios


fake = Faker()

# Kafka configuration
KAFKA_TOPIC = 'vitals-stream'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Change if your Kafka broker is running elsewhere

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def generate_normal_vitals():
    '''Generates realistic but normal vital signs data.'''
    heart_rate = random.randint(60, 100)
    spo2 = random.randint(95, 100)
    temperature = round(random.uniform(36.5, 37.5), 1)
    blood_pressure_systolic = random.randint(110, 140)
    blood_pressure_diastolic = random.randint(70, 90)

    vitals = {
        'patient_id': fake.uuid4(),
        'timestamp': time.time(),
        'heart_rate': heart_rate,
        'spo2': spo2,
        'temperature': temperature,
        'blood_pressure_systolic': blood_pressure_systolic,
        'blood_pressure_diastolic': blood_pressure_diastolic
    }
    return vitals

def inject_critical_scenario():
    '''Randomly selects and injects a critical vital signs scenario.'''
    scenario = random.choice(critical_vitals_scenarios)
    scenario['patient_id'] = fake.uuid4()
    scenario['timestamp'] = time.time()
    return scenario


if __name__ == '__main__':
    try:
        while True:
            # 90% of the time, generate normal vitals
            if random.random() < 0.90:
                vitals = generate_normal_vitals()
            else:
                # 10% of the time, inject a critical scenario
                vitals = inject_critical_scenario()

            print(f"Producing message: {vitals}")
            producer.send(KAFKA_TOPIC, value=vitals)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting the simulator.")
    finally:
        producer.close()
