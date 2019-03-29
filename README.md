wxSynfig
====================
wxPython port of Synfig 

Objective
--------------------
- Make computational 2D graphics programming accessible to everyone and easy to learn 
- Performance, stability, simplicity and platform nativity.
- Test bed for 2D computer graphics experiments and research.

Roadmap
--------
- Publication to HTML5 Canvas


Dependencies
--------------
Windows
- Python 3.7.2
   - https://www.python.org/downloads/
- wxPython 4.0 or later
   - pip install wxPython=4.0.4

Linux (Ubuntu 18.10)
- Install the dependencies
    - sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
    
- Install pip3
    - pip3 install wxpython==4.0.4
    

Entry Point:
- Run studio/src/gui/main.py

Screenshot
-----------
![screenshot](https://github.com/eshikafe/wxSynfig/blob/master/studio/images/wxSynfig_py3.PNG)
