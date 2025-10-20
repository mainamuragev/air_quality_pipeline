#  Air Quality Pipeline

Real-time air quality ingestion pipeline for Nairobi and Mombasa, built with Kafka, Cassandra, and Python.

##  Tech Stack
- **Kafka**: Stream ingestion
- **Python**: ETL orchestration
- **MongoDB**: Raw data storage
- **Cassandra**: Scalable inserts
- **Airflow**: Optional DAG scheduling

##  Data Sources
- Public environmental APIs
- Custom ingestion scripts
- Validated for Nairobi & Mombasa

##  Features
- Real-time ingestion and transformation
- Scalable backend architecture
- Reproducible workflows with clean logging
- Modular design for future expansion

##  Setup
```bash
git clone https://github.com/mainamuragev/air_quality_pipeline.git
cd air_quality_pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##  Usage
Run the ingestion script:
```bash
python ingest_air_quality.py
```

## Validation
Includes:
- URL checks
- Schema enforcement
- Logging for each stage

##  Contributing
Open to collaborators focused on environmental data, backend systems, or scalable infrastructure.

##  Contact
Maina Murage — muragevincent39@gmail.com
