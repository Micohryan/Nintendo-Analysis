# Macros-of-High-Protein-Foods

One of my passions outside of data analysis and coding is working out. While working out, you have to keep track of your diet and make sure you eat enough protein in order to allow your muscles to recover and grow. I was wondering what foods had the highest protein content and if I could find foods that I didn't know had high protein content into my diet. 

## Data Source

I looked on Kaggle to find any data sources that could help answer my question. The data source I found here https://www.kaggle.com/datasets/fydrose/macros-of-popular-high-protein-foods?select=macros_dataset.csv

## Content
The dataset was pretty new being published around November. The author obtained the data through cross-referencing blogs and lists for high protein foods and then finding the macro content or Fats, Protein, and Carb content of a 100g serving of each food. The dataset contains 60 rows and 8 different attributes. The author categorized each food in a certain food group in the category_name attribute. The origin column describes whther the food came from an animal or not. The diet_type column describes what foods are suitable for the three different types of diets which are Omnivorous, Vegetarian and Vegan.

## Attributes in dataset

* food_name
* proteins_100g
* carbohydrates_100g
* fat_100g
* energy_100g
* category_name
* origin
* diet_type

## Questions

1. General trends macros of high protein foods?
2. Which foods have the highest protein to calorie ratio?
3. Are there any significant difference between Macros and Calories between Diet Types?
4. Which food Groups have the lowest calorie content?

## Data Cleaning
I used Excel for my data cleaning process since the overall dataset was small. Overall the data set was already pretty clean as there were no missing data in any of the rows. While looking at the dataset I realized in the category_name while looking at all the unqiue values that some foods I felt were classified too specifically. For example there was only one yoghurt items and a few milk items. I felt that some of the rows could be categorized more generally. I organized any foods that felt to specific that also fell into Legumes, Dairy, and Seafood into these categories. I also decided that in the Diet types I wanted to add was Pescatarian so I looked for foods that were categorized as Seafood and converted their diet types to Pescatarian.

## Data Transformation
I then downloaded the dataset into a CSV file and used the Data Script found in the repository that uploads the data into my local PostgreSQL database. I then used PGAdmin 4 a management tool for PostgreSQL to transform my data and find answers to the questions above. 

## Visualization 
I used PowerBI in order to visualize my data. You can find these Visualizations in the Visualization folder where you can view the powerbi file to interact with the data or just view the pdf file if you want the general gist of it.

## Files in Repository
