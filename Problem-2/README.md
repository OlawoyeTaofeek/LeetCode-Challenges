# Solving Turing Practice Test Problem 1- 

### BaseBall Game
You are keeping scores for a baseball game with strange rule. The game consists of several rounds where the scores of the past rounds may affect future round scores.
At the beginning of the game, you start with an empty record. You are given a list of string 'ops' where ops[i] is the ith operation you must apply to the record and is one of the following. 
1. An integer X- Record a new score of x
2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score 

- Return the Sum of all tyhe scores on the record .


Example 1:

Input: ops = ['5', '2', 'C', 'D', '+']
Output: 30
Explanation: 
"5" - Add 5 to the record, record is now [5]
"2" - Add 2 to the record, record is now [5 , 2]
"C" - Invalidate and remove the previous score, record is now [5]
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10]
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15]
- The total sum is 5 + 10 + 15 = 30 


Example 1:

Input: ops = ['5', '-2', '4', 'C', 'D', '9', '+', '+']
Output: 27
Explanation: 
"5" - Add 5 to the record, record is now [5]
"-2" - Add -2 to the record, record is now [5 , -2]
"4" - Add 4 to the record, record is now [5 , -2, 4]
"C" - Invalidate and remove the previous score, record is now [5, -2]
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4]
"9" - Add 9 to the record, record is now [5 , -2, -4, 9]
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5]
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14]
- The total sum is 5 + (-2) + (-4) + 9 + 5 + 14 = 27



Example 3:

Input: ops = ['1']
Output: 1
Explanation: 
'1' - Add 1 to the record, record is now [1]
The total sum is 1