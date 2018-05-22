import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def main():
	sc = SparkContext(appName="PysparkStreaming")
	ssc = StreamingContext(sc,3) #Streaming execution = every 3 sec
	lines = ssc.textFileStream('mylogs/*.txt.gz')
	counts = lines.flatMap(lambda line: line.split(" ")) 
	counts.pprint()
	ssc.start()
	ssc.awaitTermination()

if __name__ == "__main__":
	main()
