class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> st;
        if(n==1) return true;
        while(n!=1){

             if(st.find(n) != st.end()) {
                return false;
            }

            st.insert(n);

            int sum = 0;
        while(n>0){
            int a = n%10;
            sum = sum + a*a;
            n = n/10;
        }

        n = sum;
           if(n==1) return true;
        }
        return false;
        
    }
};