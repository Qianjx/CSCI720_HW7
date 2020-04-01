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

### Part 1 (Guo, Zizhun): Using Cross-Correlation for Feature Rejection and Selection
Codes:
```py
import pandas as pd

# rule out ID column
column_names = df.columns[1:column_names_size]  
df_new = df.iloc[:, 1:column_names_size]

# use panda package to get correlation matrix
corr = df_new.corr()
```
The cc matrix:
![ccmaxtrix](https://i.imgur.com/jcg1WMc.png)

<!-- For Questions **e** **f** **g**
Code:
```py
    min_dist = np.inf
    min_dist_2nd = np.inf

    idx_min = np.inf
    idx_min_2nd = np.inf
    
    for attr1 in range(0, 20):
        dist_total = 0
        for attr2 in range(0, 20):
            dist_total += distance.euclidean(corr.values[attr1] , corr.values[attr2])
        dist = dist_total/20
        if dist < min_dist and dist != 0:
            idx_min_2nd = idx_min
            min_dist_2nd = min_dist
            idx_min = attr1
            min_dist = dist
    print(corr)
    print(min_dist)
    print("first leaset correlated with all others:" + str(column_names[idx_min]))
    print(min_dist_2nd)
    print("second leaset correlated with all others:" + str(column_names[idx_min_2nd]))
``` -->


**Questions:**

a. Which two attributes are most strongly cross-correlated with each other? ( ¼ )
> Corn & Tortya

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
> Yes. Buying fish is also strongly cross-correlated with buying baby products.
> Suppose: 
$cov(buying fish) = x = cos\alpha$ 
$cov(buying cereal) = y = cos\beta$
$cov(buying baby products) = z = cos\gamma$
Since the value of x, y and z are in range between -1 to 1 
$\alpha, \beta, \gamma\in[0, \pi]$
so $cos\alpha cos\beta - sin\alpha sin\beta <= cos\gamma <= cos\alpha cos\beta + sin\alpha sin\beta$
so $cos(\alpha + \beta) <= cos\gamma <= cos(\alpha - \beta)$
so $\vert \alpha - \beta \vert <= \gamma <= min(\alpha + \beta, 2\pi - \alpha -\beta)$
This proves if the other sides from $\alpha$ and $\beta$ are at the same side of the common side which they both have (x and y are both either positive or negative), $\gamma$ has the minimal value of $\vert \alpha - \beta \vert$. $cos \gamma$ would be closer to 1.0 or -1.0 than $\alpha$ or $\beta$.
If $\alpha$ and $\beta$ are on the wrong sides, $\gamma$ can still get smaller value, which makes the correlation coefficients keep strongly the same.


---
### Part 3 (Qian Martin): Agglomeration

Final agglomeration clustering result:
<img src="HW7.png" title="final result" width="400" height="400" />
The nodes show two things: their size and their labels. According to the requirement of letting small labels be main label while merging, the root label is definetaly 1. As we can see, six clusters(blue nodes) has been clearly generated, Due to the tree structure, no more nodes are needed to be shown.

The model training part is very time consuming, about 3 hours. So it is not recommended to run to code. Alternatively, we saved the model into a text file and rebuild it with information we preserved. This is a rough display of the model, and if you want to see all the label for trained dataset, you can read the HW07_MQ_Trained_Classifier.txt for details.

---

1. When you have clustered to six clusters, report the size of each cluster, from lowest to highest. 
115 121 131 140 161 181 

2. When you have clustered to six clusters, report the average prototype of these six clusters.
node 1:
node 2:
node 3: 
node 4: 
node 5:
node 6:

3. What typifies each of the six clusters?  What name should we give each of these prototypes? 
As far as I am concerned, I am not sure what kind of name I should assign to each cluster. By looking into the dataset, for example, cluster labeled 1, we can see they are likely to buy eggs and milk and daily food together. So I think they might be students or workers. Similar to the rest 5 clusters.

6. Write a conclusion about what you learned overall.   If each of you learned different things, tell me what each of you learned. 

**Martin Qian:**
>I learned a lot of clustering algorithms, not only agglomeration, I also learned something about k-means, DBScan and PCA. Apart from this, I learned the importance of effeciency and code optimization as this time training the model is really time consuming. The time complecity is O(n^3) and as a matter of fact can be reduced to O(n^2) if we can backup all these distance rather than compute them again.
> As for data exploration itself, I have to say the data is exactly divided into 6 clusters, very clearly and explicit. When all beanches of one node is in big size, this indicating this two nodes are all complete and pure clusters.  

**Zizhun Guo:**
>What did I learn?
CC can be used to determine what attributes can be discarded or not. For example, some attributes like milk and fruit attributes, they are the two attributes that are least correlated with all other attributes. The reason may come from that all customers conducted consumption would highly possible purchase these two products, which makes them less considerably matter to the clustering. So the two can be pruned before conducting the clustering algorithm in order to reduce the dimensions of the data set so that to increase the efficiencies.