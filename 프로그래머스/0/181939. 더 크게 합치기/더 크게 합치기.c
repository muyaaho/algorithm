#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int a, int b) {
    int answer = 0;
    
    int tmp = a;
    int a_size = 0, b_size = 0;
    
    int ab[10];
    int ba[10];
    int aarr[10];
    int barr[10];
    
    
    while (tmp > 0) {
        if (tmp < 10) {
            aarr[a_size++] = tmp;
            break;
        }
        aarr[a_size++] = tmp % 10;
        tmp /= 10;
    }
    
    tmp = b;
    while (tmp > 0) {
        if (tmp < 10) {
            barr[b_size++] = tmp;
            break;
        }
        barr[b_size++] = tmp%10;
        tmp /= 10;
    }
    
    // printf("a_size, b_size = %d, %d\n", a_size, b_size);
    
    for (int i = 0; i < (a_size + b_size); i++) {
        if (i < a_size) {
            ab[i] = aarr[a_size - i - 1];
        } else {
            ab[i] = barr[b_size - i + a_size - 1];
        }
        // printf("ab[%d] = %d\n", i, ab[i]);
        
        if (i < b_size) {
            ba[i] = barr[b_size - i - 1];
        } else {
            ba[i] = aarr[a_size - i + b_size - 1];
        }
        // printf("ba[%d] = %d\n", i, ba[i]);
        
    }
    
    bool is_a = true;
    for (int i = 0; i < (a_size + b_size); i++) {
        if (ab[i] < ba[i]) {
            is_a = false;
            break;
        }
        else if (ab[i] > ba[i]) {
            break;
        }
    }
    
    if (is_a) {
        for (int i = 0 ; i < (a_size + b_size); i++) {
            answer += pow(10, (a_size + b_size - i - 1)) * ab[i];
        }
    }
    else {
        for (int i = 0 ; i < (a_size + b_size); i++) {
            answer += pow(10, (a_size + b_size - i - 1)) * ba[i];
        }
    }
    
    
    return answer;
}