# Some Traditional algorithms for Object Segmentation

# OverSegmentation using Superpixel Algorithm.  

Getting superpixels of the image using the scikit-image python package
Four methods for Super-pixel Classification:  
a) Felenszwalb's efficient graph based segmentation.         
b) Quickshift image segmentation.                            
c) SLIC -K-Means based image segmentation.                   
d) Compact watershed segmentation of gradient images.

# GrabCut Algorithm 

GrabCut is an iterative algorithm that combines statistics and Graph Cuts technique in order to accomplish detailed 
2D segmentation with very limited input, originally developed at MICROSOFT RESEARCH CAMBRIDGE.

The user input three things: background pixels, foreground pixels, unknown part of the image. (Normally done by selecting a rectangle, and assigning the part inside the rectangle as unknown and the rest as background class).

GRABCUT ALGORITHM OVERVIEW:

1)The user input three things: background pixels, foreground pixels, unknown part of the image. (Normally done by selecting a rectangle, and assigning the part inside the rectangle as unknown and the rest as background class).

2) The foreground and background are modeled as Gaussian Mixture Models (GMMs) using any clustering algorithm.

3) Then every pixel in the foreground assigned most probable Gaussian component in foreground GMMs. The same process id done with the pixels in the background but with the background GMMs.

4) New GMMs are learned from the pixel sets that were created in the previous step.

5) A graph is built and Graph Cut is used to find a new classification of foreground and background pixels.

6) Repeat steps 3 to 5 over and over again until classification converges 
