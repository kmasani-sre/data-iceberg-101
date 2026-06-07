from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ReadJSON').getOrCreate()

dataFrame = spark.read.option("multiLine",True).json("/Users/kmasani/ml-learning/movies.json")

dataFrame.createOrReplaceTempView("MoviesTable")

dataFrame.printSchema()

oldMoviesDF = spark.sql("""
    Select count(*) as NewMovieCount from MoviesTable
        where year=2000
        UNION
    Select count(*) as OldMovieCount from MoviesTable
        where year=1900
""")

oldMoviesDF.show()