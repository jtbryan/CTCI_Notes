# Interview Coding Notes

<a href=#sliding-window>Sliding Window</a>

<a href=#two-pointers>Two Pointers</a>

<a href=#fast-and-slow-pointers>Fast and slow pointers</a>

<a href=#common-patterns>Common Patterns</a>

## Common Patterns
### Sources:
* https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

### **Sliding Window**
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--os4Lz5eD--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/h3h2h4s11pjgla88pqzp.png">

* **Description**: This is a pattern used to perform an operation on a window of an array or linked list given a size.
* **How to Identify**: Examples of indicators for these types of problems are as follows:
    * Maximum sum subarray of size 'K'
    * Longest substring with 'K' distinct character
    * String anagrams



### **Two Pointers**
<img src="https://hackernoon.com/images/G9YRlqC9joZNTWsi1ul7tRkO6tv1-x4da3w5y.jpg">

* **Description**: This is a pattern where two pointers iterate through the data structure in tandem until one or both hit a certain condition. This design is often 
* **How to Identify**: Some of the following indicators should provide insight into when to use this design pattern:
    * Dealing with sorted array or linked lists and need to find a set of elements that fulfill a certain condition
    * Examples:
        * Squaring a sorted array
        * Triplets that sum to zero
        * Comparing strings that contain backspaces

* **Example**: The following is an example of how we can use the tortoise and hare to find the middle of a linked list:

```python
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return

    p1 = head
    p2 = head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    
    return p1
```

### **Fast and Slow pointers**
<img src="https://media.licdn.com/dms/image/C4E12AQGFgaF0ZlO3yA/article-inline_image-shrink_1500_2232/0/1612410843906?e=1683158400&v=beta&t=2XdTy8i6JFNRP4Rkn7KaU0cdBOSdNOGfnUosSddp1N0">

* **Description**: Similar to the two pointer method, the fast and slow pointer method utilizes two pointers, also known as the Hare & Tortoise Algorithm. This approach is ideal when looking for a **cyclic** list. 
* **How to Identify**: The problem deals with a loop in a linked list or array or when you need the position of an element or length of a linked list. Here are some example problems for this pattern:
    * Linked List Cycle
    * Palindrome Linked List
    * Cycle in a Circular Array
* **When to use this over 2-pointer**: The two pointer method should not be used for a singly linked list. 

### **Merge Intervals** (array)
<img src="https://camo.githubusercontent.com/e091f6fc4d537308f6acf965f20c89e721aba762fc3806cf6091df1ff1cec84a/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f302a6339556e66416f4535736b52414c6c55">

* **Description**: This pattern is a technique used for merging overlapping intervals. For interval problems, there are 6 ways intervals can relate to each other:
    1. 'a' and 'b' do not overlap
    2. 'a' and 'b' overlap and 'b' ends after 'a'
    3. 'a' completely overlaps 'b'
    4. 'a' and 'b' overlap, 'a' ends after 'b'
    5. 'b' completely overlaps 'a'
    6. 'a' and 'b' do not overlap
* **How to Identify**: Indicators for this pattern can be identified if you are asked to produce a list with only mutually exclusive interval or if you hear the term 'overlapping intervals'. Examples of these problems:
    * Intervals intersection
    * Maximum CPU load

### **Cyclic sort**
* **Description**: 
