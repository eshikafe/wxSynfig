Synfig-Reloaded
====================
wxPython port of Synfig with a focus on performance, stability, simplicity and platform nativity.

Development Strategy
--------------------
- Eliminate ETL and Boost. Use Python built-in modules as much as possible.
- Reduce the number of dependencies as much as possible.
- Speed up computationally intensive routines with Cython.
- Simplify the GUI and make it as intuitive as possible.
- Port mypaint brush library to Cython.
- Use Swig for C/C++ libraries only where there's no performance improvement over Cython.
- Use existing Python ports where applicable.

Dependencies
--------------
- Python 2.7.10
- wxPython 3.0


Entry Point:
- Run studio/src/gui/main.py

