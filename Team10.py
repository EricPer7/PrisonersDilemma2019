Team_name = 'Team10'
Strategy_name = 'When they betray, we automatically betray'
Strategy_description = 'Do what the others do to us'

def move(my_history, their_history, my_score, their_score):
  if len(their_history) >= 21 and their_history[-21] == 'b':
    return 'b'
  if 'bbb' in their_history:
    return 'b'
  else:
    return 'c'


move("c", 'b',0,0)
