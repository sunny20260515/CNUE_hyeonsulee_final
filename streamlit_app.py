import random
import re

import streamlit as st

st.set_page_config(page_title="초등 5학년 수학 학습", page_icon="🧠", layout="centered")

st.title("🧩 초등학교 5학년 수학 학습 페이지")
st.write("다섯 가지 활동으로 수학을 재미있게 연습해보세요.")

st.markdown("---")

# 1. 숫자 분류하기
st.header("1. 숫자 분류하기")
st.write("아래 숫자들을 5보다 작은 숫자와 5보다 크거나 같은 숫자로 나누어 보세요.")
st.write("숫자: 3.5 / 5.7 / 1.7 / 4 / 8.9 / 0.5 / 7.2 / 5")

st.write("##### 5 미만인 숫자")
below_five = st.text_input("쉼표로 구분하여 숫자를 적으세요", key="below_five")
st.write("##### 5 이상인 숫자")
above_or_equal_five = st.text_input("쉼표로 구분하여 숫자를 적으세요", key="above_or_equal_five")

st.write("##### 적용 개념")
concept = st.text_area("어떤 기준으로 분류했는지 적어보세요.", key="sort_concept")
st.write("##### 정답을 고른 이유")
reason = st.text_area("왜 이렇게 분류했는지 설명해보세요.", key="sort_reason")

correct_below = {"3.5", "1.7", "4", "0.5"}
correct_above = {"5.7", "8.9", "7.2", "5"}

if st.button("정답 확인", key="classify_check"):
    def normalize_input(text):
        items = [item.strip() for item in re.split(r"[,\s]+", text) if item.strip()]
        return {item for item in items}

    user_below = normalize_input(below_five)
    user_above = normalize_input(above_or_equal_five)

    if user_below == correct_below and user_above == correct_above:
        st.success("정답입니다! 5 미만과 5 이상으로 잘 분류했어요.")
    else:
        st.error("틀렸어요. 다시 한 번 숫자들을 잘 살펴보세요.")
        st.write("- 5 미만: 3.5 / 1.7 / 4 / 0.5")
        st.write("- 5 이상: 5.7 / 8.9 / 7.2 / 5")

st.markdown("---")

# 2. O/X 퀴즈 문제 풀이
st.header("2. 실생활 O/X 문제")
st.write("아래 세 가지 실생활 이야기를 읽고, O 또는 X를 골라 보세요.")

st.write("1번 문제. 이번 줄넘기 대회에서 반 대표는 줄넘기를 한 번에 200회 이상 한 친구를 뽑습니다. 이때 태형이가 한 번에 줄넘기를 딱 200회를 했습니다. 이때 태형이는 줄넘기 반 대표가 된다.")
answer1 = st.radio("1번 정답", options=["O", "X"], key="ox_q1")

st.write("2번 문제. 쇼핑몰에서 30,000원 초과 구매 시 무료 배송일 때, 딱 30,000원어치를 사면 배송비를 내야 합니다. 이때 결제한 금액이 딱 30,000원이면 배송비를 내야 합니다.")
answer2 = st.radio("2번 정답", options=["O", "X"], key="ox_q2")

st.write("3번 문제. 생일이 지나지 않은 12살 시은이와 원영이는 이번에 개봉한 영화를 보러 갔습니다. 그런데 확인해보니 보려고 한 영화가 '만 12세 이상 관람가'였습니다. 이때 이 둘은 영화를 볼 수 있습니다.")
answer3 = st.radio("3번 정답", options=["O", "X"], key="ox_q3")

if st.button("정답 확인", key="ox_check"):
    correct_answers = ["O", "O", "X"]
    user_answers = [answer1, answer2, answer3]
    results = [user_answers[i] == correct_answers[i] for i in range(3)]

    for i, correct in enumerate(results, start=1):
        if correct:
            st.success(f"{i}번 정답입니다.")
        else:
            st.error(f"{i}번이 틀렸습니다.")

    if all(results):
        st.success("모든 문제를 맞혔어요! 잘했어요.")
    else:
        st.info("틀린 문제를 다시 확인해보세요.")

st.markdown("---")

# 3. 빈칸 채우기
st.header("3. 빈칸 채우기")
st.write("아래 두 문제에 맞는 숫자를 각각 빈칸에 채워보세요.")
st.write("1. 361을 올림하여 십의 자리까지 나타내면 ___ 입니다.")
st.write("2. 401을 올림하여 백의 자리까지 나타내면 ___ 입니다.")

blank_answer1 = st.text_input("1번 정답", key="blank_input_1")
blank_answer2 = st.text_input("2번 정답", key="blank_input_2")

if st.button("정답 확인", key="blank_check"):
    correct1 = 370
    correct2 = 500
    is_correct1 = blank_answer1.isdigit() and int(blank_answer1) == correct1
    is_correct2 = blank_answer2.isdigit() and int(blank_answer2) == correct2

    if is_correct1:
        st.success("1번 정답입니다! 361을 올림하여 십의 자리까지 나타내면 370입니다.")
    else:
        st.error("1번이 틀렸습니다. 다시 한 번 확인해보세요.")

    if is_correct2:
        st.success("2번 정답입니다! 401을 올림하여 백의 자리까지 나타내면 500입니다.")
    else:
        st.error("2번이 틀렸습니다. 다시 한 번 확인해보세요.")

    if is_correct1 and is_correct2:
        st.balloons()
        st.success("두 문제 모두 정답입니다! 잘했어요.")

st.markdown("---")

# 4. 수직선 표시하기
st.header("4. 수직선 표시하기")
st.write("수직선을 보고 숫자의 위치를 확인해보세요.")
start = st.slider("수직선 시작값", min_value=-10, max_value=0, value=-5)
end = st.slider("수직선 끝값", min_value=0, max_value=10, value=5)
if start >= end:
    st.error("시작값은 끝값보다 작아야 합니다.")
else:
    ticks = list(range(start, end + 1))
    line = " "
    for value in ticks:
        if value == 0:
            line += "0"
        else:
            line += "|"
        line += "   "

    labels = ""
    for value in ticks:
        label = str(value)
        labels += label + " " * (4 - len(label))

    st.code(line + "\n" + labels, language="text")

st.markdown("---")

# 5. 실생활 상황 활용 어림 문제
st.header("5. 실생활 어림 빈칸 문제")
scenarios = [
    ("마트에서 사과 47개를 샀어요. 대략 ___개입니다.", 50),
    ("버스에 128명이 타면, 약 ___명입니다.", 130),
    ("숙제 문제는 64문제였어요. 약 ___문제입니다.", 60),
    ("공원에 꽃이 236송이 있어요. 약 ___송이입니다.", 240),
    ("책이 195권 있어요. 약 ___권입니다.", 200),
]

scenario_text, scenario_answer = random.choice(scenarios)
st.write(f"문제: {scenario_text}")
estimate_answer = st.text_input("어림하여 채울 숫자를 쓰세요", key="estimate_input")
if st.button("확인", key="estimate_check"):
    if estimate_answer.isdigit() and int(estimate_answer) == scenario_answer:
        st.success("정답입니다! 어림하기 잘했어요.")
    else:
        st.error(f"틀렸어요. 정답은 {scenario_answer}입니다.")
