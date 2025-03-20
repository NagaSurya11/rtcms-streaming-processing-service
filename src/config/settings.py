import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

KAFKA_BROKER = os.getenv('KAFKA_BROKER')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

MINIO_BUCKET_NAME=os.getenv('MINIO_BUCKET_NAME')
MINIO_ACCESS_KEY=os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY=os.getenv('MINIO_SECRET_KEY')
MINIO_ENDPOINT=os.getenv('MINIO_ENDPOINT')

SPARK_MODE=os.getenv('SPARK_MODE')
SPARK_MASTER_URL=os.getenv('SPARK_MASTER_URL')