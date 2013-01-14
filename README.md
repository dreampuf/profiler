# Profile Utils

Python library of profile tools

# Tools 

- mem_profiler
- line_profiler
- objgraph 

# Usage

## Step One - Install

    pip install git+https://github.com/dreampuf/profiler.git

## Step Two - Enable

    import profiler
    
    @profiler.line_profiler
    def THE_FUNC_OF_YOU_WANT_PROFILING():
        pass

## Step Three - Run

Just run your code like normally.

## Complete simple

    def test_fun():
        import time
        a = 2**2**16
        b = [{"a": 123}] * 1024 * 1024 * 20
        c = [0] * 1024 * 1024
        del b
        time.sleep(2)

    # when you want to profiling it
    import profiler
    @profiler.line_profiler
    def test_fun():
        # ...

    # when you run this code, you will get..

    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        79                                                   def test_fun():
        80         1           26     26.0      0.0              import time
        81         1         1208   1208.0      0.1              a = 2**2**16
        82         1       124101 124101.0      5.7              b = [{"a": 123}] * 1024 * 1024 * 10
        83         1         5086   5086.0      0.2              c = [0] * 1024 * 1024
        84         1        46671  46671.0      2.1              del b
    85         1      2001282 2001282.0     91.9              time.sleep(2)

more example in testcase.

