# Mth-to-Last Element of a Linked List

## Given a singly linked list, devise a time- and space-efficient algorithm to find the *m*th-to-last element of the list. Implement the algorithm, taking care to handle relevant error conditions. Define *m*th to last such that when *m* = 0 the last element of the list is returned.

* You may want to tell your interviewer that a singly linked list is a particularly poor choice for a data structure when you frequently need to find the *m*th-to-last element.
  * This comment shows that you understand good design
* If you could change the functions that modify the list such that they would increment a count variable for every element added and decrement it for every element removed, you could eliminate the count pass, making this a relatively efficient algorithm.

## Solutions
* We could iterate through the list twice, once to get the length of the entire list and a second time to find the *m*th-to-last element.
  * Runs in O(*n* + *n*) = O(*n*) time if *n* is the length of the list
* We could iterate through the list once by maintaining two position pointers -- an *m*-behind pointer and a current position pointer. We will maintain a distance of *m* between the two position pointers. Once the current position pointer reaches the end of the list, the *m*-behind pointer will give us the *m*th-to-last element of the linked list.
  * Runs in O(*n*) time, faster than O(*n* + *n*) time, if *n* is the length of the list
