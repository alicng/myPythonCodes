def like_or_dislike(lst):
    cur_state = 'Nothing'
    for chosen in lst:
        if cur_state == chosen:
            cur_state = 'Nothing'
        else:
            cur_state = chosen
    return cur_state

a=like_or_dislike(['Like', 'Like', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike', 'Dislike', 'Like', 'Like', 'Like', 'Dislike', 'Dislike'])
print(a)