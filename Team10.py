Team_name = 'Team 10'
Team_Strategy = 'When they betray we automatically betray'
Strategy_description = 'Do what the others do to us'
def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return'c'
  elif (len(their_history)-1) == 'b':
    return'b'
  else:
    return 'c'
  
  
move("b","c",0,0)
