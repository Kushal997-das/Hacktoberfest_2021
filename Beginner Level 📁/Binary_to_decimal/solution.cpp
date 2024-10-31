#include <iostream>
#include <string>

int binaryToDecimal(const std::string &binaryStr)
{
    int decimalNumber = 0;

    // Iterate over each character in the binary string
    for (char bit : binaryStr)
    {
        // Shift decimal result to the left (multiply by 2)
        decimalNumber = decimalNumber * 2 + (bit - '0');
    }

    return decimalNumber;
}

int main()
{
    std::string binaryStr;
    std::cout << "Enter a binary number: ";
    std::cin >> binaryStr;

    int decimalResult = binaryToDecimal(binaryStr);
    std::cout << "Decimal representation: " << decimalResult << std::endl;

    return 0;
}
