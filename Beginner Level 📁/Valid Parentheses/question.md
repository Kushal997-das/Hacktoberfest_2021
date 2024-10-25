# Valid Parentheses

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Input
- A string `s`.

## Output
- `True` if the string is valid, `False` otherwise.

## Example
input : s = "([)]" 
output: False

input : s = "{[]}"
output: True

input : s = "()[]{}"
output: True
