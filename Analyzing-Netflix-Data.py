#Analyzing Netflix Data
#Creating a dictionary years and durations lists
yrs = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
time = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

mv_dictionary = {'years': yrs, 'durations': time}
mv_dictionary

#import pandas as pd & create DataFrame using mv_dictionary
import pandas as pd
durations_df = pd.DataFrame(mv_dictionary)
durations_df

#Import matplotlib.pyplot to visualise the data and test plot
#Create a figure and draw a line plot with years (x-axis) & duration (y-axis)
import matplotlib.pyplot as plot
fig = plot.figure()

plot.plot(yrs, time)
#give the plot a title
plot.title("Netflix Movie Durations 2011-2020")
plot.show

#Read in a CSV file to load more data
csv_df = pd.read_csv("C:/Users/rsoba/Desktop/Rahima's Folder/Important Docs/Data Science/Python/Analyzing Netflix Data/datasets/netflix_data.csv")

#printing first 5 rows of the DF
csv_df.head()

#subsetting the csv data frame for type "Movie"
mvs_only = csv_df[csv_df["type"] == "Movie"]

#subset the DF to Filter out required columns (title, country, genre, release year, duration)
mvs_columns = mvs_only[['title', 'country', 'genre', 'release_year', 'duration']]

#printing first 5 rows of mvs_columns
mvs_columns.head()

#create a scatter plot with release_year (x-axis) & duration (y-axis)
#creating and increasing figure size
fig = plot.figure(figsize = (12,8))

plot.scatter (yrs, time)
plot.title("Movie Duration by Year of Release")
plot.show()

#filter for movies < 60 minutes to analyse trends
short_mvs = mvs_columns[mvs_columns['duration'] < 60]
short_mvs.head(20) #print the first 20 rows

#sort the genres by color to identify trends
#defining empty list for colors
colors = []

#Using a for loop to assign colors to genres 
for lab, row in mvs_columns.iterrows() :
    if row['genre'] == "Children":
        colors.append("blue")
    elif row ['genre'] == "Documentaries":
        colors.append("purple")
    elif row ['genre'] == "Stand-Up":
        colors.append("pink")
    else:
        colors.append("green")

#Print the first 10 values
colors [0:10]

#Using the colors to create a plot
plot.style.use('fivethirtyeight')
fig = plot.figure(figsize = (12,8))

#Make a scatter plot release_year (x-axis) and duration (y-axis)
plot.scatter(mvs_columns["release_year"], mvs_columns["duration"], c= colors)

#Add plot title and axis labels
plot.title("Movie duration by year of release")
plot.xlabel("Release Year")
plot.ylabel("Duration(mins)")
plot.show

#Does this prove that movies are getting shorter? No 

#Done as a Python project through Data Camp

