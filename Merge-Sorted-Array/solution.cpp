class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> arr;
        for(int i = 0;i<m;i++){
            if(nums1[i]!=0){
                arr.push_back(nums1[i]);
            }
        }
        for(int j = 0;j<n;j++){
            if(nums2[j]!=0){
                arr.push_back(nums2[j]);
            }
        }
        sort(arr.begin(),arr.end());
        for(int a =0;a<arr.size();a++){
            nums1[a]= arr[a];
        }
    }
};