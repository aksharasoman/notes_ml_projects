- A special type of tree.
- elements are organized in a specific way
- Two types:
	- Min Heap
		- Smallest value is always at the top (root).
		- Each parent is smaller than its children
		- uses to find K-largest values
	- Max Heap
		- Largest value is at the root.
		- Each parent is larger than its children
		- uses to find K-smallest values.
![[images/Pasted image 20241114122516.png]]

### Algorithm
Find k *smallest* values in the list of ‘n’ elements
1. Create a *max*-heap of size *‘k’* with first k elements.
2. For the next element:
	1. If larger than the root → No change
	2. If smaller than the root → Replace root with this value
3. Continue step 2 until the end of list

> Why **heaps** are efficient? because we always know where the largest/smallest value is - At the root.
> 	Allows access to largest or smallest element in O(1) time.
> 	 Inserting or removing elements take O(log n) time.
> 	

