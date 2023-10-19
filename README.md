# Pattern-Matching
This project focuses on implementing three different pattern matching algorithms to determine whether a specific string pattern occurs in a given text. The algorithms employed are Brute Force, Boyer-Moore-Horspool, and Knuth-Morris-Pratt. Each algorithm provides a unique approach to pattern matching, allowing users to choose the most suitable one for their specific use case.

Pattern Matching Algorithms
1. Brute Force
The Brute Force algorithm is a straightforward technique that involves checking all positions in the text for a match against the pattern. While simple, it can be inefficient for large texts due to its time complexity.

2. Boyer-Moore-Horspool Algorithm
The Boyer-Moore-Horspool algorithm is a more efficient approach that skips multiple characters in the text based on the mismatched character's occurrence in the pattern. This reduces the number of comparisons required, making it faster than the Brute Force method.

3. Knuth-Morris-Pratt Algorithm
The Knuth-Morris-Pratt algorithm improves efficiency further by using information from previous comparisons to avoid redundant checks. It preprocesses the pattern to create a "failure function," allowing the algorithm to skip unnecessary comparisons, making it particularly efficient for large texts.
