''' 
Agglomeration cluster
'''

import numpy as np # fundamental scientific computing package
import pandas as pd # data analysis and manipulation package
from scipy.spatial import distance # calculate Euclidean distance

# recording all the weights during the agglomeration
merged_weights = []

# for saving train model
trained_program=open('./HW07_MQ_Trained_Classifier.txt','a')

class Agglomeration_Node:
    '''
    Node definition for the agglomeration cluster
    left: left child of this node
    right: right child of this node
    values: list of IDs that are same cluster
    label: the class this node is
    size: how many values are in the cluster
    center: center point of the cluster
    Right node's size should be smaller than left
    '''
    def __init__(self, left = None, right = None, values = None):
        self.left = left
        self.right = right
        if(left != None and right != None):
            self.values = left.values+right.values
            self.center = (left.center*left.size + right.center*right.size)\
                /(left.size+right.size)
            self.label = min(left.label,right.label)
            self.size = left.size + right.size
        else:
            self.values = [values['ID']]
            self.center = values[1:]
            self.label = values['ID']
            self.size = 1

def Merge(data_nodes, node_pair):
    '''
    data_nodes : all current data nodes
    node_pair : the two nodes to merge
    Merge will remove these two nodes and add a new merged node to all data nodes
    '''

    # determine which node is smaller, the bigger size node would be left node
    if(node_pair[0].size >= node_pair[1].size):
        left = node_pair[0]
        right = node_pair[1]
    else:
        left = node_pair[1]
        right = node_pair[0]

    merged_weights.append(right.size)
    merged_node = Agglomeration_Node(left, right)
    data_nodes.add(merged_node)
    data_nodes.remove(node_pair[0])
    data_nodes.remove(node_pair[1])
    print(str(len(merged_weights)) + "nodes merged")
    return data_nodes

def Agglomeration_Clustering(data_nodes):
    '''
    Agglomeration algorithm
    Starting with all elements as a single cluster
    Ending with only one cluster
    Returning a tree recording all middle clusters
    '''
    min_dist = np.inf
    count = 0
    for node1 in data_nodes:
        for node2 in data_nodes:
            dist = distance.euclidean(node1.center , node2.center)
            count+=1
            if dist < min_dist and dist != 0:
                min_dist = dist
                node_pair = node1, node2
    
    return(Merge(data_nodes, node_pair))

def Pre_Traversal(root, depth = 0):
    '''
    pre_traversal for the tree root
    show the full model
    '''
    # restrictions, because the tree has over 800 nodes
    if depth > 10 or root is None:
        return
    depth += 1
    trained_program.write(str(depth) + ' ' + str(root.label) + ' ' + str(root.size) + '\n')
    trained_program.write(str(root.values) + '\n')
    Pre_Traversal(root.left, depth)
    Pre_Traversal(root.right, depth)

def main():

    # read csv file
    shopping_cart_data = pd.read_csv('HW_PCA_SHOPPING_CART_v895.csv')
    # initialize all data nodes
    data_nodes = set()
    for index in range(0, shopping_cart_data.shape[0]):
        data_nodes.add(Agglomeration_Node(None, None, \
            shopping_cart_data.iloc[index,:]))

    # we can build a fully agglomeration tree by setting the umber of nodes 1 
    while len(data_nodes) > 1:
        data_nodes = Agglomeration_Clustering(data_nodes)

    Pre_Traversal(data_nodes.pop())
    trained_program.write(str(merged_weights))
    print('All Merged weight:' + str(merged_weights))
    

if __name__ == "__main__":
    main()