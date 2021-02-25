import runpy
import sys

sys_argv = sys.argv

def test():
    # SUITE: python_fnmatch
    sys.argv = sys_argv + [
        '--matcher', 'pywildmatch',
        '--suite', 'python_fnmatch',
        '--results', 'pywildmatch'
    ]
    runpy.run_module(
        'pywildmatch.test',
        run_name='__main__',
        init_globals={'sys.argv': sys.argv}
    )

    # SUITE: libgit2
    sys.argv = sys_argv + [
        '--matcher', 'pywildmatch',
        '--suite', 'libgit2',
        '--results', 'pywildmatch'
    ]
    runpy.run_module(
        'pywildmatch.test',
        run_name='__main__',
        init_globals={'sys.argv': sys.argv}
    )

    # SUITE: pywildmatch
    sys.argv = sys_argv + [
        '--matcher', 'pywildmatch',
        '--suite', 'pywildmatch',
        '--results', 'pywildmatch'
    ]
    runpy.run_module(
        'pywildmatch.test',
        run_name='__main__',
        init_globals={'sys.argv': sys.argv}
    )


test()
