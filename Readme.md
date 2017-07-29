# data visualization in python
this is the basic data visualization stuff that every CS engineer know.
## Definitions

* Visualization is the graphical presentation of information, with the goal of providing the viewer with a qualitative understanding of the information contents.
* Information may be data, processes, relations, or concepts.
* Graphical presentation may entail manipulation of graphical entities (points, lines, shapes, images, text) and attributes (color, size, position, shape).
* Understanding may involve detection, measurement, and comparison, and is enhanced via interactive techniques and providing the information from multiple views and with      multiple techniques. 

## Characteristics of Data

* Numeric, symbolic (or mix)
* Scalar, vector, or complex structure
* Various units
* Discrete or continuous
* Spatial, quantity, category, temporal, relational, structural
* Accurate or approximate
* Dense or sparce
* Ordered or non-ordered
* Disjoint or overlapping
* Binary, enumerated, multilevel
* Independent or dependent
* Multidimensional
* Single or multiple sets
* May have similarity or distance metric
* May have intuitive graphical representation (e.g. temperature with color)
* Has semantics which may be crucial in graphical consideration 

## What is the dimension of data?

Assume function with a domain and range. If for every x and y we have temperature t and pressure p, 
'''

    f(x, y) -> (t, p)

    f1(x, y) -> t, f2(x, y) -> p

    f3(x, y, t) -> 0 or 1, f4(x, y, p) -> 0 or 1

    f5(x, y, t, p) -> 0 or 1 

The key is that the mapping must go to a single value (or vector), e.g. f(x, t) -> 0 or more values of elements with position x and temp t,

therefore losing information (e.g. hidden surfaces in projection). This is OK for statistics (e.g. histogram). 

## Graphical entities and attributes

* Entity: point, line, polyline, glyph, surface, solid, image, text
* Attribute: color/intensity, location, style, size, relative position/motion 

## What do we see and how well do we see it?

* Different viewers perceive different graphical/spatial/color in different degrees
* Context varies our sensitivity
* According to one researcher (Cleveland), in increasing inaccuracy 

    1. Position along a common scale
    2. Position along identical, non-aligned scales
    3. Length
    4. Angle/slope
    5. Area
    6. Volume
    7. Hue/saturation/intensity (informally derived) 

* Weber's law - detection is proportional to percent change, not scale
* Stevens' law - perceived scale is proportional to a power of the actual scale.

## What makes a good visualization?

* Examine cardinality of dimension with detectible variations in graphics (see below for evaluation under human perception)
* Use scaling and offset to fit in range
* Use derived values (residuals, logs) to emphasize changes
* Use projections, other combinations, to compress information, get statistics
* Use random jiggling to separate overlaps
* Use multiple views to handle hidden relations, high dimensions
* Use effective grids, keys and labels to aid understanding 

## Interacting with the data

* Dynamically adjust mapping
* Tour data by varying views
* Labeling to get original data
* Deleting to eliminate clutter
* Brushing/Highlighting to see correspondence in multiple views
* Zooming to focus attention
* Panning to explore neighborhoods 

## Common Techniques

* Charts: bar or pie
* Graphs: good for structure, relationships
* Plots: 1- to n-dimensional
* Maps: one of most effective
* Images: use color/intensity instead of distance (surfaces)
* 3-D surfaces and solids
* isosurfaces/slices
* translucency
* stereopsis
* animation 


