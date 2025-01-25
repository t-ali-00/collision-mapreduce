# Hadoop MapReduce Framework for Analysing Motor Vehicle Collision Data
This repository contains Python scripts for a Hadoop MapReduce framework designed to process and analyse motor vehicle collision data. The framework calculates the average number of deaths and injuries per borough, providing actionable insights to improve transportation safety.

# Overview
Mapper: Extracts and formats relevant data (borough, deaths, and injuries) from the input dataset.
Reducer: Aggregates data by borough and calculates the average number of deaths and injuries.

# How It Works
Input Data: The CSV dataset is uploaded to HDFS.
Mapper: Processes each line of the dataset and outputs key-value pairs in the format borough \t num_killed \t num_injured.
Reducer: Groups data by borough, calculates averages for deaths and injuries, and outputs the results.

# Usage
Upload the dataset to HDFS.
Run the Mapper and Reducer scripts using Hadoop streaming.
View the output file in HDFS for results.

