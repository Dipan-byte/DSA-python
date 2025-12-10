#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    int freq[10000] = {0}; // adjust if needed

    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        freq[arr[i]]++;
    }

    int found = 0;

    for(int i = 0; i < n; i++){
        if(freq[arr[i]] > 1){
            printf("First Repeating Element: %d", arr[i]);
            found = 1;
            break;
        }
    }

    if(!found)
        printf("No repeating element");

    return 0;
}
