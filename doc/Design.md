wxSynfig Design Document
=============================


# Folder Structure
Here is an overview of the wxSynfig source code folder structure
```bash
|- wxSynfig
|----src
|    |- core/
|    |  |- examples/
|    |  |- modules/
|    |  |- po/
|    |  |- synfig/
|    |  |- test/
|    |  |- tool/
|    |- ETL/          ==> Extended Template Library (ported from C++ to Rust)
|    |  |- cpp/
|    |  |- src/
|    |  |- test/
|    |- studio/
|    |  |- brushlib/  ==> Brush library
|    |  |- gui/       ==> GUI source code files (ported from C++ to Python)
|    |  |- images/    ==> All images and icons are stored here
|    |  |- plugins/   ==> Plugin folder
|    |  |- synfigapp/
|----doc
      |- Design.md
```
# Source Code Description
