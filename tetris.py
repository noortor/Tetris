import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

game_start = False
game_over = False 
WIDTH = 600
HEIGHT = 700
#length of squares
BlockLen = 30
#controls points to be drawn, can be generalized for all tetromino types
current_mid = []
current_pts = []
#contains points that are changed to affect the drawn points
update_pts = []
#temporary variable used in rotation
old_pts = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#keeps track of current type of tetromino
current = 0
#color of tetrominoes
current_color = []
#used for indexing when updating and drawing points
count = -1
#keeps track if current block is on right or left side
right_grid = False
left_grid = False
#index of point used for checking position in grid
check_pt = []
#used for predicting the next point if tetromino is rotated
test_pts = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
current_test_pts = [[[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]]]
#determines if a tetromino can rotate
can_rotate = True
#tracks if a new tetromino needs to be created
set_new = False
#keeps track of lines cleared
clear = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
row_filled = 0
#determines if there's a block underneath the current
block_under = False
score = 0
lines_cleared = 0
#determines if block being set is first
first_block = True

next_block = 0 
#points for next block to be displayed
next_pts = []
next_color = 0

#determines level
total_lines_cleared = 0
level = 1
#I Block initial position
I_mid = [300,110]
I_pts = []
I_pts.append([I_mid[0] - BlockLen, I_mid[1] - 2 * BlockLen])
I_pts.append([I_mid[0] - BlockLen, I_mid[1] - BlockLen])
I_pts.append([I_mid[0] - BlockLen, I_mid[1]])
I_pts.append([I_mid[0] - BlockLen, I_mid[1] + BlockLen])
I_pts.append([I_mid[0] - BlockLen, I_mid[1] + 2 * BlockLen])
I_pts.append([I_mid[0], I_mid[1] - 2 * BlockLen])
I_pts.append([I_mid[0], I_mid[1] - BlockLen])
I_pts.append([I_mid[0], I_mid[1]])
I_pts.append([I_mid[0], I_mid[1] + BlockLen])
I_pts.append([I_mid[0], I_mid[1] + 2* BlockLen])

#J Block initial position
J_mid = [285, 95]
J_pts = []
J_pts.append([J_mid[0] - 1.5 * BlockLen, J_mid[1] - 1.5 * BlockLen])
J_pts.append([J_mid[0] - 1.5 * BlockLen, J_mid[1] - 0.5 * BlockLen])
J_pts.append([J_mid[0] - 1.5 * BlockLen, J_mid[1] + 0.5 * BlockLen])
J_pts.append([J_mid[0] - 0.5 * BlockLen, J_mid[1] - 1.5 * BlockLen])
J_pts.append([J_mid[0] - 0.5 * BlockLen, J_mid[1] - 0.5 * BlockLen])
J_pts.append([J_mid[0] - 0.5 * BlockLen, J_mid[1] + 0.5 * BlockLen])
J_pts.append([J_mid[0] + 0.5 * BlockLen, J_mid[1] - 0.5 * BlockLen])
J_pts.append([J_mid[0] + 0.5 * BlockLen, J_mid[1] + 0.5 * BlockLen])
J_pts.append([J_mid[0] + 1.5 * BlockLen, J_mid[1] - 0.5 * BlockLen])
J_pts.append([J_mid[0] + 1.5 * BlockLen, J_mid[1] + 0.5 * BlockLen])

#L Block initial position
L_mid = [285, 95]
L_pts = []
L_pts.append([L_mid[0] - 1.5 * BlockLen, L_mid[1] - 0.5 * BlockLen])
L_pts.append([L_mid[0] - 1.5 * BlockLen, L_mid[1] + 0.5 * BlockLen])
L_pts.append([L_mid[0] - 0.5 * BlockLen, L_mid[1] - 0.5 * BlockLen])
L_pts.append([L_mid[0] - 0.5 * BlockLen, L_mid[1] + 0.5 * BlockLen])
L_pts.append([L_mid[0] + 0.5 * BlockLen, L_mid[1] - 1.5 * BlockLen])
L_pts.append([L_mid[0] + 0.5 * BlockLen, L_mid[1] - 0.5 * BlockLen])
L_pts.append([L_mid[0] + 0.5 * BlockLen, L_mid[1] + 0.5 * BlockLen])
L_pts.append([L_mid[0] + 1.5 * BlockLen, L_mid[1] - 1.5 * BlockLen])
L_pts.append([L_mid[0] + 1.5 * BlockLen, L_mid[1] - 0.5 * BlockLen])
L_pts.append([L_mid[0] + 1.5 * BlockLen, L_mid[1] + 0.5 * BlockLen])

#O Block initial position
O_mid = [300,80]
O_pts = []
O_pts.append([O_mid[0] - BlockLen, O_mid[1] - BlockLen])
O_pts.append([O_mid[0] - BlockLen, O_mid[1]])
O_pts.append([O_mid[0] - BlockLen, O_mid[1] + BlockLen])
O_pts.append([O_mid[0], O_mid[1] - BlockLen])
O_pts.append([O_mid[0], O_mid[1]])
O_pts.append([O_mid[0], O_mid[1] + BlockLen])
O_pts.append([O_mid[0] + BlockLen, O_mid[1] - BlockLen])
O_pts.append([O_mid[0] + BlockLen, O_mid[1]])
O_pts.append([O_mid[0] + BlockLen, O_mid[1] + BlockLen])

#S Block initial position
S_mid = [285, 65]
S_pts = []
S_pts.append([S_mid[0] - 1.5 * BlockLen, S_mid[1] + 0.5 * BlockLen])
S_pts.append([S_mid[0] - 1.5 * BlockLen, S_mid[1] + 1.5 * BlockLen])
S_pts.append([S_mid[0] - 0.5 * BlockLen, S_mid[1] - 0.5 * BlockLen])
S_pts.append([S_mid[0] - 0.5 * BlockLen, S_mid[1] + 0.5 * BlockLen])
S_pts.append([S_mid[0] - 0.5 * BlockLen, S_mid[1] + 1.5 * BlockLen])
S_pts.append([S_mid[0] + 0.5 * BlockLen, S_mid[1] - 0.5 * BlockLen])
S_pts.append([S_mid[0] + 0.5 * BlockLen, S_mid[1] + 0.5 * BlockLen])
S_pts.append([S_mid[0] + 0.5 * BlockLen, S_mid[1] + 1.5 * BlockLen])
S_pts.append([S_mid[0] + 1.5 * BlockLen, S_mid[1] - 0.5 * BlockLen])
S_pts.append([S_mid[0] + 1.5 * BlockLen, S_mid[1] + 0.5 * BlockLen])

#T Block initial position
T_mid = [285, 95]
T_pts = []
T_pts.append([T_mid[0] - 1.5 * BlockLen, T_mid[1] - 0.5 * BlockLen])
T_pts.append([T_mid[0] - 1.5 * BlockLen, T_mid[1] + 0.5 * BlockLen])
T_pts.append([T_mid[0] - 0.5 * BlockLen, T_mid[1] - 1.5 * BlockLen])
T_pts.append([T_mid[0] - 0.5 * BlockLen, T_mid[1] - 0.5 * BlockLen])
T_pts.append([T_mid[0] - 0.5 * BlockLen, T_mid[1] + 0.5 * BlockLen])
T_pts.append([T_mid[0] + 0.5 * BlockLen, T_mid[1] - 1.5 * BlockLen])
T_pts.append([T_mid[0] + 0.5 * BlockLen, T_mid[1] - 0.5 * BlockLen])
T_pts.append([T_mid[0] + 0.5 * BlockLen, T_mid[1] + 0.5 * BlockLen])
T_pts.append([T_mid[0] + 1.5 * BlockLen, T_mid[1] - 0.5 * BlockLen])
T_pts.append([T_mid[0] + 1.5 * BlockLen, T_mid[1] + 0.5 * BlockLen])

#Z Block initial position
Z_mid = [285, 65]
Z_pts = []
Z_pts.append([Z_mid[0] - 1.5 * BlockLen, Z_mid[1] - 0.5 * BlockLen])
Z_pts.append([Z_mid[0] - 1.5 * BlockLen, Z_mid[1] + 0.5 * BlockLen])
Z_pts.append([Z_mid[0] - 0.5 * BlockLen, Z_mid[1] - 0.5 * BlockLen])
Z_pts.append([Z_mid[0] - 0.5 * BlockLen, Z_mid[1] + 0.5 * BlockLen])
Z_pts.append([Z_mid[0] - 0.5 * BlockLen, Z_mid[1] + 1.5 * BlockLen])
Z_pts.append([Z_mid[0] + 0.5 * BlockLen, Z_mid[1] - 0.5 * BlockLen])
Z_pts.append([Z_mid[0] + 0.5 * BlockLen, Z_mid[1] + 0.5 * BlockLen])
Z_pts.append([Z_mid[0] + 0.5 * BlockLen, Z_mid[1] + 1.5 * BlockLen])
Z_pts.append([Z_mid[0] + 1.5 * BlockLen, Z_mid[1] + 0.5 * BlockLen])
Z_pts.append([Z_mid[0] + 1.5 * BlockLen, Z_mid[1] + 1.5 * BlockLen])

#sets array keeping track of which squares in the grid are filled with which tetromino
grid_list = []
for i in range(0,20):
    grid_list.append([False, False, False, False, False, False, False, False, False, False])

def set_current():
    global current, current_mid, current_pts, current_color, update_pts, count, check_pt, first_block, next_block, next_pts, next_color
    if first_block:     
        current = random.choice(['I', 'J', 'L', 'O', 'S', 'T', 'Z'])
        next_block = random.choice(['I', 'J', 'L', 'O', 'S', 'T', 'Z'])
        first_block = False
    else:
        current = next_block
        next_block = random.choice(['I', 'J', 'L', 'O', 'S', 'T', 'Z'])
    #adds a new set of coordinates to be drawn
    current_mid = [0,0]
    update_pts.append([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    count += 1      
    #adds index of point to be used to check, varies on rotation
    check_pt.append(2)
    #resets points to be displayed in next square
    next_pts = []
    #sets newly added coordinates and color based on tetromino type
    if current == 'I': 
        current_color.append('turquoise')
        current_mid[0] = I_mid[0]
        current_mid[1] = I_mid[1]
        for i in range(len(I_pts)):
            update_pts[count][i][0] = I_pts[i][0]
            update_pts[count][i][1] = I_pts[i][1]            
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][6], update_pts[count][5]], [update_pts[count][1], update_pts[count][2], update_pts[count][7], update_pts[count][6]], [update_pts[count][2], update_pts[count][3], update_pts[count][8], update_pts[count][7]], [update_pts[count][3], update_pts[count][4], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'I':    
        next_pts = [[I_pts[0], I_pts[1], I_pts[6], I_pts[5]], [I_pts[1], I_pts[2], I_pts[7], I_pts[6]], [I_pts[2], I_pts[3], I_pts[8], I_pts[7]], [I_pts[3], I_pts[4], I_pts[9], I_pts[8]]]
        next_color = 'turquoise'
    if current == 'J':
        current_color.append('blue')
        current_mid[0] = J_mid[0]
        current_mid[1] = J_mid[1]
        for i in range(len(J_pts)):
            update_pts[count][i][0] = J_pts[i][0]
            update_pts[count][i][1] = J_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][4], update_pts[count][3]], [update_pts[count][1], update_pts[count][2], update_pts[count][5], update_pts[count][4]], [update_pts[count][4], update_pts[count][5], update_pts[count][7], update_pts[count][6]], [update_pts[count][6], update_pts[count][7], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'J':    
        next_pts = [[J_pts[0], J_pts[1], J_pts[4], J_pts[3]], [J_pts[1], J_pts[2], J_pts[5], J_pts[4]], [J_pts[4], J_pts[5], J_pts[7], J_pts[6]], [J_pts[6], J_pts[7], J_pts[9], J_pts[8]]]
        next_color = 'blue'
    if current == 'L':
        current_color.append('orange')
        current_mid[0] = L_mid[0]
        current_mid[1] = L_mid[1]
        for i in range(len(L_pts)):
            update_pts[count][i][0] = L_pts[i][0]
            update_pts[count][i][1] = L_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][3], update_pts[count][2]], [update_pts[count][2], update_pts[count][3], update_pts[count][6], update_pts[count][5]], [update_pts[count][4], update_pts[count][5], update_pts[count][8], update_pts[count][7]], [update_pts[count][5], update_pts[count][6], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'L':
        next_pts = [[L_pts[0], L_pts[1], L_pts[3], L_pts[2]], [L_pts[2], L_pts[3], L_pts[6], L_pts[5]], [L_pts[4], L_pts[5], L_pts[8], L_pts[7]], [L_pts[5], L_pts[6], L_pts[9], L_pts[8]]]
        next_color = 'orange'
    if current == 'O':
        current_color.append('yellow')
        current_mid[0] = O_mid[0]
        current_mid[1] = O_mid[1]
        for i in range(len(O_pts)):
            update_pts[count][i][0] = O_pts[i][0]
            update_pts[count][i][1] = O_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][4], update_pts[count][3]], [update_pts[count][1], update_pts[count][2], update_pts[count][5], update_pts[count][4]], [update_pts[count][3], update_pts[count][4], update_pts[count][7], update_pts[count][6]], [update_pts[count][4], update_pts[count][5], update_pts[count][8], update_pts[count][7]]])
    if next_block == 'O':
        next_pts = [[O_pts[0], O_pts[1], O_pts[4], O_pts[3]], [O_pts[1], O_pts[2], O_pts[5], O_pts[4]], [O_pts[3], O_pts[4], O_pts[7], O_pts[6]], [O_pts[4], O_pts[5], O_pts[8], O_pts[7]]]
        next_color = 'yellow'
    if current == 'S':
        current_color.append('green')
        current_mid[0] = S_mid[0]
        current_mid[1] = S_mid[1]
        for i in range(len(S_pts)):
            update_pts[count][i][0] = S_pts[i][0]
            update_pts[count][i][1] = S_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][4], update_pts[count][3]], [update_pts[count][2], update_pts[count][3], update_pts[count][6], update_pts[count][5]], [update_pts[count][3], update_pts[count][4], update_pts[count][7], update_pts[count][6]], [update_pts[count][5], update_pts[count][6], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'S':
        next_pts = [[S_pts[0], S_pts[1], S_pts[4], S_pts[3]], [S_pts[2], S_pts[3], S_pts[6], S_pts[5]], [S_pts[3], S_pts[4], S_pts[7], S_pts[6]], [S_pts[5], S_pts[6], S_pts[9], S_pts[8]]]
        next_color = 'green'
    if current == 'T':
        current_color.append('purple')
        current_mid[0] = T_mid[0]
        current_mid[1] = T_mid[1]
        for i in range(len(T_pts)):
            update_pts[count][i][0] = T_pts[i][0]
            update_pts[count][i][1] = T_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][4], update_pts[count][3]], [update_pts[count][2], update_pts[count][3], update_pts[count][6], update_pts[count][5]], [update_pts[count][3], update_pts[count][4], update_pts[count][7], update_pts[count][6]], [update_pts[count][6], update_pts[count][7], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'T':
        next_pts = [[T_pts[0], T_pts[1], T_pts[4], T_pts[3]], [T_pts[2], T_pts[3], T_pts[6], T_pts[5]], [T_pts[3], T_pts[4], T_pts[7], T_pts[6]], [T_pts[6], T_pts[7], T_pts[9], T_pts[8]]]
        next_color = 'purple'
    if current == 'Z':
        current_color.append('red')
        current_mid[0] = Z_mid[0]
        current_mid[1] = Z_mid[1]
        for i in range(len(Z_pts)):
            update_pts[count][i][0] = Z_pts[i][0]
            update_pts[count][i][1] = Z_pts[i][1]
        current_pts.append([[update_pts[count][0], update_pts[count][1], update_pts[count][3], update_pts[count][2]], [update_pts[count][2], update_pts[count][3], update_pts[count][6], update_pts[count][5]], [update_pts[count][3], update_pts[count][4], update_pts[count][7], update_pts[count][6]], [update_pts[count][6], update_pts[count][7], update_pts[count][9], update_pts[count][8]]])
    if next_block == 'Z':
        next_pts = [[Z_pts[0], Z_pts[1], Z_pts[3], Z_pts[2]], [Z_pts[2], Z_pts[3], Z_pts[6], Z_pts[5]], [Z_pts[3], Z_pts[4], Z_pts[7], Z_pts[6]], [Z_pts[6], Z_pts[7], Z_pts[9], Z_pts[8]]]
        next_color = 'red'

#updates grid array
def grid_check():
    global update_pts, grid_list, current_pts, check_pt, count, game_over
#loops help access all points on the grid
    for l in range(0, 10):               
        for n in range(0, 20):
#resets the grid           
            grid_list[n][l] = False
            for m in range(0,count+1):
#sets each square in grid to which tetromino fills it                
                for i in range(0,len(current_pts[m])):
                    if current_pts[m][i][check_pt[m]][0] - 15 == 165 + 30 * l and current_pts[m][i][check_pt[m]][1] - 15 == 65 + 30 * n:  
                        if grid_list[n][l]==False:
                            grid_list[n][l] = m+1
#player loses if there is an overlap                        
                        elif grid_list[n][l] != count+1:
                            game_over = True
                            timer1.stop()
                            fast_timer1.stop()
                            timer2.stop()
                            fast_timer2.stop()
                            timer3.stop()
                            fast_timer3.stop()
def set_check():
    global current_pts, set_pts, grid_list, set_new
    set_new = False
    for i in range(0,10):
#checks if tetromino hits the bottom
        if grid_list[19][i] == count+1:
            set_new = True
#checks if another tetromino is directly below current
        for n in range(0,19):
            if grid_list[n][i] == count + 1 and (grid_list[n+1][i]!=count+1 and grid_list[n+1][i]!=False):
                set_new = True
#calls function to set new tetromino
    if set_new == True:
        set_current()
            
def boundaries():
    global right_grid, left_grid, grid_list, count
    right_grid = False
    left_grid = False
#determines if current tetromino is on right or left edge
    for i in range(0,20):
        if grid_list[i][9] == count+1:
            right_grid = True
    for i in range(0,20):
        if grid_list[i][0] == count+1:
            left_grid =True
#determines if there is a tetromino directly on the right or left of the current one
    for n in range(0,20):
        for i in range(0,9):
            if grid_list[n][i] == count + 1  and (grid_list[n][i+1]!=count+1 and grid_list[n][i+1]!=False):
                right_grid = True 
        for i in range(1,10):
            if grid_list[n][i] == count + 1  and (grid_list[n][i-1]!=count+1 and grid_list[n][i-1]!=False):
                left_grid = True   
def check_rotate():
    global test_pts, current_mid, update_pts, can_rotate, count, current_test_pts, current_pts, check_pt
    can_rotate = True
    #sets hypothetical rotated points similar to how current_pts is organized
    for i in range(0,len(current_pts[count])):
        for n in range(0,4):
            current_test_pts[i][n][0] = current_mid[0] + current_mid[1] - current_pts[count][i][n][1]
            current_test_pts[i][n][1] = current_mid[1] - current_mid[0] + current_pts[count][i][n][0]
            for m in range(0,count):
                for l in range(0,len(current_pts[m])): 
                    if check_pt[count] == 3:
                        if current_pts[m][l][check_pt[m]][0] - 15 == current_test_pts[i][0][0] - 15 and current_pts[m][l][check_pt[m]][1] - 15 == current_test_pts[i][0][1] - 15:
                            can_rotate = False
                    else: 
                        if current_pts[m][l][check_pt[m]][0] - 15 == current_test_pts[i][check_pt[count]+1][0] - 15 and current_pts[m][l][check_pt[m]][1] - 15 == current_test_pts[i][check_pt[count]+1][1] - 15 and set_new == False:   
                            can_rotate = False
    #sets hypothetical rotated points similar to how update_pts is organized
    for i in range(0,10):
        test_pts[i][0] = current_mid[0] + current_mid[1] - update_pts[count][i][1]
        test_pts[i][1] = current_mid[1] - current_mid[0] + update_pts[count][i][0] 
        if test_pts[i][0] > 450 or test_pts[i][0] < 150 or test_pts[i][1] > 650:
            can_rotate = False
        
def clear_check():
    global current_pts, grid_list, row_filled, clear, count, check_pt, block_under, set_new, lines_cleared, current_mid, total_lines_cleared   
#checks to see if lines need to be cleared and how many    
    for n in range(0,20):
        row_filled = 0       
        for i in range(0,10):
            if grid_list[n][i] != False:
                row_filled+=1
            if row_filled == 10 and set_new == True:                
                clear[n] = True
                lines_cleared +=1  
                total_lines_cleared +=1
                row_filled = 0
                level_update()
#deletes points to clear rows
        if clear[n] == True:                        
            for m in range(0,count):                
                for i in range(len(current_pts[m])-1,-1,-1):
                    if current_pts[m][i-len(current_pts[m])][check_pt[m]][1] - 15 == 65 + 30 * n and set_new == True:  
                        current_pts[m].pop(i-len(current_pts[m]))
                for i in range(0,10):
                    if update_pts[m][i][1] - 15 <= 65 + 30 * (n-1) and set_new == True:
                        update_pts[m][i][1]+=30                        
                clear[n]=False
#updates levels and timers
def level_update():
    global level, total_lines_cleared
    if total_lines_cleared >= 2 and total_lines_cleared <= 3:
        level = 2
        timer1.stop()
        fast_timer1.stop()
        timer2.start()
    if total_lines_cleared >= 4:
        level = 3
        timer2.stop()
        fast_timer2.stop()
        timer3.start()
def score_update():
    global score, lines_cleared
    if lines_cleared == 1:
        score += 80
        lines_cleared = 0
    elif lines_cleared == 2:
        score+= 200
        lines_cleared = 0
    elif lines_cleared == 3:
        score += 600
        lines_cleared = 0
    elif lines_cleared == 4:
        score += 1200
        lines_cleared = 0

def reset():
    global current_pts, update_pts, current_mid, old_pts, current, current_color, count, right_grid, left_grid
    global check_pt, test_pts, can_rotate, set_new, clear, row_filled, block_under, score, lines_cleared, grid_list, first_block, level, total_lines_cleared
    current_mid = []
    current_pts = []
    update_pts = []
    old_pts = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    current_color = []
    count = -1
    right_grid = False
    left_grid = False
    check_pt = []
    test_pts = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    can_rotate = True
    set_new = False
    clear = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    row_filled = 0
    block_under = False
    score = 0
    lines_cleared = 0
    grid_list = []
    for i in range(0,20):
        grid_list.append([False, False, False, False, False, False, False, False, False, False])
    first_block = True
    total_lines_cleared = 0
    level = 1
    set_current()
def draw(canvas):
    #print frame.get_canvas_textwidth('Score', 40)
    if game_start == False:
        canvas.draw_image(intro_background, (1920/2, 1080/2), (1920, 1080), (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
        canvas.draw_text('Tetris', (WIDTH/2-181, HEIGHT/4), 160 , "White")
        canvas.draw_text('Press Space to Start', [WIDTH/2-158, HEIGHT/2+200], 40, 'White')
    if game_start:
        canvas.draw_image(game_background, (298/2, 168/2), (298, 168), (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
        canvas.draw_polygon([(150, 50),(150, HEIGHT - 50),(WIDTH - 150, HEIGHT - 50),(WIDTH - 150, 50)], 5, 'White', 'Black')       
        canvas.draw_polygon([(WIDTH-130, 90),(WIDTH-130, 240),(WIDTH-20, 240),(WIDTH-20, 90)], 5, 'White', 'Black')
        canvas.draw_text('Next', (WIDTH-105, 70), 30, 'White')
        canvas.draw_text('Score:', (WIDTH-110, HEIGHT/2), 30 , "White")
        canvas.draw_text(str(score), (WIDTH-80, HEIGHT/2+50), 30 , "White")  
        canvas.draw_text('Level:', (30,300), 30, 'White')
        canvas.draw_text(str(level), (60, 360), 30, 'White')
        for i in range(0,4):
            try: 
                canvas.draw_polygon([(next_pts[i][0][0]+240, next_pts[i][0][1]+60),(next_pts[i][1][0]+240, next_pts[i][1][1]+60),(next_pts[i][2][0]+240, next_pts[i][2][1]+60),(next_pts[i][3][0]+240, next_pts[i][3][1]+60)], 1, 'black', next_color)
            except IndexError:
                pass
        for n in range(0,count+1):  
            for i in range(0,len(current_pts[n])):
                try:
                    canvas.draw_polygon([(current_pts[n][i][0][0],current_pts[n][i][0][1]), (current_pts[n][i][1][0],current_pts[n][i][1][1]), (current_pts[n][i][2][0],current_pts[n][i][2][1]), (current_pts[n][i][3][0],current_pts[n][i][3][1])],1,'black',current_color[n]) 
                except IndexError:
                    pass  
            
        
    if game_over:
        canvas.draw_text('Press Space to Restart', [WIDTH/2-177, HEIGHT/2+200], 40, 'White')


#key handlers
def keydown(key): 
    global game_start, game_over, current_mid, update_pts, current, old_pts, check_pt, test_pts, can_rotate, count, level
    if key == simplegui.KEY_MAP["space"] and game_start == False:
        game_start = True
        timer1.start()
    elif key == simplegui.KEY_MAP["space"] and game_over:       
        reset()
        game_over = False
       
        timer1.start()
    #right/left movement + rotation
    if game_start == True and game_over == False:
        
        if key == simplegui.KEY_MAP["right"]:  
           
            if right_grid == False:               
                current_mid[0] += 30       
                for i in range(0,10):
                    update_pts[count][i][0]+=30
                    
            grid_check()        
            boundaries()
            check_rotate()
            clear_check()
            score_update()
        if key == simplegui.KEY_MAP["left"]:  
           
            if left_grid == False:  
                current_mid[0] -= 30
                for i in range(0,10):
                    update_pts[count][i][0]-=30
            grid_check()
            boundaries()
            check_rotate()
            clear_check()
            score_update()
        #speeds up downward movement
        if key == simplegui.KEY_MAP["down"]:
            if level == 1:             
                timer1.stop()
                fast_timer1.start()
            if level == 2:
                timer2.stop()
                fast_timer2.start()
            if level == 3:
                timer3.stop()
                fast_timer3.start()
        if key == simplegui.KEY_MAP["z"] and can_rotate == True:
            
            if check_pt[count] == 3:
                check_pt[count] = 0
            else:
                check_pt[count] += 1
            for i in range(0,10):
                old_pts[i][0] = update_pts[count][i][0]
                old_pts[i][1] = update_pts[count][i][1]               
            for i in range(0,10):
                update_pts[count][i][0] = current_mid[0] + current_mid[1] - old_pts[i][1]
                update_pts[count][i][1] = current_mid[1] - current_mid[0] + old_pts[i][0]
            grid_check()
            boundaries()
            check_rotate()
            clear_check()
            score_update()
def keyup(key):
    global game_start, game_over, level 
    if game_start and game_over == False:
        if key == simplegui.KEY_MAP["down"]:
            if level == 1:               
                fast_timer1.stop()
                timer1.start()
            if level == 2:
                fast_timer2.stop()
                timer2.start()
            if level == 3:
                fast_timer3.stop()
                timer3.start()
def move_down():
    global update_pts, count, grid_list, test_pts
    set_check() 
    current_mid[1] += 30
    for i in range(0,10):
        update_pts[count][i][1]+=30
    grid_check()
    check_rotate()
    set_check() 
    boundaries()
    clear_check()
    score_update()
#downward movement            
def timer1_handler():
    move_down()
    
def fast_timer1_handler():
    move_down()

def timer2_handler():
    move_down()
    
def fast_timer2_handler():
    move_down()
    
def timer3_handler():
    move_down()
    
def fast_timer3_handler():
    move_down()
intro_background = simplegui.load_image('http://scoreboredsports.com/wp-content/uploads/2016/05/tetris-2.jpg')
game_background = simplegui.load_image('http://web-vassets.ea.com/Assets/Resources/Image/FeaturedGame/tetris-blitz-thumb.png?cb=1366763145')
# create frame
frame = simplegui.create_frame("Tetris", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#start timer
timer1 = simplegui.create_timer(700, timer1_handler)
fast_timer1 = simplegui.create_timer(70, fast_timer1_handler)
timer2 = simplegui.create_timer(550, timer2_handler)
fast_timer2 = simplegui.create_timer(55, fast_timer2_handler)
timer3 = simplegui.create_timer(300, timer3_handler)
fast_timer3 = simplegui.create_timer(30, fast_timer3_handler)

# start frame
frame.start()
set_current()