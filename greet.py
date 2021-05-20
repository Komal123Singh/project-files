{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myFun():\n",
    "    print(\"Hello , John ....How r r u....!\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-fbf0d77b0d1e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mgreet\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mgreet\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmyFun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\greet.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m    \u001b[1;34m\"outputs\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import greet\n",
    "\n",
    "greet.myFun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.3862943611198906"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Python - rename the imported module\n",
    "# alisas- as\n",
    "import math as cal\n",
    "\n",
    "cal.log(4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'module_name'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-df017c257f2c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Python : module- from keyword\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmodule_name\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mfun_name\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfun2_name\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'module_name'"
     ]
    }
   ],
   "source": [
    "#Python : module- from keyword\n",
    "from module_name import fun_name, fun2_name\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-5-474289ae8ecc>, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-5-474289ae8ecc>\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    or\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Python : module- from keyword\n",
    "from greet import *\n",
    "\n",
    "myFun('Jonh')\n",
    "add(2,3)\n",
    "\n",
    "or\n",
    "\n",
    "import greet\n",
    "\n",
    "greet.myFun('John')\n",
    "greet.add(2,3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in module math:\n",
      "\n",
      "NAME\n",
      "    math\n",
      "\n",
      "DESCRIPTION\n",
      "    This module provides access to the mathematical functions\n",
      "    defined by the C standard.\n",
      "\n",
      "FUNCTIONS\n",
      "    acos(x, /)\n",
      "        Return the arc cosine (measured in radians) of x.\n",
      "    \n",
      "    acosh(x, /)\n",
      "        Return the inverse hyperbolic cosine of x.\n",
      "    \n",
      "    asin(x, /)\n",
      "        Return the arc sine (measured in radians) of x.\n",
      "    \n",
      "    asinh(x, /)\n",
      "        Return the inverse hyperbolic sine of x.\n",
      "    \n",
      "    atan(x, /)\n",
      "        Return the arc tangent (measured in radians) of x.\n",
      "    \n",
      "    atan2(y, x, /)\n",
      "        Return the arc tangent (measured in radians) of y/x.\n",
      "        \n",
      "        Unlike atan(y/x), the signs of both x and y are considered.\n",
      "    \n",
      "    atanh(x, /)\n",
      "        Return the inverse hyperbolic tangent of x.\n",
      "    \n",
      "    ceil(x, /)\n",
      "        Return the ceiling of x as an Integral.\n",
      "        \n",
      "        This is the smallest integer >= x.\n",
      "    \n",
      "    copysign(x, y, /)\n",
      "        Return a float with the magnitude (absolute value) of x but the sign of y.\n",
      "        \n",
      "        On platforms that support signed zeros, copysign(1.0, -0.0)\n",
      "        returns -1.0.\n",
      "    \n",
      "    cos(x, /)\n",
      "        Return the cosine of x (measured in radians).\n",
      "    \n",
      "    cosh(x, /)\n",
      "        Return the hyperbolic cosine of x.\n",
      "    \n",
      "    degrees(x, /)\n",
      "        Convert angle x from radians to degrees.\n",
      "    \n",
      "    erf(x, /)\n",
      "        Error function at x.\n",
      "    \n",
      "    erfc(x, /)\n",
      "        Complementary error function at x.\n",
      "    \n",
      "    exp(x, /)\n",
      "        Return e raised to the power of x.\n",
      "    \n",
      "    expm1(x, /)\n",
      "        Return exp(x)-1.\n",
      "        \n",
      "        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.\n",
      "    \n",
      "    fabs(x, /)\n",
      "        Return the absolute value of the float x.\n",
      "    \n",
      "    factorial(x, /)\n",
      "        Find x!.\n",
      "        \n",
      "        Raise a ValueError if x is negative or non-integral.\n",
      "    \n",
      "    floor(x, /)\n",
      "        Return the floor of x as an Integral.\n",
      "        \n",
      "        This is the largest integer <= x.\n",
      "    \n",
      "    fmod(x, y, /)\n",
      "        Return fmod(x, y), according to platform C.\n",
      "        \n",
      "        x % y may differ.\n",
      "    \n",
      "    frexp(x, /)\n",
      "        Return the mantissa and exponent of x, as pair (m, e).\n",
      "        \n",
      "        m is a float and e is an int, such that x = m * 2.**e.\n",
      "        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.\n",
      "    \n",
      "    fsum(seq, /)\n",
      "        Return an accurate floating point sum of values in the iterable seq.\n",
      "        \n",
      "        Assumes IEEE-754 floating point arithmetic.\n",
      "    \n",
      "    gamma(x, /)\n",
      "        Gamma function at x.\n",
      "    \n",
      "    gcd(x, y, /)\n",
      "        greatest common divisor of x and y\n",
      "    \n",
      "    hypot(x, y, /)\n",
      "        Return the Euclidean distance, sqrt(x*x + y*y).\n",
      "    \n",
      "    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)\n",
      "        Determine whether two floating point numbers are close in value.\n",
      "        \n",
      "          rel_tol\n",
      "            maximum difference for being considered \"close\", relative to the\n",
      "            magnitude of the input values\n",
      "          abs_tol\n",
      "            maximum difference for being considered \"close\", regardless of the\n",
      "            magnitude of the input values\n",
      "        \n",
      "        Return True if a is close in value to b, and False otherwise.\n",
      "        \n",
      "        For the values to be considered close, the difference between them\n",
      "        must be smaller than at least one of the tolerances.\n",
      "        \n",
      "        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That\n",
      "        is, NaN is not close to anything, even itself.  inf and -inf are\n",
      "        only close to themselves.\n",
      "    \n",
      "    isfinite(x, /)\n",
      "        Return True if x is neither an infinity nor a NaN, and False otherwise.\n",
      "    \n",
      "    isinf(x, /)\n",
      "        Return True if x is a positive or negative infinity, and False otherwise.\n",
      "    \n",
      "    isnan(x, /)\n",
      "        Return True if x is a NaN (not a number), and False otherwise.\n",
      "    \n",
      "    ldexp(x, i, /)\n",
      "        Return x * (2**i).\n",
      "        \n",
      "        This is essentially the inverse of frexp().\n",
      "    \n",
      "    lgamma(x, /)\n",
      "        Natural logarithm of absolute value of Gamma function at x.\n",
      "    \n",
      "    log(...)\n",
      "        log(x, [base=math.e])\n",
      "        Return the logarithm of x to the given base.\n",
      "        \n",
      "        If the base not specified, returns the natural logarithm (base e) of x.\n",
      "    \n",
      "    log10(x, /)\n",
      "        Return the base 10 logarithm of x.\n",
      "    \n",
      "    log1p(x, /)\n",
      "        Return the natural logarithm of 1+x (base e).\n",
      "        \n",
      "        The result is computed in a way which is accurate for x near zero.\n",
      "    \n",
      "    log2(x, /)\n",
      "        Return the base 2 logarithm of x.\n",
      "    \n",
      "    modf(x, /)\n",
      "        Return the fractional and integer parts of x.\n",
      "        \n",
      "        Both results carry the sign of x and are floats.\n",
      "    \n",
      "    pow(x, y, /)\n",
      "        Return x**y (x to the power of y).\n",
      "    \n",
      "    radians(x, /)\n",
      "        Convert angle x from degrees to radians.\n",
      "    \n",
      "    remainder(x, y, /)\n",
      "        Difference between x and the closest integer multiple of y.\n",
      "        \n",
      "        Return x - n*y where n*y is the closest integer multiple of y.\n",
      "        In the case where x is exactly halfway between two multiples of\n",
      "        y, the nearest even value of n is used. The result is always exact.\n",
      "    \n",
      "    sin(x, /)\n",
      "        Return the sine of x (measured in radians).\n",
      "    \n",
      "    sinh(x, /)\n",
      "        Return the hyperbolic sine of x.\n",
      "    \n",
      "    sqrt(x, /)\n",
      "        Return the square root of x.\n",
      "    \n",
      "    tan(x, /)\n",
      "        Return the tangent of x (measured in radians).\n",
      "    \n",
      "    tanh(x, /)\n",
      "        Return the hyperbolic tangent of x.\n",
      "    \n",
      "    trunc(x, /)\n",
      "        Truncates the Real x to the nearest Integral toward 0.\n",
      "        \n",
      "        Uses the __trunc__ magic method.\n",
      "\n",
      "DATA\n",
      "    e = 2.718281828459045\n",
      "    inf = inf\n",
      "    nan = nan\n",
      "    pi = 3.141592653589793\n",
      "    tau = 6.283185307179586\n",
      "\n",
      "FILE\n",
      "    (built-in)\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "help(math)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'math'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Python- Atrributes of Module\n",
    "#  name,doc,file,dict\n",
    "\n",
    "#__name__ -(is used to return the name of a module)\n",
    "\n",
    "import math\n",
    "\n",
    "math.__name__\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This module provides access to the mathematical functions\\ndefined by the C standard.'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Python- Atrributes of Module\n",
    "#  name,doc,file,dict\n",
    "\n",
    "#__doc__\n",
    "\n",
    "import math\n",
    "\n",
    "math.__doc__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Rajesh\\\\Anaconda3\\\\lib\\\\io.py'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Python- Atrributes of Module\n",
    "#  name,doc,file,dict\n",
    "\n",
    "#__file__ (hold the name & path of the module)\n",
    "\n",
    "import io\n",
    "\n",
    "io.__file__\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'__name__': 'math',\n",
       " '__doc__': 'This module provides access to the mathematical functions\\ndefined by the C standard.',\n",
       " '__package__': '',\n",
       " '__loader__': _frozen_importlib.BuiltinImporter,\n",
       " '__spec__': ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),\n",
       " 'acos': <function math.acos(x, /)>,\n",
       " 'acosh': <function math.acosh(x, /)>,\n",
       " 'asin': <function math.asin(x, /)>,\n",
       " 'asinh': <function math.asinh(x, /)>,\n",
       " 'atan': <function math.atan(x, /)>,\n",
       " 'atan2': <function math.atan2(y, x, /)>,\n",
       " 'atanh': <function math.atanh(x, /)>,\n",
       " 'ceil': <function math.ceil(x, /)>,\n",
       " 'copysign': <function math.copysign(x, y, /)>,\n",
       " 'cos': <function math.cos(x, /)>,\n",
       " 'cosh': <function math.cosh(x, /)>,\n",
       " 'degrees': <function math.degrees(x, /)>,\n",
       " 'erf': <function math.erf(x, /)>,\n",
       " 'erfc': <function math.erfc(x, /)>,\n",
       " 'exp': <function math.exp(x, /)>,\n",
       " 'expm1': <function math.expm1(x, /)>,\n",
       " 'fabs': <function math.fabs(x, /)>,\n",
       " 'factorial': <function math.factorial(x, /)>,\n",
       " 'floor': <function math.floor(x, /)>,\n",
       " 'fmod': <function math.fmod(x, y, /)>,\n",
       " 'frexp': <function math.frexp(x, /)>,\n",
       " 'fsum': <function math.fsum(seq, /)>,\n",
       " 'gamma': <function math.gamma(x, /)>,\n",
       " 'gcd': <function math.gcd(x, y, /)>,\n",
       " 'hypot': <function math.hypot(x, y, /)>,\n",
       " 'isclose': <function math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)>,\n",
       " 'isfinite': <function math.isfinite(x, /)>,\n",
       " 'isinf': <function math.isinf(x, /)>,\n",
       " 'isnan': <function math.isnan(x, /)>,\n",
       " 'ldexp': <function math.ldexp(x, i, /)>,\n",
       " 'lgamma': <function math.lgamma(x, /)>,\n",
       " 'log': <function math.log>,\n",
       " 'log1p': <function math.log1p(x, /)>,\n",
       " 'log10': <function math.log10(x, /)>,\n",
       " 'log2': <function math.log2(x, /)>,\n",
       " 'modf': <function math.modf(x, /)>,\n",
       " 'pow': <function math.pow(x, y, /)>,\n",
       " 'radians': <function math.radians(x, /)>,\n",
       " 'remainder': <function math.remainder(x, y, /)>,\n",
       " 'sin': <function math.sin(x, /)>,\n",
       " 'sinh': <function math.sinh(x, /)>,\n",
       " 'sqrt': <function math.sqrt(x, /)>,\n",
       " 'tan': <function math.tan(x, /)>,\n",
       " 'tanh': <function math.tanh(x, /)>,\n",
       " 'trunc': <function math.trunc(x, /)>,\n",
       " 'pi': 3.141592653589793,\n",
       " 'e': 2.718281828459045,\n",
       " 'tau': 6.283185307179586,\n",
       " 'inf': inf,\n",
       " 'nan': nan}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Python- Atrributes of Module\n",
    "#  name,doc,file,dict\n",
    "\n",
    "#__dict__ (return the dictionary objectb of a module)\n",
    "\n",
    "import math\n",
    "\n",
    "math.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__doc__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " 'acos',\n",
       " 'acosh',\n",
       " 'asin',\n",
       " 'asinh',\n",
       " 'atan',\n",
       " 'atan2',\n",
       " 'atanh',\n",
       " 'ceil',\n",
       " 'copysign',\n",
       " 'cos',\n",
       " 'cosh',\n",
       " 'degrees',\n",
       " 'e',\n",
       " 'erf',\n",
       " 'erfc',\n",
       " 'exp',\n",
       " 'expm1',\n",
       " 'fabs',\n",
       " 'factorial',\n",
       " 'floor',\n",
       " 'fmod',\n",
       " 'frexp',\n",
       " 'fsum',\n",
       " 'gamma',\n",
       " 'gcd',\n",
       " 'hypot',\n",
       " 'inf',\n",
       " 'isclose',\n",
       " 'isfinite',\n",
       " 'isinf',\n",
       " 'isnan',\n",
       " 'ldexp',\n",
       " 'lgamma',\n",
       " 'log',\n",
       " 'log10',\n",
       " 'log1p',\n",
       " 'log2',\n",
       " 'modf',\n",
       " 'nan',\n",
       " 'pi',\n",
       " 'pow',\n",
       " 'radians',\n",
       " 'remainder',\n",
       " 'sin',\n",
       " 'sinh',\n",
       " 'sqrt',\n",
       " 'tan',\n",
       " 'tanh',\n",
       " 'tau',\n",
       " 'trunc']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "dir(math)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
