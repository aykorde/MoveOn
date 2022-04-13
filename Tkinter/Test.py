from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import MinMaxScalerModel
from pyspark.ml.classification import GBTClassificationModel
from pyspark.sql import SparkSession

import pandas as pd


def createDF(ax, ay, az, gx, gy, gz, w):
    data = [(ax, ay, az, gx, gy, gz, w)]
    df = pd.DataFrame(data, columns=['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'wrist'])

    # Create PySpark SparkSession
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("SparkByExamples.com") \
        .getOrCreate()
    # Create PySpark DataFrame from Pandas

    sdf = spark.createDataFrame(df)
    sdf.show()
    return sdf


def mergeFeatures(df):
    features = VectorAssembler(inputCols=['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'wrist'], outputCol='Independent Features')
    mon_df = features.transform(df)
    print("Features merged")
    scalardata = MinMaxScalerModel.load('/user/talentum/MoveOn/scalardata')
    out = scalardata.transform(mon_df)
    print("Applied MinMax scaler")
    return out


def prediction(df):
    sgbmodel = GBTClassificationModel.load('/user/talentum/MoveOn/ModelGB')
    spredictions = sgbmodel.transform(df.select('scaledFeatures'))
    return float(spredictions.first()['prediction'])
