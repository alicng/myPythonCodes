def is_goal_scored(goal):

    return any('0' in i[0][3:8] for i in goal[:3])

a=is_goal_scored([
  ["  #0    #  "],
  ["  #     #  "],
  ["  #     #  "],
  ["  #######  "],
  ["     #     "],
  ["     #     "],
  ["     #     "]
])
print(a)