# Nutrition Facts for McDonald's Menu

## Background
Ray Kroc wanted to build a restaurant system that would be famous for providing food of consistently high quality and uniform methods of preparation. He wanted to serve burgers, buns, fries and beverages that tasted just the same in Alaska as they did in Alabama. To achieve this, he chose a unique path: persuading both franchisees and suppliers to buy into his vision, working not for McDonald’s but for themselves, together with McDonald’s. Many of McDonald’s most famous menu items – like the Big Mac, Filet-O-Fish, and Egg McMuffin – were created by franchisees.

## Objective
Roy wants to know how many calories does the average McDonald's value meal contain? How much do beverages, like soda or coffee, contribute to the overall caloric intake? Does ordered grilled chicken instead of crispy increase a sandwich's nutritional value? What about ordering egg whites instead of whole eggs? What is the least number of items could you order from the menu to meet one day's nutritional requirements?

## About the Dataset
The dataset is retrieved from [Kaggle](https://www.kaggle.com/mcdonalds/nutrition-facts). It contains 24 features, most of them are integer, and six are object/float. The dataset provides a nutrition analysis of every menu item on the US McDonald's menu, including breakfast, beef burgers, chicken and fish sandwiches, fries, salads, soda, coffee and tea, milkshakes, and desserts.

# Analysis
## How many calories does the average McDonald’s value meal contain?
There are 8 categories of menu in this dataset. They are Breakfast', 'Beef & Pork', 'Chicken & Fish', 'Salads',  'Snacks & Sides', 'Desserts', 'Beverages', 'Coffee & Tea', 'Smoothies & Shakes'. The definition of the ‘meal’ itself is ‘the food eaten on regular occasions’. So, it must not be any drink in the meal. By category the average calories in the meal category are:<br><br>
![Meal Category by Calories](/gambar/category_meal.jpg)<br><br>
‘Beef & Pork’, ‘Breakfast’ and ‘Chicken & Fish’ are the top three meal categories with highest calories. They are considered as main dish. The ‘Dessert’, ‘Salads’, and ‘Snack & Sides’ are considered side dish. Together they have average calories by 385.26 calories. The distribution of the meal calories are:<br><br>
![Meal Category by Calories Distributin](/gambar/meal_distribution.jpg)

## How much do beverages, like soda or coffee, contribute to the overall caloric intake?
Caloric intake is [defined](https://link.springer.com/10.1007/978-1-4419-1005-9_1107) as the amount of energy consumed via food and beverage. To estimate how many is your caloric intake, you need to know about your gender, weight (kg), height (cm), and years. We will choose the amount of the caloric intake by gender for the sake of simplicity. Generally, the [recommended](https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/#:~:text=Generally%2C%20the%20recommended%20daily%20calorie,women%20and%202%2C500%20for%20men.) daily calorie intake is 2,000 calories a day for women and 2,500 for men. After we know about the recommended daily calorie intake, we need to know how many average calories of soda and coffe to know how much they contribute to the overall caloric intake. 
```
  df_soda=dfbev[dfbev['Item'].str.contains("Coca-Cola|Coke|Pepper|Sprite")]
  df_soda['Item'].unique()
  df_coffe=dfbevt[dfbevt['Item'].str.contains("Coffee|Latte")]
  df_coffe['Item'].unique()

  avg_bef = df_soda['Calories'].mean()
  avg_beft = df_coffe['Calories'].mean()

  men_soda = avg_bef/2500
  women_soda=avg_bef/2000

  men_coffe = avg_beft/2500
  woment_coffe=avg_beft/2000
 ```
Soda will be retrieved from beverages category that contains Coca-Cola, Coke, Pepper and Sprite words. The coffee will be retrieved from coffee and tea category that contains Coffee and Latte words. Turns out the average calories for soda is 107 and average calories for coffee is 215.42. Divided by man and woman recommended daily calories intake, we will get 4.29% for woman and 5.36% for man in the soda categories. In the coffee we get 8.62% for woman and 10.77% for man. Therefore, we can [conclude](https://my.clevelandclinic.org/health/articles/4182-fat-and-calories) that coffee are more likely to make us fat faster than soda. 

## Does ordered grilled chicken instead of crispy increase a sandwich's nutritional value?
There are [seven](https://www.open.edu/openlearncreate/mod/oucontent/view.php?id=315&printable=1) main classes of nutrients that the body needs. These are carbohydrates, proteins, fats, vitamins, minerals, fiber and water. In the datasets, there are so many nutrients features. Some of them are Sodium, Total Fat, Protein, Sugar, Vitamin A, Vitamin C, Calcium, and Iron. We will not cover all of them, but pick some features that representing important nutrient. For the comparison, bar chart is used to determine whether grilled and crispy chicken in sandwich make a difference.<br><br>
![Comparison between grilled and crispy](/gambar/comparison_grilled1.jpg)<br><br>
![Comparison between grilled and crispy2](/gambar/comparison_grilled2.jpg)<br><br>
From the bar chart, we can conclude that eating grilled chicken instead of crispy chicken are increasing Cholesterol, Vitamin A, Vitamin C, Calcium, and Iron. 

## What about ordering egg whites instead of whole eggs? 
We will be do the same analysis from above. What makes it different is that we retrieving the menu that contains Egg White from the Item and menu that doesn’t contains Egg White but contains Egg from the menu.<br><br>
![Comparison between egg and only white egg](/gambar/comparison_egg2.jpg)<br><br>
![Comparison between egg and only white egg2](/gambar/comparison_egg1.jpg)<br><br>
From the bar chart, the egg whole are certainly contains more nutrient than menu that only has egg white. If you are ordering menu that has whole eggs, it will contains more Fiber, Vitamin A, Vitamin C, Calcium, and Iron. However, the menu with whole egg contains more Fat, Saturated Fat, and Cholesterol. Eating too much saturated fat can [increase](https://www.healthline.com/health/heart-disease/good-fats-vs-bad-fats) blood cholesterol levels and LDL (bad) cholesterol levels. Traditionally, doctors have linked higher saturated fat intake with [increased](https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/fats-and-cholesterol/) heart disease risks. So, if you are on diet, I suggest you to avoid the menu that has whole egg in the ingredients. Choose the menu wisely!

## What is the least number of items could you order from the menu to meet one day's nutritional requirements?
From the information above, the [recommended](https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/) daily calorie intake is 2,000 calories a day for women and 2,500 for men. So, we need the menu that have big calories value to make the least number of items to meet one day’s nutritional requirements. 
```
dfsortmeall=dfmeall.sort_values('Calories')
dfsortmeall.tail(3)
```
From the code above, we can know that the three menu that have biggest value of calories are Chciken McNuggets (1880 calories), Big Breakfast with Hotcakes (Large Biscuit) (1150 calories), and Big Breakfast with Hotcakes (Regular Biscuit) (1090 calories). So, we must order at least more than one menu to meet one day’s nutritional requirements. For women, the one’s day nutritional requirement is 2000. Therefore we need 120 calories more to make it 2000. Using:
```
dfsortmeall[(dfsortmeall['Calories'].between(110,130))]
```
We can find menu that have exactly 120 calories. The menu is French Vanilla Iced Coffee (Small) and Iced Coffee with Sugar Free French Vanilla Syrup. For men, we need 620 calories to make at least 2500 calories requirement. There is only one menu that have exactly 620 calories. The menu name is Bacon, Egg & Cheese Bagel. Thus, you need at least two number of items from the menu to meet one day’s nutritional requirement. 
<br>
Happy eating!
