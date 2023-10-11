# app/data_processing/spark_processor.py

from pyspark.sql import SparkSession

def process_data(data):
    try:
        # Create a SparkSession
        spark = SparkSession.builder.appName("MySparkApp").getOrCreate()
        
        # Split the input data into words
        words = data.split()  # Split by whitespace, you can use a more advanced tokenizer if needed
        
        # Create a DataFrame from the list of words
        data_df = spark.createDataFrame([(word,) for word in words], ['text'])
        
        # Perform word count
        word_counts = data_df.groupBy('text').count()
        
        # Print the word counts
        word_counts.show()
        # Collect the word counts as JSON strings
        json_data = word_counts.toJSON().collect()

        # Join the JSON strings into a single string
        result = "\n".join(json_data)

        spark.stop()
        return result
    except Exception as e:
        print(e)
