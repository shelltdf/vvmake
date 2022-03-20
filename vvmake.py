
import os.path
import sys
# import vvmakelib as vm
# from vvmakelib import test
from vvmakelib import vv
from vvmakelib.vv import VVCONFIG


def loadScript(str_name):

    #find script
    e = os.path.isfile(str_name + ".py") 
    if(e == False):
        print (str_name + " is not exist")
        return False
        
    #dir
    print( "os.getcwd() = " + os.getcwd())
    sys.path.append(os.getcwd())

    #import script
    pk = __import__(str_name)
    # val = getattr(s, str_name)

    return pk
    
    
def main():
    
    # test
    # print("hello world")
    # test.vvmake_test()
    
    
    vv.CWD = os.getcwd()
    
    vvconfig = VVCONFIG()
    
    #
    for arg_num in range(len(sys.argv)):
        strclip = sys.argv[arg_num].strip('\r')
        
        if strclip == "build" or strclip == "install" or strclip == "test" or strclip == "package":
            vvconfig.vv_mode = strclip
                
        # if strclip == "build":
            # vv_mode = strclip
            # if(arg_num < len(sys.argv)-1):
                # vv_install_dir = sys.argv[arg_num+1]
        
        # if strclip == "-pdir" or strclip == "-project_dir":
            # if(arg_num < len(sys.argv)-1):
                # vvconfig.vv_project_dir = sys.argv[arg_num+1].strip('\r')
        
        if strclip == "-idir" or strclip == "-install_dir":
            if(arg_num < len(sys.argv)-1):
                vvconfig.vv_install_dir = sys.argv[arg_num+1].strip('\r')
                
        if strclip == "-a" or strclip == "-arch":
            if(arg_num < len(sys.argv)-1):
                vvconfig.vv_target_arch = sys.argv[arg_num+1].strip('\r')
                
        if strclip == "-release":
            vvconfig.vv_release_debug = "release"
        if strclip == "-debug":
            vvconfig.vv_release_debug = "debug"
        if strclip == "-dynamic":
            vvconfig.vv_dynamic_static = "dynamic"
        if strclip == "-static":
            vvconfig.vv_dynamic_static = "static"
        # if strclip == "-only":
            # ARG_ONLIY = True   
    
    #
    vvconfig.print_info()

    #
    if(vvconfig.vv_mode == "help"):
        print("help")
        return
        

    # load vvmake_config.py
    # vvmake_config = loadScript(vvconfig.vv_project_dir + "/" + vvconfig.vv_project_script)
    vvmake_config_py = loadScript(vvconfig.vv_project_script)
    if(not vvmake_config_py):
        print("vvmake_config.py error")
        return
    
    # 
    if(vvconfig.vv_mode == "build"):
        vvmake_config_py.make(vvconfig)
        
    if(vvconfig.vv_mode == "install"):
        vvmake_config_py.install(vvconfig)
        
    # if(vvconfig.vv_mode == "test"):
        # vvmake_config_py.test()
        
    if(vvconfig.vv_mode == "package"):
        vvmake_config_py.package(vvconfig)
        
    
    
if __name__ == '__main__':
    main()

