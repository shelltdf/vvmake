
import os

CWD = ""

class VVCONFIG:
    
    # mode
    vv_mode = 'help'
    
    # project dir
    # vv_project_dir = './'
    
    # install dir
    vv_install_dir = 'c:/dev'
    
    # current project python script
    vv_project_script = 'vvmake_config' # vvmake_config.py
    
    # target setting
    vv_target_arch = 'vs2019-64' # vc gcc clang 32 64
    vv_dynamic_static = 'dynamic'
    vv_release_debug = 'release'
    
    # 
    vv_cmake_cfg = ''
    
    def print_info(self):
        print( "vv_mode = " + self.vv_mode )
        # print( "vv_project_dir = " + self.vv_project_dir )
        print( "vv_install_dir = " + self.vv_install_dir )
        print( "vv_project_script = " + self.vv_project_script )
        print( "vv_target_arch = " + self.vv_target_arch )
        print( "vv_dynamic_static = " + self.vv_dynamic_static )
        print( "vv_release_debug = " + self.vv_release_debug )
        
 
def my_exec( str_cmd ):
    print ("exec - "  + str_cmd)
    
    if(True):
        os.system(str_cmd)
    else:
        ps = subprocess.Popen(str_cmd)
        ps.wait()
        
def my_build_and_install_dir(vvconfig):
    dir_name = ""
    dir_name += vvconfig.vv_target_arch
    
    if(vvconfig.vv_dynamic_static == 'static'):
        dir_name += '_static'
    if(vvconfig.vv_dynamic_static == 'dynamic'):
        dir_name += '_dynamic'
        
    # if(dict_config['arch'][:2]=="vs"):
        # return dir_name
        
    if(vvconfig.vv_release_debug == 'debug'):
        dir_name += '_debug'
    if(vvconfig.vv_release_debug == 'release'):
        dir_name += '_release'
    return dir_name
    
def my_into_build_dir( str_name , vvconfig ):

    if(os.path.isdir("vvbuild")==False):
        os.system( "mkdir vvbuild" )
    os.chdir( "vvbuild" )
    
    dir_name = my_build_and_install_dir(vvconfig)
        
    if(os.path.isdir(dir_name)==False):
        os.system( "mkdir " + dir_name)
    os.chdir( dir_name )
    
    # if(os.path.isdir(str_name)==False):
        # os.system( "mkdir " + str_name )
    # os.chdir( str_name )

def my_out_build_dir( str_name ):
    # os.chdir( ".." )
    # os.chdir( ".." )
    # os.chdir( ".." )
    os.chdir( CWD )

    
        
def FIND(filename):
    print("FIND " + filename)
    e = os.path.isfile(filename) 
    return e
    
def CONFIGURE(vvconfig , OPT):
    print("CONFIGURE")
    
    my_into_build_dir( '' ,vvconfig )
    dir_name = my_build_and_install_dir(vvconfig)
    
    # global CWD

    BUILD_TYPE = ""
    BUILD_STATIC_LIB = ""
    if(vvconfig.vv_dynamic_static == 'static'):
        BUILD_STATIC_LIB = " -DBUILD_SHARED_LIBS=0"
    if(vvconfig.vv_dynamic_static == 'dynamic'):
        BUILD_STATIC_LIB = " -DBUILD_SHARED_LIBS=1"
        
    # if(force_static):
        # BUILD_STATIC_LIB = " -DBUILD_SHARED_LIBS=0"
    
    if(vvconfig.vv_target_arch[:2]!="vs"):
        if(vvconfig.vv_release_debug == 'debug'):
            BUILD_TYPE = ' -DCMAKE_BUILD_TYPE=debug'
        if(vvconfig.vv_release_debug == 'release'):
            BUILD_TYPE = ' -DCMAKE_BUILD_TYPE=release'
        
    source_dir = '../../'
    # source_dir = str_local_dir
    # if(source_dir == ""):
        # source_dir = "../../../source/"
    
    # e = os.path.isfile("CMakeCache.txt") 
    # if(e):
        # print str_name + "configure is exist"
    # else:
    # my_exec( "cmake "+source_dir+"/" + str_name + "/" + str_subdir +
    
    if(vvconfig.vv_target_arch == "ndk"):
        # pass
        cmake_string = "cmake " + source_dir
        cmake_string += ' -DCMAKE_TOOLCHAIN_FILE=' + ANDROID_NDK_PATH + '/build/cmake/android.toolchain.cmake'+ dict_config['cmake_cfg']
        cmake_string += ' -DCMAKE_INSTALL_PREFIX="../../../install/' + dir_name + '"'
        cmake_string += ' -DANDROID_ABI=' + ANDROID_ABI
        cmake_string += ' -DANDROID_NATIVE_API_LEVEL=' + str(ANDROID_API_LEVEL)
        
        # cmake_string += ' -DANDROID'
        cmake_string += ' -DJ=8' #+ str(CPU_NUM)
        # cmake_string += " -DCMAKE_ANDROID_API="+str(ANDROID_API_LEVEL)
        # cmake_string += " -DCMAKE_ANDROID_API_MIN="+str(ANDROID_API_LEVEL)
        # cmake_string += ' -DANDROID_NDK=' + ANDROID_NDK_PATH
        
        if(dict_config['dynamic']==True):
            # cmake_string += ' -DANDROID_STL=gnustl_shared '
            cmake_string += ' -DANDROID_STL=c++_shared '
        else:
            # cmake_string += ' -DANDROID_STL=gnustl_static '
            cmake_string += ' -DANDROID_STL=c++_static '
        
        if(dict_config['debug']==True):
            cmake_string += ' -DCMAKE_BUILD_TYPE=debug'
        if(dict_config['release']==True):
            cmake_string += ' -DCMAKE_BUILD_TYPE=release'
            
        cmake_string += OPT
        my_exec(cmake_string)
        
    elif(vvconfig.vv_target_arch == "em"):
        my_exec( "emcmake cmake "+source_dir+
        " -DCMAKE_USE_RELATIVE_PATHS=1 -DCMAKE_INSTALL_PREFIX='../../../install/" + dir_name + "' " +
        vvconfig.vv_cmake_cfg + BUILD_TYPE + BUILD_STATIC_LIB + OPT )
        
    else:
        my_exec( "cmake "+source_dir+
        " -DCMAKE_USE_RELATIVE_PATHS=1" +
        # " -DCMAKE_CODEBLOCKS_MAKE_ARGUMENTS=-j2" +
        # " -DCMAKE_SYSROOT=" + CWD + "'/rootfs'" +
        # " -DCMAKE_INSTALL_PREFIX='../../../install/" 
        " -DCMAKE_INSTALL_PREFIX='" + vvconfig.vv_install_dir + "/" 
        + dir_name + "' " +
        vvconfig.vv_cmake_cfg + BUILD_TYPE + BUILD_STATIC_LIB + OPT )
    
    my_out_build_dir( '' )
    
    
def BUILD(vvconfig):
    print("BUILD")
    
    my_into_build_dir( '' ,vvconfig)
    current_dir = os.getcwd()
    system_ret = 0
    
    if(vvconfig.vv_target_arch[:2]=="vs"):
        if(vvconfig.vv_release_debug == 'debug'):
            system_ret = os.system('msbuild ALL_BUILD.vcxproj -maxcpucount:16 /p:Configuration=Debug')
            # system_ret = os.system('msbuild ALL_BUILD.vcxproj /p:Configuration=Debug')
        if(vvconfig.vv_release_debug == 'release'):
            system_ret = os.system('msbuild ALL_BUILD.vcxproj -maxcpucount:16 /p:Configuration=Release')
            # system_ret = os.system('msbuild ALL_BUILD.vcxproj /p:Configuration=Release')
            
    elif(vvconfig.vv_target_arch=="nmake"):
        system_ret = os.system('nmake')
        
    elif(vvconfig.vv_target_arch=="unix"):
        system_ret = os.system('make -j 8')
        
    elif(vvconfig.vv_target_arch=="ninja"):
        system_ret = os.system('ninja -j 8')
        
    elif(vvconfig.vv_target_arch=="ndk"):
        system_ret = os.system('nmake')
        
    elif(vvconfig.vv_target_arch=="em"):
        # system_ret = os.system('set CL=/MP nmake')
        system_ret = os.system('ninja -j 8')
        
    else:
        system_ret = os.system('make')
        
    my_out_build_dir( '' )
    
    
    # error
    global CWD
    if(system_ret != 0):
        # print("error = " + CWD)
        print("error = " + current_dir)
        sys.exit(1)
        
    
def INSTALL(vvconfig):
    print("INSTALL")
    
    my_into_build_dir( '' ,vvconfig)
    
    if(vvconfig.vv_target_arch[:2]=="vs"):
        if(vvconfig.vv_release_debug == 'debug'):
            os.system('msbuild INSTALL.vcxproj /p:Configuration=Debug')
        if(vvconfig.vv_release_debug == 'release'):
            os.system('msbuild INSTALL.vcxproj /p:Configuration=Release')
            
    elif(vvconfig.vv_target_arch=="nmake"):
        os.system('nmake install')
        
    elif(vvconfig.vv_target_arch=="unix"):
        os.system('make install')
        
    elif(vvconfig.vv_target_arch=="ninja"):
        os.system('ninja install')
        
    elif(vvconfig.vv_target_arch=="ndk"):
        os.system('nmake install')
        
    elif(vvconfig.vv_target_arch=="em"):
        # os.system('nmake install')
        os.system('ninja install')
        
    else:
        os.system('make install')
        
    my_out_build_dir( '' )
    
    
def PACKAGE(vvconfig):
    print("PACKAGE")
    
    my_into_build_dir( '' ,vvconfig)
    
    os.system('cpack')
    
    my_out_build_dir( '' )
    
    