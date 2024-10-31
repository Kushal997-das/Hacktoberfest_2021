### Problem Statement

Write a function that converts a binary number, given as a string, to its decimal (base-10) equivalent.

### Input

- A single string `binaryStr` representing a binary number. The string will contain only characters `'0'` and `'1'`.
  
### Output

- An integer representing the decimal (base-10) equivalent of the binary number.

### Constraints

- `1 <= binaryStr.length <= 32` (assuming a maximum of 32 bits for simplicity).
- `binaryStr` will always represent a valid binary number (no invalid characters).
- The input binary number does not contain leading zeros unless it is `"0"`.

### Examples

#### Example 1
- **Input:** `"101"`
- **Output:** `5`
  
  **Explanation:** \(1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 4 + 0 + 1 = 5\)

#### Example 2
- **Input:** `"1111"`
- **Output:** `15`
  
  **Explanation:** \(1 \times 2^3 + 1 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 4 + 2 + 1 = 15\)

#### Example 3
- **Input:** `"0"`
- **Output:** `0`

### Function Signature

```cpp
int binaryToDecimal(const std::string& binaryStr);
```

### Hints

1. Iterate over each character in the binary string, treating it as a bit.
2. For each bit, update the decimal result by shifting left (multiplying by 2) and adding the bit value (0 or 1).
  
### Edge Cases

- A single `"0"` should return `0`.
- A single `"1"` should return `1`.
- Very large binary numbers up to 32 bits.
