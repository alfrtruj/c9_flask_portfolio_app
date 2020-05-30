from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

	
@app.route('/tic_tac_toc', methods=['GET','POST'])
def tic_tac_toc_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('tic_tac_toc.html')
	  elif request.method == 'POST':
  	      #print(request.form['text'].split())
  	      #total = 0
  	      #try:
  	      	#for str_num in request.form['text'].split():
  	      		#total += int(str_num)
  	      	#return render_template('tic_tac_toc.html', result=str(total))         
  	      #except ValueError:
  	      	#return "Easy now! Let's keep it simple! 2 numbers with a space between them please"
	      def display_board():
		  # Display Board
		  print(board[0] + "|" + board[1] + "|" + board[2])
		  print(board[3] + "|" + board[4] + "|" + board[5])
		  print(board[6] + "|" + board[7] + "|" + board[8])


		# Check wins and ties
	      def check_win(z):
		  y = board.count("_")
		  # check ties
		  if y == 0:
		      print("Nobody wins!!!")
		    # check wins
		  elif board[0] == board[1] == board[2] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[3] == board[4] == board[5] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[6] == board[7] == board[8] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[0] == board[3] == board[6] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[1] == board[4] == board[7] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[2] == board[5] == board[8] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[0] == board[4] == board[8] == z:
		      print(f"Congratulations {z}, you won!!! ")
		  elif board[2] == board[4] == board[6] == z:
		      print(f"Congratulations {z}, you won!!! ")
		    # flip player
		  else:
		      if z == "X":
			  z = "O"
			  handle_turn(z)
		  else:
			  z = "X"
			  handle_turn(z)


	      def handle_turn(i):
		  position = input(f"Player {i}, choose a position between 1-9: ")
		  while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		      print("Wrong input!")
	              position = input(f"Player {i}, choose a position between 1-9: ")
		  while board[int(position) -1] != "_":
		      position = input(f"Player {i}, This position {position} is taken. Choose another: ")
		  board.insert(int(position) - 1, i)
		  board.pop(int(position))
		  print()
		  display_board()
		  print()
		  check_win(i)


		# play game
	      def play_game():
		  display_board()
		  figure = input("What do you want, X or O: ")
		  if figure != "X" and figure != "O":
		      print("Wrong input!")
		      print()
		      play_game()
		  else:
			# handle turn
		      handle_turn(figure)


		# Create board
	      board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
	      play_game()

	
@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
