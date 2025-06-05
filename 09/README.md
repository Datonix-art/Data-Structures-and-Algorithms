stack is a data structure that stores ordered items. it is like a list and design is more restrictive. it only allows items to be removed or added from only top of the stack

It's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item off the top of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. You'll often hear a stack referred to as a LIFO (last in, first out) data structure.


Operation 	Big O 	Description
push 	    O(1) 	Add an item to the top of the stack
pop 	    O(1) 	Remove and return the top item from the stack
peek 	    O(1) 	Return the top item from the stack without modifying the stack
size 	    O(1) 	Return the number of items in the stack


All supported operations are O(1) by themselves. However, some tasks, like getting to an item at the bottom of the stack have a higher time complexity because they require multiple pop operations.

Stacks are often used in the real world for:

    Function call management
    Undo/redo functionality
    Expression evaluation
    Browser history
