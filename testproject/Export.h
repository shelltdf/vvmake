#ifndef _FOO_EXPORT_H
#define _FOO_EXPORT_H

#if defined(_MSC_VER) || defined(__CYGWIN__) || defined(__MINGW32__) || defined( __BCPLUSPLUS__)  || defined( __MWERKS__)
#if defined(FOO_LIBRARY_STATIC)
#   define FOO_EXPORT
#elif defined(FOO_LIBRARY)
#   define FOO_EXPORT __declspec(dllexport)
#else
#   define FOO_EXPORT __declspec(dllimport)
#endif
#else
#define FOO_EXPORT
#endif

#endif //_FOO_EXPORT_H

