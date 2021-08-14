# Exercise: Oscar Nominee

## Table of Contents

- [DataSets](https://github.com/mukaruernest/Python-StratascratchExercises/new/master/oscar_nominees#dataset)
- [Questions](https://github.com/mukaruernest/Python-StratascratchExercises/new/master/oscar_nominees#question)
- [Solutions](https://github.com/mukaruernest/Python-StratascratchExercises/new/master/oscar_nominees#solution)


More details about this exercise can be found on [Stratascratch website](https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?python=1)

## DataSet

`oscar_nominees`

**Table 1: oscar_nominees**
| year | category                     | nominee         | movie                     | winner | id |
|------|------------------------------|-----------------|---------------------------|--------|----|
| 2006 | actress in a supporting role | Abigail Breslin | Little Miss Sunshine      | FALSE  | 1  |
| 1984 | actor in a supporting role   | Adolph Caesar   | A Soldier's Story         | FALSE  | 2  |
| 2006 | actress in a supporting role | Adriana Barraza | Babel                     | FALSE  | 3  |
| 2002 | actor in a leading role      | Adrien Brody    | The Pianist               | TRUE   | 4  |
| 1942 | actress in a supporting role | Agnes Moorehead | The Magnificent Ambersons | FALSE  | 5  |

## Question 

Count the number of movies that Abigail Breslin was nominated for an oscar.

## Solution

``` python
import pandas as pd

df = oscar_nominees[oscar_nominees.nominee =='Abigail Breslin']
result = len(df)
```

**Result**

| 1 |
|---|


