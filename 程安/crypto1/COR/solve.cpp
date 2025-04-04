#include<bits/stdc++.h>
using namespace std;
#define int long long
#define LEN(a) (sizeof(a)/sizeof(a[0]))
int result[]={1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1};
typedef unsigned int uint;

class LFSR{
    public:
        unsigned int state,tap,size;
        LFSR(unsigned int state,unsigned int tap, uint size):
            state{state},tap{tap},size{size} {};
        int getbit(){
            int f=__builtin_popcountll(state & tap) & 1;
            int ret = state & 1;
            state >>= 1;
            state |= f << (size - 1);
            return ret;
        }
        void backward() {
            int o = (state >> (size - 1)) & 1;
            state <<= 1;
            state &= (1 << size) -1;
            if((__builtin_popcountll((state | 1) & tap) & 1) == o)
                state |= 1;
        }
};

double cal_cor(int a[],int b[]){
    int count = 0;
    const int total = 200;
    for(int i=0;i<total;i++){
        if(a[i] == b[i]) count++;
    }
    return (double)count / total;
}

vector<unsigned int> get_state(unsigned int tap,uint size){
    int output[200];
    vector<unsigned int> vec;
    for(unsigned int state = 0;state < 1ll << size;state++){
        LFSR lfsr = LFSR(state,tap,size);
        for (int i = 0; i < 232; i++){
            lfsr.getbit();
        }
        for(int i=0;i<200;i++){
            output[i]=lfsr.getbit();
        }
        double cor = cal_cor(output, &result[LEN(result) - 200]);
        if(cor >= 0.7){
            vec.push_back(state);
        }
    }
    return vec;
}

signed main(){
    unsigned char flag[(LEN(result)-200)/8+1]={0};
    int output[200];
    unsigned int origin_states[3],taps[3],size[3] = {27,23,25};
    vector<vector<unsigned int>> states;
    taps[0] = (1 << 26) | (1 << 16) | (1 << 13) | 1;
    taps[1] = (1 << 22) | (1 << 7) | (1 << 5) | 1;
    taps[2] = (1 << 24) | (1 << 19) | (1 << 17) | 1;
    for(int i=1;i<3;i++){
        states.push_back(get_state(taps[i],size[i]));
    }
    for(unsigned int state1 : states[0]){
        for(unsigned int state2 : states[1]){
            for(unsigned int state0 = 0; state0 < 1ll <<size[0];state0++){
                LFSR lfsr0 = LFSR(state0, taps[0], size[0]);
                LFSR lfsr1 = LFSR(state1, taps[1], size[1]);
                LFSR lfsr2 = LFSR(state2, taps[2], size[2]);
                int x0,x1,x2;
                for (int i = 0; i < 232; i++){
                    x0=lfsr0.getbit();
                    x1=lfsr1.getbit();
                    x2=lfsr2.getbit();
                }
                for(int i=0;i<200;i++){
                    x0=lfsr0.getbit();
                    x1=lfsr1.getbit();
                    x2=lfsr2.getbit();
                    output[i] = x0 ? x1 : x2;
                }
                double cor = cal_cor(output, &result[LEN(result) - 200]);
                if(cor >= 1){
                    origin_states[0] = state0;
                    origin_states[1] = state1;
                    origin_states[2] = state2;
                    goto final;
                }
            }
        }
    }
final:
    LFSR lfsr0 = LFSR(origin_states[0], taps[0], size[0]);
    LFSR lfsr1 = LFSR(origin_states[1], taps[1], size[1]);
    LFSR lfsr2 = LFSR(origin_states[2], taps[2], size[2]);
    for(int i=0;i<29;i++){
        for(int j=0;j<8;j++){
            int x0,x1,x2,o;
            x0 = lfsr0.getbit();
            x1 = lfsr1.getbit();
            x2 = lfsr2.getbit();
            o = x0 ? x1 :x2;
            flag[i] |= (result[i*8+j] ^ o) << (7-j); 
        }
    }
    cout<<flag;
}