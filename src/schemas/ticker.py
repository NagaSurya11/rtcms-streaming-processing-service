from pyspark.sql.types import StructType, StringType, StructField, LongType, DecimalType, ArrayType

ticker_schema = ArrayType(StructType([
        StructField('e', StringType()),
        StructField('E', LongType()),
        StructField('s', StringType()),
        StructField('p', DecimalType(38, 18)),
        StructField('P', DecimalType(38, 18)),
        StructField('w', DecimalType(38, 18)),
        StructField('c', DecimalType(38, 18)),
        StructField('Q', DecimalType(38, 18)),
        StructField('o', DecimalType(38, 18)),
        StructField('h', DecimalType(38, 18)),
        StructField('l', DecimalType(38, 18)),
        StructField('v', DecimalType(38, 18)),
        StructField('q', DecimalType(38, 18)),
        StructField('O', LongType()),
        StructField('C', LongType()),
        StructField('F', LongType()),
        StructField('L', LongType()),
        StructField('n', LongType())
    ]))