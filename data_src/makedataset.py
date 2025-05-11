import random
from getdata import get_data_531_basic, getdata_str
import glob
import json
import os

def make_tuning_dataset(s, n):
    for i in range(s, n+1):
        rm = random.randrange(70, 200, step = 5)
        input_text1 = f"난 {rm}만큼 무게를 들어. 이거에 맞는 5/3/1 루틴 만들어줘."
        input_text2 = f"내 RM은 {rm}이야. 이거에 맞는 5/3/1 루틴 만들어줘."
        input_text3 = f"내 데드 최대 {rm}이야. 이거에 맞는 5/3/1 루틴 알려줘."
        input_text4 = f"내 스쿼트 최대 중량은 {rm}이야. 5/3/1 루틴을 어떻게 짜는게 좋을까?"
        input_text5 = f"내 벤치 최대는 {rm}이야. 적절한 5/3/1 루틴이 뭐야?"
        input_text6 = f"나 벤치프레스 최대 {rm}만큼 해. 적절한 5/3/1 루틴 짜줘."
        input_text7 = f"{rm}만큼 해. 적절한 5/3/1 루틴 만들어."
        input_text8 = f"내 RM은 {rm}이야. 적절한 루틴 만들어."
        input_texts = [input_text1, input_text2, input_text3, input_text4, input_text5, input_text6, input_text7, input_text8]
        input_text = random.choice(input_texts)
        out_text1_1 = "5/3/1 운동 루틴을 알려드리겠습니다."
        out_text1_2 = "말씀하신대로 5/3/1 루틴을 만들겠습니다."
        out_text1_3 = "네. 5/3/1 루틴을 짜드리겠습니다."
        out_text1_4 = "5/3/1 루틴을 만들겠겠습니다."
        out_text1_5 = "여기 말씀하신 5/3/1 루틴입니다."
        out_text2_1 = "이대로 운동하시면 됩니다. 요일은 편한 날에 하면 됩니다. 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_2 = "5/3/1 운동 루틴을 만들었습니다. 요일은 편한 날에 해주면 됩니다. 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_3 = "5/3/1 운동 루틴을 짰습니다. 편한 날에 하되, 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_4 = "루틴 나왔습니다. 요일은 자유롭게 결정하세요. 하지만 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_5 = "이 루틴대로 하면 된니다. 단, 중간에 쉬는 날은 꼭 넣도록하세요."
        out_texts1 = [out_text1_1, out_text1_2, out_text1_3, out_text1_4, out_text1_5]
        out_texts2 = [out_text2_1, out_text2_2, out_text2_3, out_text2_4, out_text2_5]
        out_text1 = random.choice(out_texts1)
        out_text2 = random.choice(out_texts2)
        path = f'tuning_data{i}.json'
        result = get_data_531_basic(input_text, rm, path, out_text1, out_text2)
    return result

def make_tuning_dataset_list(s, n):
    for i in range(s, n+1):
        b = random.randrange(70, 200, step = 5)
        d = random.randrange(70, 200, step = 5)
        s = random.randrange(70, 200, step = 5)
        o = random.randrange(70, 200, step = 5)
        rms = [b, d, s, o]
        input_text1 = f"난 벤치는 {b}만큼 치고, 데드는 {d}만큼 쳐. 스쿼트는 {s}정도 쳐. 오버헤드프레스는 {o}만큼 쳐. 나에게 맞는 5/3/1 루틴을 짜줘"
        input_text2 = f"벤치프레스 RM은 {b}야. 데드리프트 최대는 {d}고, 스쿼트는 {s}야. 오버헤드는 {o}야. 이거에 맞는 5/3/1 루틴을 짜줘"
        input_text3 = f"벤치 rm = {b}, 데드 rm = {d}, 스쿼트 rm = {s}, 오버헤드 rm = {o}. 이거에 맞는 5/3/1 루틴 만들어."
        input_text4 = f"벤치 최대는 {b}, 데드 최대는 {d}, 스쿼트 최대는 {s}, 오베헤드 최대는 {o} 이거에 맞는 5/3/1 루틴 만들어봐."
        input_text5 = f"내가 하는 운동 최대는 각각 {b}, {d}, {s}, {o}. 5/3/1 루틴 만들어봐."
        input_text6 = f"내가 하는 운동과 각각의 RM을 알려줄게. 벤치프레스는 {b}, 데드리프트는 {d}, 스쿼트는 {s}, 오버헤드프레스는 {o}. 이거에 맞는 5/3/1 루틴을 만들어줘."
        texts = [input_text1, input_text2, input_text3, input_text4, input_text5, input_text6]
        input_text = random.choice(texts)
        out_text1_1 = "5/3/1 운동 루틴을 알려드리겠습니다."
        out_text1_2 = "말씀하신대로 5/3/1 루틴을 만들겠습니다."
        out_text1_3 = "네. 5/3/1 루틴을 짜드리겠습니다."
        out_text1_4 = "5/3/1 루틴을 만들겠겠습니다."
        out_text1_5 = "여기 말씀하신 5/3/1 루틴입니다."
        out_text2_1 = "이대로 운동하시면 됩니다. 요일은 편한 날에 하면 됩니다. 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_2 = "5/3/1 운동 루틴을 만들었습니다. 요일은 편한 날에 해주면 됩니다. 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_3 = "5/3/1 운동 루틴을 짰습니다. 편한 날에 하되, 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_4 = "루틴 나왔습니다. 요일은 자유롭게 결정하세요. 하지만 중간에 쉬는 날은 꼭 넣어주세요."
        out_text2_5 = "이 루틴대로 하면 된니다. 단, 중간에 쉬는 날은 꼭 넣도록하세요."
        out_texts1 = [out_text1_1, out_text1_2, out_text1_3, out_text1_4, out_text1_5]
        out_texts2 = [out_text2_1, out_text2_2, out_text2_3, out_text2_4, out_text2_5]
        out_text1 = random.choice(out_texts1)
        out_text2 = random.choice(out_texts2)
        path = f'tuning_data_list{i}.json'
        result = get_data_531_basic(input_text, rms, path, out_text1, out_text2)
    return result

def make_531_explanation(s, n):
    instruction = "5/3/1 운동 루틴에 대해 설명하세요."
    for i in range(s, n+1):
        input_text1 = "5/3/1 루틴이 뭐야?"
        input_text2 = "5/3/1 운동 루틴에 대해 설명해봐"
        input_text3 = "5/3/1 루틴이란게 있다는데 그건 또 뭐야?"
        input_text4 = "5/3/1 루틴에 대해 알려줘"
        input_text5 = "5/3/1 운동 루틴 알려줘"
        input_text6 = "5/3/1 운동 루틴은 뭐하는 루틴이야?"
        input_texts = [input_text1, input_text2, input_text3, input_text4, input_text5, input_text6]
        input_text = random.choice(input_texts)
        output_text1 = "5/3/1 운동 루틴은 짐 웬들러가 만든 루틴으로, 본 운동 반복 횟수를 5회, 3회, 1회 하는 루틴입니다. 물론 이렇게만 하진 않습니다."
        output_text2 = "5/3/1 루틴은 짐 웬들러가 만들었습니다. 반복 횟수를 5, 3, 1회 하는 운동법입니다. 물론 이렇게만 하진 않습니다."
        output_text3 = "5/3/1 루틴이란 근육을 키우기 좋은 루틴으로, 본 운동을 5회, 3회, 1회를 한다고 하여 붙은 이름입니다. 반복 횟수는 고정은 아닙니다."
        output_text4 = "5/3/1 루틴은 짐 웬들러가 고안한 루틴입니다. 기본적인 골격은 5회, 3회, 1회 반복합니다. 다만 이는 고정적이지 않습니다."
        output_text5 = "5/3/1 루틴은 짐 웬들러가 만든 루틴입니다. 이는 5, 3, 1회 반복한다고 하여 붙은 이름입니다. 꼭 이렇지는 않습니다."
        output_texts = [output_text1, output_text2, output_text3, output_text4, output_text5]
        output_text = random.choice(output_texts)
        path = f'tuning_data_exp{i}.json'
        result = getdata_str(instruction, input_text, output_text, path)
    return result
        

def make_1file(d_path, file_name):
    new_data = []
    json_files = glob.glob(os.path.join(d_path, '*.json'))
    print(json_files)
    for file in json_files:
        with open(file, encoding = 'utf-8') as f:
            data = json.load(f)
            new_data.append(data)
    with open(file_name, "w", encoding = 'utf-8') as r:
        json.dump(new_data, r, ensure_ascii=False, indent = 2)
    return new_data