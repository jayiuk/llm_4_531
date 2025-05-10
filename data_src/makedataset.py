import random
from getdata import get_data_531_basic
import glob
import json
import os

def make_tuning_dataset(s, n):
    for i in range(s, n+1):
        rm = random.randrange(60, 140, step = 5)
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
        b = random.randrange(60, 150, step = 5)
        d = random.randrange(80, 200, step = 5)
        s = random.randrange(90, 200, step = 5)
        rms = [b, d, s]
        input_text1 = f"난 벤치는 {b}만큼 치고, 데드는 {d}만큼 쳐. 스쿼트는 {s}정도 쳐. 나에게 맞는 5/3/1 루틴을 짜줘"
        input_text2 = f"벤치프레스 RM은 {b}야. 데드리프트트 최대는 {d}고, 스쿼트는 {s}야. 이거에 맞는 5/3/1 루틴을 짜줘"
        input_text3 = f"벤치 rm = {b}, 데드 rm = {d}, 스쿼트 rm = {s}. 이거에 맞는 5/3/1 루틴 만들어."
        input_text4 = f"벤치 최대는 {b}, 데드 최대는 {d}, 스쿼트 최대는 {s} 이거에 맞는 5/3/1 루틴 만들어봐."
        input_text5 = f"내가 하는 운동 최대는 각각 {b}, {d}, {s}. 5/3/1 루틴 만들어봐."
        texts = [input_text1, input_text2, input_text3, input_text4, input_text5]
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