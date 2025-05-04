#!/usr/bin/python
from collections import deque
import sys
import unicodedata
import re

dictionary = '/home/gar/dic/jm.txt'

# 仮名の一覧（拗音含む）
kana_list = [
    'あ','い','う','え','お',
    'か','き','く','け','こ',
    'が','ぎ','ぐ','げ','ご',
    'さ','し','す','せ','そ',
    'ざ','じ','ず','ぜ','ぞ',
    'た','ち','つ','て','と',
    'だ','ぢ','づ','で','ど',
    'な','に','ぬ','ね','の',
    'は','ひ','ふ','へ','ほ',
    'ば','び','ぶ','べ','ぼ',
    'ぱ','ぴ','ぷ','ぺ','ぽ',
    'ま','み','む','め','も',
    'や','ゆ','よ',
    'ら','り','る','れ','ろ',
    'わ','を','ん','ー',
    'きゃ','きゅ','きょ',
    'しゃ','しゅ','しょ',
    'ちゃ','ちゅ','ちょ',
    'にゃ','にゅ','にょ',
    'ひゃ','ひゅ','ひょ',
    'みゃ','みゅ','みょ',
    'りゃ','りゅ','りょ',
    'ぎゃ','ぎゅ','ぎょ',
    'じゃ','じゅ','じょ',
    'ぢゃ','ぢゅ','ぢょ',
    'びゃ','びゅ','びょ',
    'ぴゃ','ぴゅ','ぴょ',
]

# 長いものから順に並べて正規表現で抽出
kana_pattern = re.compile('|'.join(sorted(kana_list, key=len, reverse=True)))

def normalize(text):
    return unicodedata.normalize('NFKC', text.strip().lower())

def split_kana(word):
    return kana_pattern.findall(word)

def load_words(word_length):
    with open(dictionary, encoding='utf-8') as f:
        words = set()
        for line in f:
            word = normalize(line)
            kana = split_kana(word)
            if len(kana) == word_length and all(k in kana_list for k in kana):
                words.add("".join(kana))
    return words

def get_neighbors(word, word_set):
    neighbors = []
    kana = split_kana(word)

    for i in range(len(kana)):
        for k in kana_list:
            if k != kana[i]:
                new_kana = kana[:i] + [k] + kana[i+1:]
                new_word = "".join(new_kana)
                if new_word in word_set:
                    neighbors.append(new_word)
    return neighbors

def solve_doublet(start, goal):
    if len(split_kana(start)) != len(split_kana(goal)):
        return None

    word_set = load_words(len(split_kana(start)))
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_word, path = queue.popleft()
        if current_word == goal:
            return path

        for neighbor in get_neighbors(current_word, word_set):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == '__main__':
    start_word = normalize(sys.argv[1])
    goal_word = normalize(sys.argv[2])

    if len(split_kana(start_word))!=len(split_kana(goal_word)):
        print("長さが合っていません。")
        exit(1)

    result = solve_doublet(start_word, goal_word)

    if result:
        print("解:", len(result)-2, ";", ",".join(result))
    else:
        print("解が見つかりませんでした。")

