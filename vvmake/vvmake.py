
import os.path
import sys
# import vvmakelib as vm
# from vvmakelib import test
# from vvmakelib import vv
import vvmake.vv
from vvmake.vv import VVCONFIG


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
    
    
    vvmake.vv.CWD = os.getcwd()
    
    vvconfig = VVCONFIG()
    # ARG_ARCH = "vs2019-64"
    
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
                # ARG_ARCH = sys.argv[arg_num+1].strip('\r')
                
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
    
    
    if(vvconfig.vv_target_arch == "vs2005-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 8 2005" '
    if(vvconfig.vv_target_arch == "vs2005-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 8 2005 Win64" '
        
    if(vvconfig.vv_target_arch == "vs2008-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 9 2008" '
    if(vvconfig.vv_target_arch == "vs2008-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 9 2008 Win64" '
    
    if(vvconfig.vv_target_arch == "vs2010-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 10 2010" '
    if(vvconfig.vv_target_arch == "vs2010-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 10 2010 Win64" '
    
    if(vvconfig.vv_target_arch == "vs2012-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 11 2012" '
    if(vvconfig.vv_target_arch == "vs2012-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 11 2012 Win64" '
    
    if(vvconfig.vv_target_arch == "vs2013-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 12 2013" '
    if(vvconfig.vv_target_arch == "vs2013-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 12 2013 Win64" '
    
    if(vvconfig.vv_target_arch == "vs2015-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 14 2015" '
    if(vvconfig.vv_target_arch == "vs2015-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 14 2015 Win64" '
        
    if(vvconfig.vv_target_arch == "vs2017-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 15 2017" '
    if(vvconfig.vv_target_arch == "vs2017-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 15 2017 Win64" '
        
    if(vvconfig.vv_target_arch == "vs2019-32"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 16 2019" -A Win32'
    if(vvconfig.vv_target_arch == "vs2019-64"):
        vvconfig.vv_cmake_cfg = ' -G "Visual Studio 16 2019" -A x64'

    if(vvconfig.vv_target_arch == "mingw-32"):
        vvconfig.vv_cmake_cfg = ' -G "MSYS Makefiles" '
    if(vvconfig.vv_target_arch == "mingw-64"):
        vvconfig.vv_cmake_cfg = ' -G "MSYS Makefiles" '

    if(vvconfig.vv_target_arch == "nmake"):
        vvconfig.vv_cmake_cfg = ' -G "NMake Makefiles" '
        
    if(vvconfig.vv_target_arch == "unix"):
        #vvconfig.vv_cmake_cfg = ' -G "Unix Makefiles" '
        #vvconfig.vv_cmake_cfg = ' -G "Kate - Unix Makefiles" '
        vvconfig.vv_cmake_cfg = ' -G "CodeBlocks - Unix Makefiles" '
        #vvconfig.vv_cmake_cfg = ' -G "CodeBlocks - Ninja" '

    if(vvconfig.vv_target_arch == "ndk"):
        vvconfig.vv_cmake_cfg = ' -G "NMake Makefiles" '
        # vvconfig.vv_cmake_cfg = ' -G "MSYS Makefiles" '
        # vvconfig.vv_cmake_cfg = ' -G "Unix Makefiles" '
        
    if(vvconfig.vv_target_arch == "ninja"):
        vvconfig.vv_cmake_cfg = ' -G Ninja'
        
    if(vvconfig.vv_target_arch == "em"):
        vvconfig.vv_cmake_cfg = True
        vvconfig.vv_cmake_cfg = False
        # vvconfig.vv_cmake_cfg = ' -G "NMake Makefiles" '
        vvconfig.vv_cmake_cfg = ' -G Ninja '
        
    # print (dict_config)
    
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

