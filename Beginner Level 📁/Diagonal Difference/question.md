matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = 1+ 5 + 9 = 15.
.The right to left diagonal =  3 +5 +9 = 17 . Their absolute difference is
|15-17| = 2 .
.

Function description

Complete the diagonal difference function in the editor below.

diagonalDifference takes the following parameter:

    int arr[n][m]: an array of integers

Return

    int: the absolute diagonal difference

Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix  arr .
Each of the next n lines describes a row, arr[i] , and consists of n space-separated integers arr[i][j]

.Constraints

-100 <= a[i][j]  <= 100

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.