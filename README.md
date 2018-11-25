# When is the best time to book your next Airbnb?

This is the fourth project in Udacity's Data Scientist Nanodegree. I analyze data for Airbnb in Toronto for 2018/19, and attempt to find interesting trends and observations. I attempt to answer 3 main questions here: 

1. Are there any visible trends in the Airbnb prices in Toronto?
2. Are weekends actually more expensive to book?
3. What is the ideal time to book your Airbnb during the holiday season in Toronto?

The files in the repository are:

 - blog.py -> Main file with the code to produce the charts and the analysis
 - img -> Folder where all the charts live
 - data -> Folder where the data live

For this project, tibraries used are `numpy` `pandas` `matplotlib` `cycler`.

The data files were too big to upload onto github. So in order to replicate the results, please submit the following commands in the command line from the directory of your choice.

```bash
git clone https://github.com/beefupinetree/dsnd-blog-post.git
cd data/

wget http://data.insideairbnb.com/canada/on/toronto/2018-10-06/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
wget http://data.insideairbnb.com/canada/on/toronto/2018-09-09/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
wget http://data.insideairbnb.com/canada/on/toronto/2018-08-08/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
wget http://data.insideairbnb.com/canada/on/toronto/2018-07-06/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
wget http://data.insideairbnb.com/canada/on/toronto/2018-05-11/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
wget http://data.insideairbnb.com/canada/on/toronto/2018-04-09/data/calendar.csv.gz
gzip -d calendar.csv.gz
mv calendar.csv calendar_oct.csv
```

## Summary

The data shows certain seasonal and inherent trends which are consistent throughout different extraction dates. There are spikes in the week of the winter holidays no matter when we look at the data. However, by comparing the average listing price per day for each different extraction date, we concluded that the best time to book a listing during the winter holidays is in the month of July.

<p align="center"><img src="/img/4.png?raw=true"/></p>
