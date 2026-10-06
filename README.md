# Weather ETL Pipeline

A data engineering pipeline that extracts weather data, transforms it, streams it through Apache Kafka, and loads it into PostgreSQL.

## Architecture

```text
Open-Meteo API
      │
      ▼
   Extract
      │
      ▼
 Transform
      │
      ▼
Python Producer
      │
      │ localhost:9092
      ▼
 Apache Kafka
      │
      │ weather topic
      ▼
Python Consumer
      │
      ▼
 PostgreSQL
```

the updated file is here
