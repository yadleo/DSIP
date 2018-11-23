def calculate_ball_probability(red, green, purple, k):
  '''
  Calculate the probability that it takes k draws to match the
  ball drawn on draw zero

  Parameters
  ----------
  red: {int} Number of red balls
  green: {int} Number of green balls
  purple: {int} Number of purple balls
  k: {int} number of draw to calculate probability for

  Returns
  -------
  final_probability: {float} probability
  '''
  return prob_helper(red, green, purple, k) + prob_helper(green, purple, red, k) + prob_helper(purple, red, green, k)

def prob_helper(first_dr, sec_dr, third_dr, count):
  universal = first_dr + sec_dr + third_dr
  non_first = sec_dr + third_dr
  draw = 0
  prob = 1
  while draw < count:
    if draw == 0:
      prob *= first_dr / (universal - draw)
      first_dr -= 1
    else:
      prob *= non_first / (universal - draw)
      non_first -= 1
    draw += 1
  prob *= first_dr / (universal - draw)
  return prob


test = calculate_ball_probability(9, 8, 3, 5)
# result should have been: 0.05655314757481941
print(test)