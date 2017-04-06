# 1 Stack Implementation

## Implement a stack using either a linked list or a dynamic array. Design the interface to your stack to be complete, consistent, and easy to use.

## Importance
* Your knowledge of basic data structures
* Your ability to write routines to manipulate these structures
* Your ability to design consistent interfaces to a group of routines

## Notes
* stack
  * LIFO, push, pop
* linked list
  * easier to implement
* dynamic array
  * array that changes size as needed when elements are added
  * usually faster than linked list (no memory allocation)
  * must occasionally be resized
    * time consuming, elements are copied from the old array to the new array
  * offers random access to any element in the array if you know its index
    * unnecessary for implementing a stack
