import json
from collections import OrderedDict

def get_data_531_basic(prompt, rm, path, outment1, outment2):
    if type(rm) == int:
        instruction = "사용자의 1RM 정보를 바탕으로 기본적인 5/3/1 루틴을 생성하세요."
        tm = rm * 0.9
        percentages = {
            "1주차" : [0.65, 0.75, 0.85],
            "2주차" : [0.7, 0.8, 0.9],
            "3주차" : [0.75, 0.85, 0.95],
            "4주차-deload" : [0.4, 0.5, 0.6]
        }
        reps = {
            "1주차" : ["5", "5", "5+"],
            "2주차" : ["3", "3", "3+"],
            "3주차" : ["5", "3", "1+"],
            "4주차-deload" : ["5", "5", "5"]
        }
        
        routine = [outment1]
        days = ['1일차', '2일차', '3일차']
        for week in percentages:
            for pct, rep, d in zip(percentages[week], reps[week], days):
                weight = round((tm * pct) / 2.5) * 2.5
                routine.append(f"{week}-{d}:{weight:.1f}kg X {rep}")
        routine.append(outment2)
            
        
        data = OrderedDict()
        data["instruction"] = instruction
        data["input"] = prompt
        data["output"] = routine
        with open(path, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii = False)
    
    elif type(rm) == list:
        instruction = "사용자의 1RM 정보를 바탕으로 기본적인 5/3/1 루틴을 생성하세요."
        tms = []
        for r in rm:
            tm = r * 0.9
            tms.append(tm)
        percentages = {
            "1주차" : [0.65, 0.75, 0.85],
            "2주차" : [0.7, 0.8, 0.9],
            "3주차" : [0.75, 0.85, 0.95],
            "4주차-deload" : [0.4, 0.5, 0.6]
        }
        reps = {
            "1주차" : ["5", "5", "5+"],
            "2주차" : ["3", "3", "3+"],
            "3주차" : ["5", "3", "1+"],
            "4주차-deload" : ["5", "5", "5"]
        }
        routine = [outment1]
        days = ['1일차', '2일차', '3일차']
        for week in percentages:
            for r in tms:
                for pct, rep, d in zip(percentages[week], reps[week], days):
                    weight = round((r * pct) / 2.5) * 2.5
                    routine.append(f"{week}-{d}:{weight:.1f}kg X {rep}")
        routine.append(outment2)
        
        data = OrderedDict()
        data["instruction"] = instruction
        data["input"] = prompt
        data["output"] = routine

        with open(path, 'w', encoding = 'UTF-8') as f:
            json.dump(data, f, ensure_ascii = False)


    return data
