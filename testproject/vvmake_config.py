from vvmakelib import vv

def dependency():
    if vv.FIND("include/pcl.h"):
        print("error")
        return False
    return True

def make(vvconfig):
    OPT = ""
    vv.CONFIGURE(vvconfig,OPT)
    vv.BUILD(vvconfig)
    
def install(vvconfig):
    vv.INSTALL(vvconfig)
    
def package(vvconfig):
    vv.PACKAGE(vvconfig)
    
    