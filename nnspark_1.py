from pyspark import SparkContext
from csv_parser import csvRDD
import csv
import sys
from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SQLContext

if __name__=='__main__':
    # Load training data
    data = sqlContext.read.format("libsvm")\
        .load("result.txt")
    # Split the data into train and test
    splits = data.randomSplit([0.7, 0.3], 1234)
    train = splits[0]
    test = splits[1]
    # specify layers for the neural network:
    # input layer of size 4 (features), two intermediate of size 5 and 4
    # and output of size 3 (classes)
    layers = [4, 2, 3]
    # create the trainer and set its parameters
    trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=1234)
    # train the model
    model = trainer.fit(train)
    # compute precision on the test set
    result = model.transform(test)
    predictionAndLabels = result.select("prediction", "label")
    evaluator = MulticlassClassificationEvaluator(metricName="precision")
    print("Precision:" + str(evaluator.evaluate(predictionAndLabels)))