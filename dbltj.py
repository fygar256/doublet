#!/usr/bin/python
from collections import deque, defaultdict
import sys
import unicodedata
import re

dictionary = 'jm.txt'

kana_list = [
    'きゃ','きゅ','きょ','しゃ','しゅ','しょ','ちゃ','ちゅ','ちょ','にゃ','にゅ','にょ',
    'ひゃ','ひゅ','ひょ','みゃ','みゅ','みょ','りゃ','りゅ','りょ','ぎゃ','ぎゅ','ぎょ',
    'じゃ','じゅ','じょ','ぢゃ','ぢゅ','ぢょ','びゃ','びゅ','びょ','ぴゃ','ぴゅ','ぴょ',
    'あ','い','う','え','お','か','き','く','け','こ','が','ぎ','ぐ','げ','ご','さ','し','す','せ','そ',
    'ざ','じ','ず','ぜ','ぞ','た','ち','つ','っ','て','と','だ','ぢ','づ','で','ど','な','に','ぬ','ね','の',
    'は','ひ','ふ','へ','ほ','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ','ま','み','む','め','も',
    'や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん','ー',
]

kana_pattern = re.compile('|'.join(sorted(kana_list, key=len, reverse=True)))

def normalize(text):
    return unicodedata.normalize('NFKC', text.strip().lower())

def split_kana(word):
    return kana_pattern.findall(word)

def load_words_all():
    length_dict = defaultdict(set)
    with open(dictionary, encoding='utf-8') as f:
        for line in f:
            word = normalize(line)
            kana = split_kana(word)
            if all(k in kana_list for k in kana):
                length = len(kana)
                length_dict[length].add(word)
    return length_dict

def build_neighbor_index(words, max_diff=2):
    length = len(next(iter(words)))
    index = defaultdict(set)

    for word in words:
        kana = split_kana(word)
        for i in range(length):
            key1 = tuple(kana[:i]) + ("*",) + tuple(kana[i+1:])
            index[key1].add(word)

        if max_diff == 2:
            for i in range(length):
                for j in range(i+1, length):
                    key2 = tuple(kana[:i]) + ("*",) + tuple(kana[i+1:j]) + ("*",) + tuple(kana[j+1:])
                    index[key2].add(word)

    return index

def get_neighbors_fast(word, neighbor_index, max_diff=2, word_set=None):
    kana = split_kana(word)
    length = len(kana)
    candidates = set()

    for i in range(length):
        key1 = tuple(kana[:i]) + ("*",) + tuple(kana[i+1:])
        candidates.update(neighbor_index.get(key1, set()))

    if max_diff == 2:
        for i in range(length):
            for j in range(i+1, length):
                key2 = tuple(kana[:i]) + ("*",) + tuple(kana[i+1:j]) + ("*",) + tuple(kana[j+1:])
                candidates.update(neighbor_index.get(key2, set()))

    results = []
    for candidate in candidates:
        if candidate == word:
            continue
        if candidate not in word_set:
            continue
        candidate_kana = split_kana(candidate)
        if len(candidate_kana) != length:
            continue
        diff = sum(k1 != k2 for k1, k2 in zip(candidate_kana, kana))
        if 1 <= diff <= max_diff:
            results.append(candidate)

    return results

def solve_doublet(start, goal, words_by_length, max_diff=2):
    start_kana = split_kana(start)
    goal_kana = split_kana(goal)

    if len(start_kana) != len(goal_kana):
        return None

    length = len(start_kana)
    word_set = words_by_length[length]

    # ❗️start / goal が辞書にない場合は探索しない
    if start not in word_set or goal not in word_set:
        return None

    neighbor_index = build_neighbor_index(word_set, max_diff)

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        current_word, path = queue.popleft()
        if current_word == goal:
            return path

        for neighbor in get_neighbors_fast(current_word, neighbor_index, max_diff, word_set):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("使い方: python dbltj.py スタート単語 ゴール単語")
        sys.exit(1)

    start_word = normalize(sys.argv[1])
    goal_word = normalize(sys.argv[2])

    words_by_length = load_words_all()

    if len(split_kana(start_word)) != len(split_kana(goal_word)):
        print("長さが合っていません。")
        sys.exit(1)

    result = solve_doublet(start_word, goal_word, words_by_length)

    if result:
        print("解:", len(result) - 2, ";", ",".join(result))
    else:
        print("解が見つかりませんでした。")

