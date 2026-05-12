class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        /*APPROACH 1
        vector<int> v;
        for(int num:nums){
            vector<int> temp;
            while(num>0){
                temp.push_back(num%10);
                num = num/10;
            }
            reverse(temp.begin(),temp.end());

            for(int x : temp){
                v.push_back(x);
            }
        }
        return v;
        */

        vector<int> v;
        for(int num:nums){
            string s = to_string(num);
            for(char c:s){
                v.push_back(c -'0');//ascii value
            }
        }
        return v;
    }
};