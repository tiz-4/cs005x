comp = 'rock'
user = 'paper' # this line is changed during the video

if comp == 'paper' and user == 'paper':
  print 'Tie'

elif comp == 'rock':

  if user == 'scissors':
    print 'I win!'
  else:
    print 'You win.'

else:

  print 'Tie.'
