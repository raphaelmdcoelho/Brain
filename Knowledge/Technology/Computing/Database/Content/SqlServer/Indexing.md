
## Concepts

Indexes are used to enhance the performance of your database queries. They are special `data structures` that help speed up the retrieval of rows from a table. They are similar to the index of a book.

A index can be created on one or more columns of a table and provides a fast way to look up data based on those columns.

Indexes are tipically implemented as a balanced tree (B-tree) or a hash table.

A `B-tree` is a type of self-balancing tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations.

A **B-tree index** organizes the data in a tree-like structure, where nodes contain **keys** (values from the indexed column) and **pointers** to the data or other nodes.

The keys are kept sorted at each level of the tree, allowing efficient traversal from the root node to the leaf nodes.

```css
           [50]
          /    \
     [20, 40]  [70, 90]
     /   |   \   /   |   \
   ...  ...  ... ... ...  ...
```

In this B-tree, if you're looking for the value `70`, you start at the root `[50]` and move right.

A **hash table** is another type of data structure used to implement database indexes, especially for **equality searches** (e.g., finding a specific value like `customer_id = 123`). A hash table uses a hash function to convert a key (like `customer_id`) into an index in an array.

#technology #computing #database #sqlserver 