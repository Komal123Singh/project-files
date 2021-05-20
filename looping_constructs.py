{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABC\n"
     ]
    }
   ],
   "source": [
    "print(\"ABC\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over list\n",
    "mylist=[2,4,6,8,10]\n",
    "for i in mylist:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "101\n",
      "Patrick\n",
      "Python\n",
      "80\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over tuple\n",
    "mytuple=(101,\"Patrick\",\"Python\",80)\n",
    "for i in mytuple:\n",
    "    print(i)"
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
      "\n",
      "Average : 30.0\n"
     ]
    }
   ],
   "source": [
    "marks=[10,20,30,40,50]\n",
    "sum=0\n",
    "for m1 in marks:\n",
    "    sum+=m1 #sum=sum+m1\n",
    "avg = sum/len(marks)\n",
    "print('\\nAverage :',avg)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('IND', 'INDIA')\n",
      "('CHN', 'CHINA')\n",
      "('GER', 'GERMANY')\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over dictionary\n",
    "dict={\"IND\":\"INDIA\",\"CHN\":\"CHINA\",\"GER\":\"GERMANY\"}\n",
    "for pair in dict.items():\n",
    "    print(pair)\n"
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
      "Key : IND, Value = INDIA\n",
      "Key : CHN, Value = CHINA\n",
      "Key : GER, Value = GERMANY\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over dictionary\n",
    "dict={\"IND\":\"INDIA\",\"CHN\":\"CHINA\",\"GER\":\"GERMANY\"}\n",
    "for k,v in dict.items():\n",
    "    print(\"Key : \"+k+\", Value = \"+v)"
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
      "IND\n",
      "CHN\n",
      "GER\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over dictionary\n",
    "dict={\"IND\":\"INDIA\",\"CHN\":\"CHINA\",\"GER\":\"GERMANY\"}\n",
    "for k in dict.keys():\n",
    "    print(k)"
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
      "IND INDIA\n",
      "CHN CHINA\n",
      "GER GERMANY\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over dictionary\n",
    "dict={\"IND\":\"INDIA\",\"CHN\":\"CHINA\",\"GER\":\"GERMANY\"}\n",
    "for k in dict.keys():\n",
    "    print(k,dict.get(k))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P\n",
      "y\n",
      "t\n",
      "h\n",
      "o\n",
      "n\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration over Strings\n",
    "\n",
    "for char in \"Python\":\n",
    "    print(char)"
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
      "Enter any no.4\n",
      "4  *  1  =  4\n",
      "4  *  2  =  8\n",
      "4  *  3  =  12\n",
      "4  *  4  =  16\n",
      "4  *  5  =  20\n",
      "4  *  6  =  24\n",
      "4  *  7  =  28\n",
      "4  *  8  =  32\n",
      "4  *  9  =  36\n",
      "4  *  10  =  40\n"
     ]
    }
   ],
   "source": [
    "#for loop iteration\n",
    "num = int(input('Enter any no.'))\n",
    "for i in range(1,11):\n",
    "    print(num,\" * \",i,\" = \",(num*i))"
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
      "* \r\n",
      "* * \r\n",
      "* * * \r\n",
      "* * * * \r\n",
      "* * * * * \r\n"
     ]
    }
   ],
   "source": [
    "rows = 5\n",
    "for i in range(0, rows):\n",
    "    for j in range(0, i + 1):\n",
    "        print(\"*\", end=' ')\n",
    "\n",
    "    print(\"\\r\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "else block in loop\n",
      "out of loop\n"
     ]
    }
   ],
   "source": [
    "#else statement in for loop\n",
    "for x in range(5):\n",
    "    print(x+1)\n",
    "else:\n",
    "    print(\"else block in loop\")\n",
    "print(\"out of loop\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#break statement \n",
    "for x in range(1,11):\n",
    "    if x==3:\n",
    "        continue\n",
    "    if x==6:\n",
    "        break\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Num = {} 1\n",
      "Num = {} 2\n",
      "Num = {} 4\n",
      "Num = {} 5\n"
     ]
    }
   ],
   "source": [
    "#pass statement \n",
    "for num in range(1,6):\n",
    "    if num==3:\n",
    "        pass\n",
    "    else:\n",
    "        print(\"Num = {}\",format(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun():\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Num : 1\n",
      "Num : 2\n",
      "Num : 3\n",
      "Num : 4\n",
      "Num : 5\n"
     ]
    }
   ],
   "source": [
    "#while demo....\n",
    "num = 0\n",
    "while num<5:\n",
    "    num+=1\n",
    "    print(\"Num :\",num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any no. .... type -1 to exit-3\n",
      "Enter any no. .... type -1 to exit-7\n",
      "Enter any no. .... type -1 to exit-6\n",
      "Enter any no. .... type -1 to exit--1\n",
      "numbers input : 3 Average :  5.333333333333333\n"
     ]
    }
   ],
   "source": [
    "num =0\n",
    "count =0\n",
    "sum =0\n",
    "while num>=0:\n",
    "    num = int(input('Enter any no. .... type -1 to exit-'))\n",
    "    if num>=0:\n",
    "        count+=1\n",
    "        sum=sum+num\n",
    "avg=sum/count\n",
    "print(\"numbers input :\",count,\"Average : \",avg)"
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
