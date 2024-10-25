// C++ Program to sort an array of 0s, 1s and 2s
// by counting the occurrence of 0s, 1s and 2s

#include <iostream>
#include <vector>

void sort012(std::vector<int> &arr)
{
    int low = 0, mid = 0, high = arr.size() - 1;

    while (mid <= high)
    {
        switch (arr[mid])
        {
        case 0:
            std::swap(arr[low], arr[mid]);
            low++;
            mid++;
            break;
        case 1:
            mid++;
            break;
        case 2:
            std::swap(arr[mid], arr[high]);
            high--;
            break;
        }
    }
}

int main()
{
    std::vector<int> arr = {0, 1, 2, 1, 0, 2, 1, 0, 2};

    sort012(arr);

    std::cout << "Sorted array: ";
    for (int num : arr)
    {
        std::cout << num << " ";
    }

    return 0;
}
