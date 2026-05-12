/*Approach 1
class MinStack {
public:
    stack <pair<int,int>> st;
    MinStack() {
        
    }
    
    void push(int val) {
        if(st.empty()) st.push({val,val});
        else{
            st.push({val,min(val,st.top().second)});
        }
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return st.top().second;
    }
};
*/

class MinStack {
public:
    stack<long long> st;
    long long min;

    MinStack() {
        
    }
    
    void push(int val) {

        long long x = val;

        if(st.empty()) {
            min = x;
            st.push(x);
        }
        else {

            if(x >= min) {
                st.push(x);
            }
            else {
                st.push(2LL * x - min);
                min = x;
            }
        }
    }
    
    void pop() {

        long long x = st.top();
        st.pop();

        if(x < min) {
            min = 2LL * min - x;
        }
    }
    
    int top() {

        long long x = st.top();

        if(x >= min) {
            return x;
        }

        return min;
    }
    
    int getMin() {
        return min;
    }
};
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */