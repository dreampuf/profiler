#!/usr/bin/env python
# vim: fileencoding=utf-8

__author__ = "dreampuf<soddyque@gmail.com>"

import os
import sys
from functools import wraps
try:
    from line_profiler import LineProfiler
except ImportError:
    sys.stderr.write("`pip install line_profiler` first please\n")

try:
    from memory_profiler import LineProfiler as MemeryProfiler, show_results
except ImportError:
    sys.stderr.write("`pip install memory_profiler` first please\n")

try:
    import objgraph
    import tempfile
    import subprocess
except ImportError:
    sys.stderr.write("`pip install objgraph` first please\n")

__all__ = ["line_profiler","memory_profiler","draw_it", "lprofiler", "mprofiler"]

lprofiler = LineProfiler()
def line_profiler(func):
    """Line Profiler function.

    @line_profiler
    def THE_FUNCTION_OF_YOU_WANT_PROFILE(*args, **kws):
        pass

    """
    profiled_func = lprofiler(func)
    @wraps(func)
    def inner(*args, **kws):
        ret = profiled_func(*args, **kws)
        lprofiler.print_stats()
        return ret
    return inner

mprofiler = MemeryProfiler()
def memory_profiler(func):
    """Memery Profiler function.

    @line_profiler
    def THE_FUNCTION_OF_YOU_WANT_PROFILE(*args, **kws):
        pass

    """
    profiled_func = mprofiler(func)
    @wraps(func)
    def inner(*args, **kws):
        ret = profiled_func(*args, **kws)
        show_results(mprofiler)
        return ret
    return inner

def draw_it(*args):
    """Draw and show it.

    """
    _, tmpf = tempfile.mkstemp(suffix='.png')
    objgraph.show_refs(args, filename=tmpf)
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', tmpf))
    elif os.name == 'nt':
        subprocess.call(('start', tmpf))
    elif os.name == 'posix':
        subprocess.call(('xdg-open', tmpf))

########## unittest ############
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        def test_fun():
            import time
            a = 2**2**16
            b = [{"a": 123}] * 1024 * 1024 * 20
            c = [0] * 1024 * 1024
            del b
            def innerfunc():
                time.sleep(1)
                return 1
                
            c = innerfunc()
            time.sleep(1)
        self.f = test_fun

    def test_draw_it(self):
        a = [i for i in xrange(100)]
        b = xrange(100)
        c = range(100)
        draw_it(a, b, c)

    def test_line_profiler(self):
        lp = line_profiler(self.f)
        lp()



    def test_memory_profiler(self):
        mp = memory_profiler(self.f)
        mp()
        
        @memory_profiler
        def g():
            return eval(repr(dict([(i, i) for i in xrange(1000)])))
        g()

if __name__ == "__main__":
    unittest.main()
        
