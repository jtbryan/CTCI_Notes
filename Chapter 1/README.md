# Chapter 1 - Arrays and Strings

* For **subarray** and **substring** problems, we can use what's known as a sliding window algorithm. 
    * This involves having a "window" of 2 pointers, *left* and *right*, and you continuously increase the right pointer.
    * If the element at the right pointer makes the window invalid, we move the left pointer to shrink the window until it becomes valid again
    * The state of the window must be stored for this to work using a hash map to store the frequency of letter, or distinct integers,
    * Example code: 
    ```
    for(right = 0; right < n; right++):
    update window with element at right pointer
    while (condition not valid):
        remove element at left pointer from window, move left pointer to the right
    update global max
    ```
    * Example code to determine longest substring with no repeating characters:
    ```
    unordered_map<char, int> counts; // Frequencies of chars in the window
        int res = 0;
        int i = 0; // Left pointer
        for(int j = 0; j < s.length(); j++){
            counts[s[j]] ++; // Add right pointer to window 
            while(counts[s[j]] > 1){ // While the element at right pointer created a repeat
                counts[s[i++]] --; // While condition not valid, remove element at left pointer from window by decreasing its count, and then increment left pointer. In this case, it is while s[j] is a duplicate (we will stop after removing the duplicate copy of s[j]).
            } // Now the condition is valid
            res = max(res, j-i+1); // Update global max with the length of current valid substring
        }
        return res;
    ```