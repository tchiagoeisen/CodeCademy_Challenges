# CodeCademy: Code Challenges Python


1.  [Calculate the Mean and Mode](#calculate-the-mean-and-mode)<br>
2.  [Fibonacci Finder](#fibonacci-finder)<br>
3.  [Find the Missing Numbers](#find-the-missing-numbers)<br>
4.  [FizzBuzz](#fizzbuzz)<br>
5.  [Flatten an Array](#flatten-an-array)<br>
6.  [Prime Number Finder](#prime-number-finder)<br>
7.  [Product of Everything Else](#product-of-everything-else)<br>
8.  [Reverse Words](#reverse-words)<br>
9.  [Top Score Sorter](#top-score-sorter)<br>
10. [Unique Characters in a String](#unique-characters-in-a-string)<br>


## Calculate the Mean and Mode
Create a stats_finder() function that takes in a list of numbers and returns a list<br> 
containing the mean and mode, in that order. As a reminder, the mean is the average<br> 
of the values and the mode is the most occurring value. If there are multiple modes,<br> 
return the mode with the lowest value. Make sure that you write your functions and<br> 
find these answers from scratch – don’t use imported tools!

> For example, stats_finder([500, 400, 400, 375, 300, 350, 325, 300]) should return<br>
[368.75, 300].

## Fibonacci Finder
Create a fib_finder() function that finds the nth number in the Fibonacci sequence.<br>
As a reminder, the Fibonacci sequence is a mathematical sequence that begins with 0<br> 
and 1, with each following term being the sum of the two previous terms.

> For example, the first two terms of the sequence are represented by fib_finder(1)<br>
and fib_finder(2), which return 0 and 1, respectively. fib_finder(6) should return 5.<br>

## Find the Missing Numbers

You have a bag containing tiles with numbers [1, 2, 3, …, n] written on them.<br>
Each number appears exactly once, so there are n tiles and n numbers. Now, without<br>
looking, k number tiles are randomly picked out of the bag and discarded. Create a<br>
missing_nos() function that takes in a list and k, and returns the missing numbersin<br> 
ascending order (from smallest to greatest).

> For example, missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2) should return [3, 9].

## FizzBuzz
Write a fizzbuzz() function that takes in a number, n, and returns a list of the<br> 
numbers from 1 to n. For multiples of three, use "Fizz" instead of the number, and<br>
for the multiples of five, use "Buzz". For numbers that are multiples of both three<br> 
and five, use "FizzBuzz" (capitalization matters).

> For example, fizzbuzz(16) should return [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',<br> 
'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16].

## Flatten an Array
Write a function, flatten_array(), that takes in a 2-dimensional array,flattens it<br>
into a 1-dimensional array, and returns it. You can assume that you will only be<br>
given one or two-dimensional arrays.

> For example, flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9])<br> 
should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

## Prime Number Finder
Create a prime_finder() function that takes in a number, n, and returns all the<br>
prime numbers from 1 to n (inclusive). As a reminder, a prime number is a number<br>
that is only divisible by 1 and itself.

> For example, prime_finder(11) should return [2, 3, 5, 7, 11].


## Product of Everything Else
Create a product_of_the_others() function that takes in an array of integers and<br>
replaces each number in the array with the product of all the numbers in the array<br>
except the number at that index itself.

> For example, product_of_the_others([1, 2, 3, 4, 5]) should return [120, 60, 40, 30, 24],<br> 
and product_of_the_others([5, 5, 5]) should return [25, 25, 25].

## Reverse Words
Write a function, word_reverser(), that will take a given string and reverse the order<br> 
of the words. You may assume that the string is a sentence that contains only letters<br> 
and spaces, with all words separated by one space.

> For example, word_reverser("Codecademy rules") should return "rules Codecademy" and<br> 
word_reverser("May the Fourth be with you") should return "you with be Fourth the May".

## Top Score Sorter
Write a function, score_sorter(), that will take a list of unsorted scores along with<br>
the highest possible score. It should return a sorted list of all of the scores, in<br> 
descending order from high to low. You are expected to create and implement your own<br> 
sorting algorithm for this challenge.

> For example, score_sorter([1, 2, 3, 9999, 13], 10000) should return [9999, 13, 3, 2, 1].

## Unique Characters in a String
Write a unique_characters() function that determines if any given string has all unique<br> 
characters (i.e. no character in the string is duplicated). If the string has all unique<br> 
characters, the function should return True. If the string does not have all unique<br> 
characters, return False.

> For example, unique_characters("apple") should return False.

Note that if the function is called with an empty string (“”), the program should return<br> 
an error message.
