# 4 Linked Lists

## Why Linked Lists?
* Linked lists are easy/quick to implement
* Little variation exists in implementations
* Requires knowledge of how pointers and references work (if using C and C++)

## Kinds of Linked List
* Singly linked lists (most common in interviews)
* Doubly linked lists
* Circular linked lists

## Singly Linked Lists
* Each data element has a link (a pointer or reference) to the element that follows it in the list
* First element referred to as the head, last element referred to as the tail (has empty or null link)
* Can only be traversed in the forward direction
  * Complete traversal must begin with the first element

## Doubly Linked Lists
* Each element has a link to the previous element in the list as well as to the next element in the list
  * Possible to traverse the list in either direction
* Head has empty or null previous link

## Circular Linked Lists
* Comes in singly and doubly linked varieties
* Have no ends (no head or tail)
  * Each element in a circular linked list has non-null next (and previous, if it's also doubly linked) pointers or references
    * A list with one element merely points to itself
* Primary traversal problem for these lists is cycle avoidance
* Rarely appear in interview problems

## Basic Linked List Operations
* Tracking the head element
* Traversing the list
* Inserting and deleting list elements

### Tracking the Head Element
* The head element of a singly linked list must always be tracked; otherwise, the list will be lost -- either garbage collected or leaked
* The pointer or reference to the head of the list must be updated when a new element is inserted ahead of the first element or when the existing first element is removed from the list

### Traversing a List
* When traversing, you must always check that you haven't reached the end of the list
  * Always test for the end of a linked list as you traverse it

### Inserting and Deleting Elements
* Any insertion or deletion of elements in the middle of a list requires modification of the previous element's next pointer or reference
  * If only given the element to delete, must traverse the list from the head because there's no other way to find the preceding element
  * Special care must be taken when the element to be deleted is the head of a list
* Deletion or insertion require a pointer or reference to the element immediately preceding the deletion or insertion location
* Deletion of an element always requires at least two pointer variables
