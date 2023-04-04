"""
1. What is the result of the code, and why?
&gt;&gt;&gt; def func(a, b=6, c=8):
print(a, b, c)
&gt;&gt;&gt; func(1, 2)

ANSWER...

The result of the code will be: 1 2 8. Here, the function func has 3 parameters: a, b, and c,
with default values for b and c. When the function is called with func(1, 2), the value of a
is set to 1, the value of b is set to 2, and the default value of c (which is 8) is used.

------------------------------------------------------------------------------------------------


2. What is the result of this code, and why?
&gt;&gt;&gt; def func(a, b, c=5):
print(a, b, c)
&gt;&gt;&gt; func(1, c=3, b=2)

ANSWER...

The result of the code will be: 1 2 3. Here, the function func has 3 parameters: a, b, and c,
with a default value for c. When the function is called with func(1, c=3, b=2), the value of
a is set to 1, the value of b is set to 2, and the value of c is set to 3, overriding the
default value of c.

------------------------------------------------------------------------------------------------


3. How about this code: what is its result, and why?
&gt;&gt;&gt; def func(a, *pargs):
print(a, pargs)
&gt;&gt;&gt; func(1, 2, 3)

ANSWER...

The result of the code will be: 1 (2, 3). Here, the function func has 1 required parameter
(a) and a variable-length argument list (*pargs). When the function is called with func(1, 2, 3),
the value of a is set to 1, and the remaining arguments (2 and 3) are collected into a tuple pargs.


------------------------------------------------------------------------------------------------


4. What does this code print, and why?
&gt;&gt;&gt; def func(a, **kargs):
print(a, kargs)
&gt;&gt;&gt; func(a=1, c=3, b=2)

ANSWER...

The result of the code will be: 1 {'c': 3, 'b': 2}. Here, the function func has 1 required
parameter (a) and a variable-length keyword argument list (**kargs). When the function is
called with func(a=1, c=3, b=2), the value of a is set to 1, and the remaining keyword
arguments (c=3 and b=2) are collected into a dictionary kargs.


------------------------------------------------------------------------------------------------


5. What gets printed by this, and explain?
&gt;&gt;&gt; def func(a, b, c=8, d=5): print(a, b, c, d)
&gt;&gt;&gt; func(1, *(5, 6))

ANSWER...

The result of the code will be: 1 5 6 5. Here, the function func has 3 parameters: a, b, and c,
with default values for c and d. When the function is called with func(1, *(5, 6)), the value
of a is set to 1, the value of b is unpacked from (5, 6) and set to 5, and the default value
of c (which is 8) is used, and the default value of d (which is 5) is used.


------------------------------------------------------------------------------------------------


6. what is the result of this, and explain?
&gt;&gt;&gt; def func(a, b, c): a = 2; b[0] = &#39;x&#39;; c[&#39;a&#39;] = &#39;y&#39;
&gt;&gt;&gt; l=1; m=[1]; n={&#39;a&#39;:0}
&gt;&gt;&gt; func(l, m, n)

&gt;&gt;&gt; l, m, n

ANSWER...

The result of the code will be: 1, ['x'], {'a': 'y'}. Here, the function func has 3 parameters:
a, b, and c. When the function is called with func(l, m, n), the value of l is set to 1, the
value of m is passed by reference and changed to ['x'], and the value of n is passed by reference
and changed to {'a': 'y'}. After the function call, the value of l remains 1, the value of m is
['x'], and the value of n is {'a': 'y'}.


------------------------------------------------------------------------------------------------


"""
