# quad-tree
A quadtree is a tree data structure in which each internal node has exactly four children. Quadtrees are the two-dimensional analog of octrees and are most often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. The data associated with a leaf cell varies by application, but the leaf cell represents a "unit of interesting spatial information".

The subdivided regions may be square or rectangular, or may have arbitrary shapes. This data structure was named a quadtree by Raphael Finkel and J.L. Bentley in 1974. A similar partitioning is also known as a Q-tree. All forms of quadtrees share some common features:

##### They decompose space into adaptable cells
##### Each cell (or bucket) has a maximum capacity. When maximum capacity is reached, the bucket splits
##### The tree directory follows the spatial decomposition of the quadtree.

### Types:
1.Region quadtree
2.Point quadtree
3.PR quadtree
4.Edge quadtree
5.PM quadtree

### Some common uses of quadtrees
1. Image representation
2. Bitmap and its compressed quadtree representation
3. Image processing
4. Mesh generation
5. Spatial indexing, point location queries, and range queries
6. Efficient collision detection in two dimensions
7. View frustum culling of terrain data
8. Storing sparse data, such as a formatting information for a spreadsheet[12] or for some matrix calculations[citation needed]
9. Solution of multidimensional fields (computational fluid dynamics, electromagnetism)
10.Conway's Game of Life simulation program.[13]
11.State estimation[14]
12.Quadtrees are also used in the area of fractal image analysis
13.Maximum disjoint sets

## Installation
clone this repository and execute the following commands:
   ##### to install requirements:
          pip install -r requirements.txt 
   ##### to try the code:
          python main.py
   Note:
   insert/query button switches b/n insert mode and query mode
   1.insert mode:
     click to insert node at that position
   2.query mode:
     click two points (topleft and bottom right of the query rectangle)
     
   ##### to use quadtree in other projects:
          import quadtree
          
## screen-shots
<img src="./outputs/bt.png">
