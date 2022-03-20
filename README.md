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

vvmake.py build -idir d:/dev

vvmake.py install

vvmake.py test

vvmake.py package

```

