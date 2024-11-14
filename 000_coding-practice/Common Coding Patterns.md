
Related Notes:
[[Main Points to Remember - DSA Coding Problems]]
[[Dumpyard of Code Snippets]]

**Good References:**
- [LeetCode Was Hard Until I Learned THESE 8 Patterns (With Templates!) - YouTube](https://youtu.be/RYT08CaYq6A)
- All code snippets: [https://algo.monster/templates](https://algo.monster/templates)

---

- reusable solutions to common problems that you might encounter in programming, especially during interviews or software development. 

- Two types of datastructures 
	- Linear
		- Arrays
		- Linked List
		- Strings
	- Non-linear
		- Trees
			- a graph with no cycles.
		- Graphs

### Linear Patterns:
1. **Two Pointers**:
   - Used to traverse data structures like arrays or linked lists with two different pointers moving at different speeds.
   - Two pointers can move in 
	   - same direction (used for single-pass data processing: O(n) time instead of O(n2) ) or opposite directions (ideal for finding pairs).
	   - different speeds (eg: one in x steps while other 2x etc)
   - **Common use-cases**: Finding pairs that meet a condition, removing duplicates, and detecting cycles in a linked list.

2. **Sliding Window**:
   - Involves creating a window that slides over the data
   - for dynamically managing a range within a data structure
   - helps analyze continuous segments 
   - ideal for substring and subarray problems.
   - **Common use-cases**: Maximum sum subarray, finding substrings, and other problems that require maintaining a dynamic range.

3. **Binary Search**:
   - to search for a target value in a sorted array.
   - A divide-and-conquer approach  (O(log n) time)
   - left, mid and right pointers
   - **Common use-cases**: Searching, finding bounds, and optimized problem-solving with logarithmic complexity.
   - [[binary_search/binary search|binary search code snippet]]
### Non-Linear Patterns
- **[[Graph Traversal]] with BFS & DFS** 
- **[[000_coding-practice/Backtracking|Backtracking]]**
	- Self-built Dynamic DFS 
	- recursion
- **Priority Queue**
	- for top-K problems
	- Most common implementation: [[Heap]]
- [[Dynamic Programming (DP)]]
   

3. **Greedy Algorithm**:
   - Building up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
   - **Common use-cases**: Problems involving minimal spanning trees, shortest paths, and scheduling tasks.
4. **Divide and Conquer**:
   - Breaking a problem into smaller subproblems, solving each independently, and combining the results.
   - **Common use-cases**: Sorting algorithms like merge sort and quicksort, and searching in multidimensional data.
5. **Topological Sorting**:
   - Ordering vertices in a directed acyclic graph (DAG) such that for every directed edge, the start comes before the end.
   - **Common use-cases**: Task scheduling, dependency resolution, and project planning.

### **Why Coding Patterns Matter**
- **Efficiency**: Knowing these patterns helps you come up with optimized solutions more quickly.
- **Reusability**: Once you master these patterns, you can adapt them to solve different variations of problems.
- **Interview Success**: Most technical interview problems are based on these fundamental patterns.

![[images/Screenshot 2024-11-13 at 11.03.44 PM.png]]
