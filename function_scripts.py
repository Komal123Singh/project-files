{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome, to the world of Python\n",
      "First line is docstring. Displaying a welcome message.\n"
     ]
    }
   ],
   "source": [
    "#functions demons......!\n",
    "\n",
    "#defining a function...\n",
    "def myfun():\n",
    "    \"\"\"First line is docstring. Displaying a welcome message.\"\"\"\n",
    "    print('Welcome, to the world of Python')\n",
    "    return \n",
    "\n",
    "myfun() # calling a function...\n",
    "print(myfun.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age :17\n",
      "U r not elligible for voting\n"
     ]
    }
   ],
   "source": [
    "#function with parameters\n",
    "\n",
    "def validate(age):\n",
    "    if age>=18:\n",
    "        print(\"U r elligible for voting\")\n",
    "    else:\n",
    "        print(\"U r not elligible for voting\")\n",
    "\n",
    "user_age=int(input('Enter your age :'))\n",
    "validate(user_age)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter english marks :23\n",
      "Enter maths marks :45\n",
      "Enter science marks :34\n",
      "Result : Fail\n"
     ]
    }
   ],
   "source": [
    "def genResult(m1,m2,m3):\n",
    "    totalm=m1+m2+m3\n",
    "    percent=totalm/3\n",
    "    if percent >=50:\n",
    "        print('Result : Pass')\n",
    "    else:\n",
    "        print(\"Result : Fail\")\n",
    "\n",
    "eng=int(input(\"Enter english marks :\"))\n",
    "mat=int(input(\"Enter maths marks :\"))\n",
    "sc=int(input(\"Enter science marks :\"))\n",
    "\n",
    "genResult(eng,mat,sc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi.... Allen\n"
     ]
    }
   ],
   "source": [
    "#Python parameterised function with default values\n",
    "def myFun(name='Allen'):\n",
    "    print(\"Hi....\",name)\n",
    "    return\n",
    "\n",
    "myFun()"
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
      "My Details - Name : Smith  Age :  20\n"
     ]
    }
   ],
   "source": [
    "#Python function with keyword arguments\n",
    "def myFun(name,age):\n",
    "    print(\"My Details - Name :\",name,\" Age : \",age)\n",
    "    return\n",
    "\n",
    "myFun(age=20,name=\"Smith\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square of sum of two no. :  121\n"
     ]
    }
   ],
   "source": [
    "#Python - how to return a value from a function\n",
    "def sum(x,y):\n",
    "    return (x+y)\n",
    "\n",
    "def squarer(z):\n",
    "    print(\"Square of sum of two no. : \",(z*z))\n",
    "    \n",
    "    \n",
    "total = sum(5,6)\n",
    "squarer(total)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value of x before pasing :  10\n",
      "value of x inside myFun()  11\n",
      "value of x after pasing :  10\n"
     ]
    }
   ],
   "source": [
    "#Python - Pass-by-value\n",
    "def myFun(x):\n",
    "    x=x+1\n",
    "    print(\"value of x inside myFun() \",x)\n",
    "\n",
    "x=10\n",
    "print(\"value of x before pasing : \",x)\n",
    "myFun(x)\n",
    "print(\"value of x after pasing : \",x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value passed :  10  id: 140728463631024\n",
      "value received : 11  id :  140728463631056\n"
     ]
    }
   ],
   "source": [
    "#Python - Pass-by-ref\n",
    "def myFun(arg):\n",
    "    arg=arg+1\n",
    "    print('value received :',arg,' id : ',id(arg))\n",
    "    \n",
    "x=10\n",
    "print('value passed : ',x,' id:',id(x))\n",
    "myFun(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list before passing  [1, 2, 3]\n",
      "Modified list insdie a function is : [1, 2, 3, 4]\n",
      "list after passing  [1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "def myFun(list):\n",
    "    list.append(4)\n",
    "    print(\"Modified list insdie a function is :\",list)\n",
    "    \n",
    "mylist = [1,2,3]\n",
    "print(\"list before passing \",mylist)\n",
    "myFun(mylist)\n",
    "print(\"list after passing \",mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C\n",
      "C++\n",
      "Python\n",
      "DJango\n",
      "JAVA\n"
     ]
    }
   ],
   "source": [
    "#Python Arbitrary arguments\n",
    "\n",
    "def courseDetails(*cname):\n",
    "    \"\"\"This function courseDetails display all the courses.\"\"\"\n",
    "    \n",
    "    #cname is a tuple with arguments\n",
    "    for cr in cname:\n",
    "        print(cr)\n",
    "\n",
    "courseDetails(\"C\",\"C++\",\"Python\",\"DJango\",\"JAVA\")"
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
