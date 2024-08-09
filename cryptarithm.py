from itertools import permutations
import streamlit as st

def solve_cryptarithm(list_sum,result):
    digits = '0123456789'
    list_word=[char for word in list_sum for char in [*word]]
    list_word.extend([*result])
    list_word=list(set(list_word))
    list_word.sort()
    for perm in permutations(digits, len(list_word)):
        pair_word={k:v for k,v in zip(list_word,perm)}
        digit_sum=[]
        skip=False
        for word in list_sum:
            if pair_word[word[0]]=='0':
                skip=True
                break
            digit=int("".join([pair_word[w] for w in [*word]]))
            digit_sum.append(digit)
        if pair_word[result[0]]=='0' or skip:
            continue
        digit_result=int("".join([pair_word[w] for w in [*result]]))
        if sum(digit_sum)==digit_result:
            print(digit_sum)
            return pair_word

num2add=st.text_input("word to add (separate by comma)","")
target=st.text_input("target word","")
if st.button("run"):
    list_text=num2add.split(",")
    result = solve_cryptarithm(list_text,target)
    if result!=None:
        st.json(result)
    else:
        st.text("can not found match")
