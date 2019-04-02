# wall-annotate

An image annotator, intended for eventual use in a crowd simulation/analysis context.

Usage: ```python wall_annotate.py [some image]```
* Click, drag, and release to draw a rectangle when in drawing mode
* When in delete mode, click on a drawn rectangle to delete it
* When in normal mode, click on a drawn rectangle to highlight its entry on the listbox

Current features:
* Display an image on the canvas
* Draw rectangles on the canvas
* Delete rectangles on the canvas
* Maintains a list of drawn rectangles and their coordinates

Planned features:
* Editable objects, for revision
* Export list of objects and coordinates

https://svn.python.org/projects/python/trunk/Demo/tkinter/matt/canvas-moving-w-mouse.py

Uses the tkinter Python library.

