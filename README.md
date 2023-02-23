# Nintendo Video Games Sales

## Data Source
I tried to look for nintendo video game Sales and I found a dataset here https://en.wikipedia.org/wiki/List_of_best-selling_Nintendo_Switch_video_games. It showed the best selling nintendo video games and I to ensure my data was accurate I looked where they obtained this data. I found that obtained the data by going to the Nintendo website and looking at their financial data where they have the best selling video games. 

## Analysis Appoach
Since the data was not in an easily downloadable format like Excel or a CSV file, I decided to write a Python Script that would web scrape the html page and would extract the data into a CSV file. Afterwards I would clean the data in Excel making sure that  column data types are correct and looking for weird errors that may have occurred extracting the data. Finally I would put my clean dataset in PowerBi and create my visuals in there. 

## Content
There are 74 rows and 8 rows in the Final Dataset. All of the attirbutes in the dataset are self explanatory except for As of. As of refers to when Nintendo last updated the sales Data. Most of the As of data were last updated December 2022 and January 2021 with only a few data points falling before January 2021. The Release date data range consists of games as old as March 2017 and as new as November 18, 2022.

## Attributes in dataset

* Ranking
* Title
* Copies sold (in millions)
* As of
* Release date
* Genre(s)
* Developer(s)
* Publisher(s)

## Questions

1. What are the top 10 best selling games?
2. What are the top 5 best selling genres?
3. Which developers have the biggest sum of video game copies sold?


## Data Cleaning
Biggest thing I noticed when looking at the dataset at first was that the citation number was still attached to the sales data so I had to remove them. I also removed the millions on each row for sales data because Powerbi would recognize it as a string and I would like it to recognize it as a decimal number. Finally I add the units of measurements in the header of copies sold.

## Visualization 
I used PowerBI in order to visualize my data. You can find these Visualizations in the Visualization folder where you can view the powerbi file to interact with the data or just view the pdf file if you want the general gist of it.

## Files in Repository
Datasets Original and Cleaned Dataset
Visualization Powerbi Visualization
Wikipage_webscrapper.py Python script to scrape wiki page
Reports Powerpoint Presentation of Findings.