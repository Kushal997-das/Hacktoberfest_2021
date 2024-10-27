// main code
class Solution {
    public int maxArea(int[] height) {
        int l=0, r=height.length-1;
        int max_a=0;

        while(l<r){
            int area=(r-l)* Math.min(height[l],height[r]);
            max_a= Math.max(max_a,area);

            if(height[l] > height[r]){
                r--;
            }
            else{
                l++;
            }
        }
        return max_a;
    }
}

//driver code for test cases
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};

        // Call the maxArea method and print the result
        int result = solution.maxArea(height);
        System.out.println("Maximum area: " + result);
    }
}

