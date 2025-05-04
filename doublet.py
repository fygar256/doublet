#!/usr/bin/python
from collections import deque
import sys

dictionary='/home/gar/dic/dic.txt'

def load_words(word_length):
    # 単語リスト（辞書ファイルから読み込む）
    with open(dictionary) as f:
        words = set(word.strip().lower() for word in f if len(word.strip()) == word_length and word.strip().isalpha())
    return words

def get_neighbors(word, word_set):
    neighbors = []
    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            new_word = word[:i] + c + word[i+1:]
            if new_word in word_set and new_word != word:
                neighbors.append(new_word)
    return neighbors

def solve_doublet(start, goal):
    if len(start) != len(goal):
        return None

    word_set = load_words(len(start))
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

    return None  # 解が見つからなかった場合

if __name__=='__main__':
    start_word = sys.argv[1]
    goal_word = sys.argv[2]

    if len(start_word)!=len(goal_word):
        print("長さが合っていません。")
        exit(1)

    result = solve_doublet(start_word, goal_word)

    if result:
        print("解:", len(result)-2, ";", ",".join(result))
    else:
        print("解が見つかりませんでした。")

