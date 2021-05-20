{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Price :400\n",
      "Enter quantity :12\n",
      "Congrat's you got 10% discount\n",
      "Payable amount is :  4320.0\n"
     ]
    }
   ],
   "source": [
    "# Python if stmt....\n",
    "\n",
    "price=int(input(\"Enter Price :\"))\n",
    "qty=int(input(\"Enter quantity :\"))\n",
    "\n",
    "amt= price*qty;\n",
    "if amt > 2000:\n",
    "    print(\"Congrat's you got 10% discount\");\n",
    "    discount=amt*10/100\n",
    "    amt=amt-discount\n",
    "else:\n",
    "    print(\"Sorry no any discount available for you...!\")\n",
    "print(\"Payable amount is : \",amt)"
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
      "Enter your marks:34\n",
      "Failed\n"
     ]
    }
   ],
   "source": [
    "marks = int(input(\"Enter your marks:\"))\n",
    "grade=\"\"\n",
    "if (marks>=50 and marks <60):\n",
    "    grade=\"Pased\"\n",
    "elif (marks>=60 and marks<70):\n",
    "    grade=\"Good\"\n",
    "elif marks>=70 and marks<80:\n",
    "    grade=\"Very Good\"\n",
    "elif marks>=80 and marks<=100:\n",
    "    grade=\"Excellent\"\n",
    "elif marks>=100 or marks<0:\n",
    "    grade=\"Invalid marks entry\"\n",
    "else:\n",
    "    grade=\"Failed\"\n",
    "print(grade)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
