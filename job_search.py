# -*- coding: utf-8 -*-
"""
Set up: You search for jobs on LinkedIn for 30-40 hours a week as if your
survival depends on it. You need to feed your family, pay child support,
and avoid eviction or getting your gas shut off for the winter. So you decide
to practice coding in Python for months, attend lectures and tutorials,
and submit as many well-thought applications as possible...

Task: Write a function to 
decide if it was all worth it, or if you should go back to the kitchen.
The function is an infinite loop of BS until you either find the job or you
dump the core and go back to the kitchen.

Function- waste_of_time(in1, in2, in3, in4)
in1: str(list), all your previous interactions on LinkedIn not leading to a job
in2: int, how many hours a day you spend searching for a job on LinkedIn
in3: int, number of phone calls you get from head hunters
in4: int, times you were ghosted by recrutiers and hiring managers
"""
class solution:
    def waste_of_time (self, lst_of_bull: list, per_day: int, 
                       phone_calls: int, times_ghosted: int) -> bool:
        #You are unemployed
        unemployed = True
        #how many applications you submit per day
        applications = 25
        #the endless list of bull represented as a single integer
        frustration = int(''.join([str(x) for x in lst_of_bull]))
        while unemployed == True:
            frustration += applications % per_day
            frustration // phone_calls - times_ghosted
            if frustration == 0:
                unemployed == False
                #congrats
                return print('you got a job offer! Though it was not likely!')
            elif frustration == 1:
                #you decided to go premium membership
                return print('you are a fool- give it up!')
            else:
                continue