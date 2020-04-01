import numpy as np # fundamental scientific computing package
import pandas as pd # data analysis and manipulation package
from scipy.spatial import distance # calculate Euclidean distance

def main():
    df = pd.read_csv('HW_PCA_SHOPPING_CART_v895.csv')

    # sets colunm names' size
    column_names_size = np.size(df.columns)

    # label slice to keep only attributes but target varaible
    column_names = df.columns[1:column_names_size]
    
    df_new = df.iloc[:, 1:column_names_size]
    corr = df_new.corr()

    # Scene 1 => Questions: abcd
    # 
    # np.fill_diagonal(corr.values, np.nan)
    # np.abs(corr.values)
    # print(np.abs(corr).values)
    # order_top2 = np.argsort(-np.abs(corr).values, axis=1)[:, :2]
    # order_bottom = np.argsort(np.abs(corr).values, axis=1)[:, :2]
    # result_top2 = pd.DataFrame(
    #     corr.columns[order_top2], 
    #     columns=['1st', '2nd'],
    #     index=corr.index)
    # result_bottom = pd.DataFrame(
    #     corr.columns[order_bottom], 
    #     columns=['Last', 'Second_Last'],
    #     index=corr.index)
    # result = result_top2.join(result_bottom)
    # for x in result.columns:
    #     result[x+"_Val"] = corr.lookup(corr.index, result[x])
    # print(corr)
    # print(result[['1st', '1st_Val', '2nd', '2nd_Val', 'Second_Last', 'Second_Last_Val', 'Last', 'Last_Val']])
    
    
    # Scene 2
    #
    # min_dist = np.inf
    # min_2nd_dist = np.inf
    # attr_min = (np.inf, np.inf)
    # attr_2nd_min = (np.inf, np.inf)

    # for node1 in corr.values:
    #     for node2 in corr.values:
    #         dist = distance.euclidean(node1 , node2)

    #         # print(dist)
    #         if dist < min_dist and dist != 0:
    #             min_2nd_dist = min_dist
    #             min_dist = dist

    # for attr1 in range(0, 20):
    #     for attr2 in range(attr1 + 1, 20):
    #         dist = distance.euclidean(corr.values[attr1] , corr.values[attr2])
    #         # print(dist)
    #         if dist < min_dist and dist != 0:
    #             attr_2nd_min = attr_min
    #             min_2nd_dist = min_dist
    #             attr_min = (attr1, attr2)
    #             min_dist = dist

    # # print(corr.values[20])
    # print(min_2nd_dist)
    # print(min_dist)    
    # print(attr_2nd_min)
    # print(attr_min)
    # print("2nd leaset cor" + str(column_names[attr_2nd_min[0]]) + " " + str(column_names[attr_2nd_min[1]]))
    # print("leaset cor" + str(column_names[attr_min[0]]) + " " + str(column_names[attr_min[1]]))


    # Scene 3 => Questions: efg
    #
    #  Minimum Average distance among all correlation coeffients between one attribute to all others
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



if __name__ == "__main__":
    main()