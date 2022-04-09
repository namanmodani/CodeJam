// Google Code Jam 2022
// Double or One Thing
// Naman Modani

#include <iostream>
#include <string>

using namespace std;

int main() {
  
  int t;
  cin >> t;
    
  for (int r = 0; r < t; ++r) {
    string s;
    cin >> s;
    string v;
    v.push_back(s[0]);
    int i = 0;
    
    while (i + 1 < s.size()) {
      char cur = v.back();
      char next = s[i + 1];
      int diff = (int)next - (int)cur;
      
      if (diff > 0) {
        v.push_back(cur);
        v.push_back(next);
      }
      else if (diff < 0) {
        v.push_back(next);
      }
      else {
        string h;
        h.push_back(cur);
        h += s.substr(i + 1);
        string g = s.substr(i + 1);
        if (h.compare(g) <= 0) {
          v.push_back(cur);
          v.push_back(next);
        }
        else {
          v.push_back(next);
        }
      }
      ++i;
    }
    printf("Case #%d: %s\n", r + 1, v.c_str());
  }
  return 0;
}
