import json
from collections import OrderedDict

def get_data_531_basic(prompt, rm):
    instruction = "사용자의 1RM 정보를 바탕으로 기본형 5/3/1 루틴을 생성하세요."
    tm = rm * 0.9
    percentages = {
        "week1" : [0.65, 0.75, 0.85],
        "week2" : [0.7, 0.8, 0.9],
        "week3" : [0.75, 0.85, 0.95],
        "week4-deload" : [0.4, 0.5, 0.6]
    }
    reps = {
        "week1" : ["5", "5", "5+"],
        "week2" : ["3", "3", "3+"],
        "week3" : ["5", "3", "1+"],
        "week4-deload" : ["5", "5", "5"]
    }
    
    routine = {}
    for week in percentages:
        routine[week] = []
        for pct, rep in zip(percentages[week], reps[week]):
            weight = round((tm * pct) / 2.5) * 2.5
            routine[week].append(f"{weight:.1f}kg X {rep}")
    
    data = OrderedDict()
    data["instruction"] = instruction
    data["input"] = prompt
    data["output"] = routine