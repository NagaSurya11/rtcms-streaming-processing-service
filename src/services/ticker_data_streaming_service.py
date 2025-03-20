from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StringType, TimestampType
from pyspark.sql.functions import col, from_json, explode, expr

from src.schemas.ticker import ticker_schema

def transformData(df: DataFrame):
    df = df.withColumn('value', col('value').cast(StringType())) \
        .withColumn('timestamp', col('timestamp').cast(TimestampType())) \
        .select(col('value'), col('timestamp'))
    df = df.withColumn('value', col('value').cast(StringType())) \
        .withColumn('timestamp', col('timestamp').cast(TimestampType()))
    df = df.withColumn('value', from_json(col('value'), schema=ticker_schema))
    df = df.withColumn('ticker_data', explode('value')).drop('value')

    df = df.select(
        expr('ticker_data.E / 1000').cast(TimestampType()).alias('event_time'),  # Event time in seconds
        col('ticker_data.s').alias('symbol'),  # Symbol
        col('ticker_data.p').alias('price_change_value'),  # Price change value
        col('ticker_data.P').alias('price_change_percentage'),  # Price change percentage
        col('ticker_data.w').alias('weighted_average_price'),  # Weighted average price
        col('ticker_data.c').alias('last_traded_price'),  # Last traded price
        col('ticker_data.Q').alias('last_traded_quantity'),  # Last traded quantity
        col('ticker_data.o').alias('open_price'),  # Open price
        col('ticker_data.h').alias('high_price'),  # High price
        col('ticker_data.l').alias('low_price'),  # Low price
        col('ticker_data.v').alias('total_traded_volume'),  # Total traded volume
        col('ticker_data.q').alias('total_traded_quote_volume'),  # Total traded quote volume
        expr('ticker_data.O / 1000').cast(TimestampType()).alias('first_trade_time'),  # First trade time in seconds
        expr('ticker_data.C / 1000').cast(TimestampType()).alias('last_trade_time'),  # Last trade time in seconds
        col('ticker_data.F').alias('first_trade_id'),  # First trade ID
        col('ticker_data.L').alias('last_trade_id'),  # Last trade ID
        col('ticker_data.n').alias('number_of_trades'),  # Number of trades
        col('timestamp')  # Original timestamp
    )
    return df

def startStreaming(spark: SparkSession):
    df = spark.readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', 'rtcms-kafka:9092') \
    .option('subscribe', 'crypto_ticker') \
    .option('startingOffsets', 'earliest') \
    .load()
    df = transformData(df)
    query = df.writeStream \
    .format("parquet") \
    .option("checkpointLocation", "s3a://crypto-data/checkpoints") \
    .option("path", "s3a://crypto-data") \
    .outputMode("append") \
    .start()
    query.awaitTermination()

