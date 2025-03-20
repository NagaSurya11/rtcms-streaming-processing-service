# Use the Bitnami Spark image as the base
FROM bitnami/spark:3.5.5

# Set working directory inside the container
WORKDIR /app

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the Spark application
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1", "src/main.py"]
