#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
// 널널하게 잡고, 카운트를 한 다음에 사이즈를 구하고 10의배수해서 숫자를 구하고 계산하기

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    
    int even[10];
    int odd[10];
    
    int a = 0;
    int b = 0;
    for(int i = 0; i < num_list_len; i++) {
        if (num_list[i] % 2 == 0) {
            even[a++] = num_list[i];
        } else {
            odd[b++] = num_list[i];

        }
    }
    
    int n = 0, m = 0;
    for (int i = 0; i < a; i++) {
        n += pow(10, (a-i-1)) * even[i];
    }
    
    for (int i = 0; i < b; i++) {
        m += pow(10, (b-i-1)) * odd[i];
    }
    
    return m+n;
}