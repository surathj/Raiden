import random
import json


display_width = 800
display_height = 600

def create_top_attack():
	top_attack_startx = random.randrange(0, display_width)
	return top_attack_startx

def create_bottom_attack():
	bottom_attack_startx = random.randrange(0, display_width)
	return bottom_attack_startx

def create_left_attack():
	left_attack_starty = random.randrange(0, display_height)
	return left_attack_starty

def create_right_attack():
	right_attack_starty = random.randrange(0, display_height)
	return right_attack_starty


#def read_in():
 #   lines = sys.stdin.readlines()
  #  return json.loads(lines[0])

def main():
    #get data as an array from read_in()
    #lines = read_in()

    attack_list = (create_top_attack(), create_left_attack(), create_bottom_attack(), create_right_attack())

    ################################
    coord_list = []

    for i in range(10):
    	coord_list.append((create_top_attack(), create_left_attack(), create_bottom_attack(), create_right_attack()))

    ################################
    print(json.dumps(coord_list))


#start process
if __name__ == '__main__':
    main()