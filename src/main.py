from fastapi import FastAPI
from pyspark.sql import SparkSession
from services.ticker_data_streaming_service import startStreaming
import uvicorn
from services.health_service import router

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("rtcms-streaming-processing-service") \
        .config('spark.sql.caseSensitive', True) \
        .config('spark.hadoop.fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem') \
        .config('spark.hadoop.fs.s3a.access.key','rtcms-admin') \
        .config('spark.hadoop.fs.s3a.secret.key', 'rtcms-admin') \
        .config('spark.hadoop.fs.s3a.endpoint','http://rtcms-minio:9000') \
        .config('spark.hadoop.fs.s3a.path.style.access', True) \
        .getOrCreate()
    startStreaming(spark)

    app = FastAPI(title='rtcms-streaming-processing-service')
    app.include_router(router)
    uvicorn.run(app, port=1000)
