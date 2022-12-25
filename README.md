# Hoshen-Kopelman Algorithm
This is an implementation of the Hoshen-Kopelman (HoKo) Algorithm for cluster labelling in one-dimensional and two-dimensional matrices. The project is still in its early stages and I am hoping to evolve it into a three-dimensional adaptation.

## The Algorithm
The basic idea behind Hoshen-Kopelman algorithm is to perform a [raster scan](https://en.wikipedia.org/wiki/Raster_scan) in a top-down, left-right manner of the two-dimensional array in question to perform cluster counting and labelling. Diagonal percolation is not considered.

The true power of this algorithm shines when we must work with very large matrices. In such matrices, the sizes of the clusters can also be correspondingly large and thus, if we tried to relabel an entire cluster, we would have significant overhead. Instead, the Hoshen-Kopelman algorithm maintains a separate data structure wherein, we can 'note' that cluster number ```x``` is actually the same as cluster number ```y```. In practice, this is done via negative numbers.

## Files in This Repository
* The script ```gridgenerator.py``` serves as a module wherein, I have defined functions for generating either randomized, or user-input-based matrices.
* The one-dimensional case is rather trivial and I have included it just as an exercise in ```onedimension.py```.
* The file ```twodimensions.py``` is where the true heart of the codebase resides. The function ```countClusters()``` takes in a matrix of zeros and ones, where one corresponds to an occupied site, and labels clusters by applying the HoKo algorithm.

Note that while HoKo algorithm does not involve relabelling clusters with their root labels, I have deliberately included a function ```renameClusters()``` for this purpose for my own sake. As far as the algorithm goes, it can be skipped.

## To-Do
1. Check for very large matrices.
2. Find a way to display the matrices properly. A preferred way would be via graphics. At the very least, the percolation should be clearly visible.
3. Generalize for three dimensions.
