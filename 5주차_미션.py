# -*- coding: utf-8 -*-
"""5주차 미션

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ycnUOyMFG-tSgFj7WpITNOmXTl6tD4IU

📌Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요. 파이썬 함수를 활용해 다음의 규칙을 만족하는 게임을 만들어보고, 컴퓨터와 대결을 해보세요. [난이도 : ⭐️⭐️⭐️/5]
"""

import random

current_number = 0
player_turns = True

print("베스킨 라빈스 31 게임\n --------------")

while current_number < 31:
    print(f"현재 숫자: {current_number}")

    if player_turns:
        my = int(input("1부터 3 사이의 숫자를 입력: "))
        while my < 1 or my > 3 or current_number + my > 31:
            my = int(input("잘못된 입력입니다. 다시 입력하세요: "))
        print(f"플레이어: {my}")
    else:
        my = min(4 - (current_number % 4), 3)
        print(f"컴퓨터: {my}")

    current_number += my
    player_turns = not player_turns

winner = "플레이어" if player_turns else "컴퓨터"
print(f"{winner} 승리!")

"""📌Q2. 한 중학교에서는 중간고사가 끝난 후, 학생들의 시험 답지와 정답지를 비교하여 점수를 계산하는 채점 프로그램을 도입하려고 합니다. 학생들의 시험 답지와 정답지가 다음과 같이 주어졌을 때, 파이썬 함수를 활용하여 다음의 요구사항을 충족하는 채점 프로그램을 만들어보세요. [난이도 : ⭐️⭐️⭐️⭐️/5]"""

def grader(s, a):
    def calculate_score(student_answer, correct_answer):
        return sum(int(sa) == ca for sa, ca in zip(student_answer, correct_answer))

    student_scores = [(name, calculate_score(answers, a)) for sa in s for name, answers in [sa.split(',')]]
    student_scores.sort(key=lambda x: x[1], reverse=True)

    for rank, (name, score) in enumerate(student_scores, start=1):
        score_text = f"{score*10}점"
        rank_text = "1등" if rank == 1 else f"{rank}등"
        print(f"학생: {name} 점수: {score_text} {rank_text}")

s = [
    "김갑,3242524215",
    "이을,3242524223",
    "박병,2242554131",
    "최정,4245242315",
    "정무,3242524315",
]
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]
grader(s, a)

"""📌Q3. 여러분은 오랜 친구와 함께 휴가를 보내기로 결정했습니다. 그리고 그 휴가의 첫 날, 두 사람은 재미있는 게임을 하기로 했습니다. 이 게임은 Up&Down 으로 숫자를 맞추는 것인데요, 컴퓨터가 1개의 숫자를 랜덤하게 생성하면, 우리가 그 값을 맞추는 도전을 해보려 합니다. 파이썬 함수를 활용해 다음의 규칙을 만족하는 Up&Down 게임을 만들어보세요. [난이도 : ⭐️⭐️⭐️⭐️/5]"""

import random

def get_user_guess(attempts):
    while True:
        try:
            guess = int(input(f"{attempts}차 시도\n숫자를 예측해보세요 : "))
            if 0 <= guess <= 100:
                return guess
            print("0부터 100 사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def compare_guesses(guess, number):
    if guess < number:
        return "UP"
    elif guess > number:
        return "DOWN"
    else:
        return "CORRECT"

number = random.randint(0, 100)
attempts_list = []

for attempts in range(1, 11):
    guess = get_user_guess(attempts)

    if guess in attempts_list:
        print("이미 예측에 사용한 숫자입니다. 다시 한번 고민해보세요.")
        continue

    attempts_list.append(guess)
    result = compare_guesses(guess, number)

    if result == "UP":
        print(result, "다시 한번 고민해보세요.")
    elif result == "DOWN":
        print(result, "다시 한번 고민해보세요.")
    else:
        print(f"{attempts}차 시도만에 예측에 성공했네요!! 게임을 종료합니다.")
        break

    if attempts == 10:
        print(f"10번의 시도 내에 정답을 맞추지 못했습니다. 정답은 {number}입니다.")

"""📌Q4. 얼마 전, 당신은 한 사람과 만나게 되었습니다. 서로의 마음을 알아가며 진실된 사랑이 시작되었고, 곧 100일이 다가오고 있습니다. 이 날을 기념하기 위해 당신은 특별한 이벤트를 준비하려고 하는데요, 하지만 100일 기념일이 정확히 언제인지 알지 못합니다. 그래서 파이썬 함수를 활용해 100일 뒤가 몇월 며칠인지 계산하는 프로그램을 작성하려고 합니다. 다음의 요구사항을 충족하는 D-Day 계산기 프로그램을 만들어보세요. [난이도 : ⭐️⭐️⭐️⭐️/5]"""

def get_day_number(day):
    days = ["일", "월", "화", "수", "목", "금", "토"]
    return days.index(day)

def get_next_day(current_day):
    days = ["일", "월", "화", "수", "목", "금", "토"]
    next_index = (get_day_number(current_day) + 1) % 7
    return days[next_index]

def calculate_date(year, month, day, num_days):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while num_days > 0:
        if day > days_in_month[month]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        day += 1
        num_days -= 1
    return year, month, day

def after_100(month, day, current_day):
    year = 1
    year, month, day = calculate_date(year, month, day, 100)
    next_day = current_day
    for _ in range(100):
        next_day = get_next_day(next_day)
    return year, month, day, next_day

input_month = int(input("월을 입력하세요: "))
input_day = int(input("일을 입력하세요: "))
input_day_of_week = input("요일을 입력하세요: ")

year, month, day, next_day = after_100(input_month, input_day, input_day_of_week)

print(f"우리의 기념일은 {input_month}월 {input_day}일 {input_day_of_week}입니다.")
print(f"이로부터 100일 뒤의 날짜는 {month}월 {day-1}일 {next_day}요일입니다.")