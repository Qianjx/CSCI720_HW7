---
puppeteer:
  landscape: false
  format: "A4"
  timeout: 3000 # <= Special config, which means waitFor 3000 ms
  printBackground: true
---

 #  <center> CSCI 720 Big Data Analytics HW07 Results </center> 
---
Student: Guo, Zizhun & Qian, Martin
Submission: Apr/1st/2020
Due Date: Apr/1st/2020 11:59 PM 

---

a. Which two attributes are most strongly cross-correlated with each other? ( ¼ )
> Corn & Tortya

           1st   1st_Val     2nd   2nd_Val Second_Last  Second_Last_Val    Last  Last_Val
 Beans    Meat -0.632335  YogChs  0.555409      ChdBby         0.025656   Fruit -0.008510
 Bread   Cerel  0.444009    Milk  0.439962      ChdBby         0.005108    Eggs  0.002145
 Cerel  Tomato -0.474217   Bread  0.444009      ChdBby         0.013300   Fruit -0.011541
ChdBby  Pepper -0.051206  Tortya -0.048586       Bread         0.005108  Vegges  0.000585
 Chips  Vegges -0.541429    Soda  0.536912      ChdBby        -0.043383   Fruit -0.006616
  Corn  Tortya  0.832840  Pepper  0.718210        Meat         0.021903   Fruit  0.021371
  Eggs   Sauce -0.686711    Meat  0.537484       Cerel        -0.014874   Bread  0.002145
  Fish    Eggs  0.449056   Beans -0.370691       Cerel        -0.035770  ChdBby  0.034767
 Fruit    Fish -0.044383    Eggs -0.043175        Milk         0.001482  Pepper  0.000416
  Meat   Sauce -0.729068   Beans -0.632335       Bread         0.010868   Fruit -0.002114
  Milk  Pepper  0.487064   Bread  0.439962      Tomato         0.013328   Fruit  0.001482
Pepper    Corn  0.718210  Tortya  0.678290       Cerel         0.014198   Fruit  0.000416
  Rice    Soda -0.802872  Vegges  0.690419       Fruit        -0.020624  ChdBby  0.017592
 Salza  Tortya  0.643361    Corn  0.630477      ChdBby        -0.015251   Fruit -0.010956
 Sauce    Meat -0.729068    Eggs -0.686711      ChdBby         0.035463   Fruit  0.009706
  Soda    Rice -0.802872  Vegges -0.756236      ChdBby        -0.030395   Fruit -0.001972
Tomato  Tortya  0.737151    Corn  0.692017      ChdBby        -0.023454    Milk  0.013328
Tortya    Corn  0.832840  Tomato  0.737151      ChdBby        -0.048586   Fruit -0.031387
Vegges    Soda -0.756236    Rice  0.690419       Fruit         0.004984  ChdBby  0.000585
YogChs  Vegges  0.605484    Soda -0.591682      ChdBby        -0.027245   Fruit  0.019034

b. Which attribute is fish most strongly cross-correlated with? ( ¼ )
> Eggs

c. Which attribute is meat most strongly cross-correlated with? (¼)
> Sauce

d. Which attribute is beans most strongly cross-correlated with? (¼)
> Meat

e. Which one attribute is least correlated with all other attributes? (¼)
> Milk

f. Which second attribute is least correlated with all other attributes? (¼)
> Fruit

g. If you were to delete two attributes, which would you guess were irrelevant? (¼)
> Milk & Fruit

h. If buying fish is strongly cross-correlated with buying cereal, and buying cereal is strongly crosscorrelated with buying baby products, is buying fish strongly cross-correlated with buying baby products? Can you explain this? (¼)

