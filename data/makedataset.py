import random
from getdata import get_data_531_basic

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
        texts = [input_text1, input_text2, input_text3, input_text4, input_text5, input_text6, input_text7, input_text8]
        input_text = random.choice(texts)
        path = f'tuning_data{i}.json'
        result = get_data_531_basic(input_text, rm, path)
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
        path = f'tuning_data_list{i}.json'
        result = get_data_531_basic(input_text, rms, path)
    return result
        