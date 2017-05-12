# 5 Trees and Graphs

## Trees
* A tree is made up of nodes (data elements) with zero, one, or several references (or pointers) to other nodes. Each node has only one node referencing it.

### Implementation (tree of integers)
* Node  (parent class)
  * Array/list of children
  * Constructor initializes children
  * `get_num_children` gets length of children
  * `get_child` gets child at specified index
* IntNode (child class, extends Node)
  * Value variable
  * Constructor initializes children and value
  * `get_value` gets value of current IntNode
* Also implement error handling and methods to add and remove nodes from the tree

### Tree-Related Terms
* Root
  * The top-level node in the tree from which you have a path to every other node
* Parent
  * A node that points to other nodes is the parent of those nodes
  * Every node except the root has one parent
* Child
  * A node is the child of any node that points to it
* Descendant
  * All the nodes that can be reached by following a path of child nodes from a particular node are the descendants of that node
* Ancestor
  * An ancestor of a node is any other node for which the node is a descendant
* Leaves
  * The leaves are nodes that do not have any children

## Binary Trees
* Most tree problems involve this type of tree
* Each node has no more than two children, referred to as left and right

### Implementation
* Node
  * Node left variable
  * Node right variable
  * Value variable
  * Constructor initializes left, right, and value
  * `get_left` gets value of left
  * `get_right` gets value of right
  * `get_value` gets value of value

### Interviewing
* If an interviewer says "tree", it's a good idea to clarify whether she is referring to a generic tree or a binary tree
  * When interviewers say "tree", they often mean a binary tree

## Binary Search Trees (BST)
* Most common way to store ordered data in a tree
* The value held by a node's left child is less than or equal to its own value
* The value held by a node's right child is greater than or equal to its value
* The data in a BST is sorted by value
  * All the descendants to the left of a node are less than or equal to the node
  * All the descendants to the right of a node are greater than or equal to the node
* When interviewers say "tree", they often mean a binary search tree

### Lookup in a BST
* Lookup operations in BSTs are fast and simple
  * Fast because we eliminate half the remaining nodes from our search on each iteration by choosing to follow the left subtree or the right subtree
    * In the worst case, we will know whether the lookup was successful by the time there is only one node left to search
    * The running time of the lookup is equal to the number of times that we can halve n nodes before we get to 1
      * This number, x, is the same as the number of times we can double 1 before reaching n, and it can be expressed as 2^x=n
        * We can find x using a logarithm
  * Lookup is an O(log(n)) operation in a balanced binary search tree
    * Only true if we can guarantee that the number of nodes remaining to be searched will be halved or nearly halved on each iteration
      * In the worst case, each node only has one child, in which case we end up with a linked list and lookup becomes an O(n) operation
  * Deletion and insertion are O(log(n)) operations in binary search trees
* This is useful for data storage
* Algorithm
  * Start at the root node
  * Loop while current node is non-null
    * If the current node's value is equal to the search value
      * Return the current node
    * If the current node's value is less than the search value
      * Make the right node the current node
    * If the current node's value is greater than the search value
      * Make the left node the current node
  * End loop
* If we fall out of the loop, the node wasn't in the tree

### Other Important Properties of BSTs
* We can obtain the smallest element by following all the left children
* We can obtain the largest element by following all the right children
* The nodes can be printed out, in order, in O(n) time
* Given a node, we can find the next highest node in O(log(n)) time
