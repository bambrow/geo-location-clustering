# Geo-Location Clustering in Spark

This project is the final project of course **Cloud Computing with Big Data Applications**. The detailed project report can be found [here](https://github.com/bambrow/geo-location-clustering/blob/master/project_report_github.pdf).

## Project Contributors
- Weiqiang Li
- Jin Yu

## Introduction and Objectives
### Introduction to Spark
Spark is a fast and general cluster computing system for Big Data. It provides high-level APIs in Scala, Java, Python, and R, and performs as an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for stream processing.

Spark completes the full data analytics operations in-memory and in near real-time. It overcomes many limitations of Hadoop MapReduce: Spark has more flexible framework, has higher-level abstraction, supports multiple programming languages, can keep the data in memory, provides interactive shell, and is faster than MapReduce. RDD, Resilient Distributed Datasets, is a fault-tolerant, parallel data structure, and the basic abstraction in Spark. RDD is a relatively flexible structure with a lot of functions to operate data.

### Introduction to k-Means Clustering
k-means is a general leaning algorithm of clustering. It assigns the data points to several centers according to the "distance" or some similarity measurements, and in this geo-location project, geographical distance is the intuitive similarity measurement. The closer two data points are, the more similar; the farther away they are, the more different. So in this geo-location k-means clustering, no matter we use Euclidean Distance or Great Circle Distance, we can get the relatively same result (when the starting centers are identical).

The main idea of k-means is to put all points into k clusters, and each point belongs to a cluster that corresponds to the nearest center. This algorithm is iterative, in that we need to re-calculate the new centers and re-assign the points to the new centers many times until there is no big difference of the change of the centers. In this way, k-means clustering can help find the similar objects and has many useful applications, such as customer clustering, document grouping, spatial data analyzing and so on.

### Project Motivation
For this project, geo-location clustering in spark, we use Spark as the framework to implement k-means. Our motivation for this project are stated below:

1. Get familiar with Spark. Spark is a useful tool in cloud computing and big data analysis. It would be extremely helpful to know Spark much better by implementing a algorithm to solve a practical problem than finishing labs in the class. As stated above, Spark has lots of advantages and is widely used for fast processing of big data, not limited to interactive queries and data analysis, but also in graph analyzation and machine learning. Being familiar with Spark will be a basic and important skill for students interested in big data.

2. Get familiar with k-means and data visualization. k-means is very useful in grouping similar objects and is widely used in marketing, social media analysis, document grouping and so on. This will be a very basic and useful skill. Data visualization, as we used in this project, is another important skill for students interested in big data because visualization will give the most direct feeling and the most intuitive understanding of the results. It is better in presentation of data analysis. Also, the meaning of the results of k-means clustering is important because data interpretation will lead us to better understanding of our datasets and guide us for further analysis and explanations.

3. This project can be extended to some very interesting and useful analysis. With functionality of stream processing, Spark can be helpful to analyze stream data like Twitter and Foursquare. In stream data analysis, location clustering is useful way to compute the geo-location hot spot. More importantly, we can use these data to monitor what is happening around the world, to give much better event report (or prediction), safety reminder, advertisement, and so on.

## Project Report
The detailed project report can be found [here](https://github.com/bambrow/geo-location-clustering/blob/master/project_report_github.pdf).
