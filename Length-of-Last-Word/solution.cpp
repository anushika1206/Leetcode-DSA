class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0;
        int n = s.size()-1;
        while(n>=0 && s[n]==' '){//for trailing spaces
            n--;
        }
        while(n>=0 && s[n]!=' '){
            cnt += 1;
            n--;
        }
        return cnt;
    }
};