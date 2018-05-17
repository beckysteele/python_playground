from pyspark import SparkContext
from pyspark.sql.functions import *

#Uncomment this line if running with spark-submit 
#sc = SparkContext("local","Dataset Ops")

### NOTE that myDataSet is a DataFrame, and not an RDD Object!

#Comment this out if running with spark-submit
myDataSet = spark.read.text("debug.log-2018032011.gz")

#Uncomment this if running with spark-submit
#myDataSet = sc.textFile("debug.log-2018032011.gz")

# Filter df for lines that contain <LogValue>
#filteredData = myDataSet.map(lambda r: Row(r)).toDF(["value"])

filteredData = myDataSet.filter("value like '%LogValue%'")

# Write to CSV inside pyspark shell
filteredData.write.csv("/home/becky/Desktop/opsout/output.csv")

# Write to CSV with spark-submit
#filteredData.saveAsTextFile("/home/becky/Desktop/opsout/output.csv")
