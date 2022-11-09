# Prog1-HW7

---

Write a program to tackle the following problems. All programming should use good function and variable names and sufficient comments for improved readability.

In **binary_search.py**, implement the recursive binary search algorithm described below.

An important problem in computer science is the 'searching' problem -- finding an element in a list (if it exists). Of course, we can use the find() function. But if our input list is especially nice, we can solve the problem more efficiently. The binary search algorithm allows us to find an element in a *sorted* list very quickly:

  1. Find the middle of the list (approximate is fine, I recommend length // 2).
  2. Check if the element at the middle is the element we want. If so, return its index.
  3. Otherwise, check if the element we are looking for is larger or smaller. If larger, do binary search on the right half of the list. If smaller, do binary search on the left half of the list.
  4. If you are doing binary search on an empty list, return None.
    
One tricky part of this recursive algorithm is translating the result of the recursive part into the correct answer. Consider the following example of how the program should run:

  >Inputs: list [1, 3, 5, 7, 9, 11, 13, 15], searching for 7.
    
    Middle is index 4, which contains 9. 7 is smaller than 9, so search the left half [1, 3, 5, 7].
        
        Middle is index 2, which contains 5. 7 is larger than 5, so search the right half [7].
            
            Middle is index 0, which contains 7. So return 0.
        
        Since index 0 of the right half was returned, return index 3.
    
    Since index 3 of the left half was returned, return index 3.

On the same input list, searching for 8 should return None.


Your completed program should do the following:
  - Implement a recursive function that executes binary search
  - Input from the user a sorted list. You may choose what format you would like them to input, but your program does not have to validate that input as long as it is clearly specified what to do.
  - Convert the user input into an actual list.
  - Input an element to search for.
  - Output the index at which that element was found if it was found.
  - Output something like 'element not found' if the element was not found. *Note: The appropriate way to check if a variable is None is not to use ==, but rather*
    >if var is None:

***Bonus***: In your binary search function, check that the list is actually sorted. If not, immediately return None or raise an exception.
