#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
 
typedef long long ll;
typedef vector<ll> poly;
 
ll pw(ll a, ll b, ll mod){
    ll ret = 1;
    while(b){
        if(b & 1) ret = ret * a % mod;
        b >>= 1; a = a * a % mod;
    }
    return ret;
}
 
template<ll mod, ll w>
class NTT{
public:
    void ntt(poly &f, bool inv = 0){
        int n = f.size(), j = 0;
        vector<ll> root(n >> 1);
        for(int i=1; i<n; i++){
            int bit = (n >> 1);
            while(j >= bit){
                j -= bit; bit >>= 1;
            }
            j += bit;
            if(i < j) swap(f[i], f[j]);
        }
        ll ang = pw(w, (mod - 1) / n, mod); if(inv) ang = pw(ang, mod - 2, mod);
        root[0] = 1; for(int i=1; i<(n >> 1); i++) root[i] = root[i-1] * ang % mod;
        for(int i=2; i<=n; i<<=1){
            int step = n / i;
            for(int j=0; j<n; j+=i){
                for(int k=0; k<(i >> 1); k++){
                    ll u = f[j | k], v = f[j | k | i >> 1] * root[step * k] % mod;
                    f[j | k] = (u + v) % mod;
                    f[j | k | i >> 1] = (u - v) % mod;
                    if(f[j | k | i >> 1] < 0) f[j | k | i >> 1] += mod;
                }
            }
        }
        ll t = pw(n, mod - 2, mod);
        if(inv) for(int i=0; i<n; i++) f[i] = f[i] * t % mod;
    }
    vector<ll> multiply(poly &_a, poly &_b){
        vector<ll> a(all(_a)), b(all(_b));
        int n = 2;
        while(n < a.size() + b.size()) n <<= 1;
        a.resize(n); b.resize(n);
        ntt(a); ntt(b);
        for(int i=0; i<n; i++) a[i] = a[i] * b[i] % mod;
        ntt(a, 1);
        return a;
    }
};
 
ll ext_gcd(ll a, ll b, ll &x, ll &y) { //ax + by = gcd(a, b)
  ll g = a; x = 1, y = 0;
  if (b) g = ext_gcd(b, a % b, y, x), y -= a / b * x;
  return g;
}
 
const ll m1 = 2281701377, m2 = 2483027969, m3 = 998244353;
NTT<m1, 3> ntt1;
NTT<m2, 3> ntt2;
NTT<m3, 3> ntt3;
 
ll f(const vector<ll> &a, ll mod){
    int sz = a.size();
    vector<ll> rmn(sz), lm(sz, 1);
    ll ans = 0, M = 1;
    vector<ll> m({m1, m2, m3}); //prime list
 
    for(int i=0; i<sz; i++){
        ll k = a[i] - rmn[i]; k %= m[i];
        if(k < 0) k += m[i];
        ll x, y;
        ext_gcd(lm[i], m[i], x, y);
        k *= x; k %= m[i];
        if(k < 0) k += m[i];
        ans += k * M % mod;
        ans %= mod;
        for(int t=i+1; t<sz; t++){
            rmn[t] += lm[t] * k;
            rmn[t] %= m[t];
            lm[t] *= m[i];
            lm[t] %= m[t];
        }
        M *= m[i]; M %= mod;
    }
    return ans;
}
 
poly multiply(poly &a, poly &b, ll mod){
    poly a1(a), a2(a), a3(a);
    poly b1(b), b2(b), b3(b);
    poly res1 = ntt1.multiply(a1, b1);
    poly res2 = ntt2.multiply(a2, b2);
    poly res3 = ntt3.multiply(a3, b3);
    poly ret(res1.size());
    for(int i=0; i<res1.size(); i++){
        ret[i] = f({res1[i], res2[i], res3[i]}, mod);
    }
    return ret;
}

int main(){
    
}