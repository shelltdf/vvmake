# vvmake

one man call him self AV. so he`s make call VVMAKE.

```
pip install vvmake
```



# vvmake_config.py

you mast add this py file to your project root dir. for example:

```python
from vvmakelib import vv

def dependency():
    if vv.FIND("include/pcl.h"):
        print("error")
        return False
    return True

def make():
	OPT = ""
    vv.CMAKE(OPT)
    
def install():
    vv.INSTALL()
    
def package():
    vv.PACKAGE()
    
```



# vvmake.py

```
cd source_dir

vvmake build -idir d:/dev
vvmake build -debug
vvmake build -debug -static

vvmake install
vvmake install -debug
vvmake install -debug -static

vvmake test

vvmake package

```

