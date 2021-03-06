#회전 리스트 이동으로 표현
#12시 방향과 맞닿는 부분의 차이 += 2
#중간에 물려있는 톱니바퀴 -2 0 +2

#점수 12시방향을 기준으로 n은 0점 s는 [1,2,4,8]점

#n극 0, s극 1

# 시계 1, 반시계 -1
############################################1
# input1 = ["10101111","01111101","11001110","00000010"]
# input2 = 2
# Gear_list = [list(map(str, i)) for i in input1]
# rot =input2
# rot_gear=[[3,-1],[1,1]]
############################################2
# input1 = ["10001011","10000011","01011011","00111101"]
# input2 = 5
# Gear_list = [list(map(str, i)) for i in input1]
# rot =input2
# rot_gear=[[1, 1],[2, 1],[3, 1],[4, 1],[1, -1]]
############################################3
# input1 = ["10010011","01010011","11100011","01010101"]
# input2 = 8
# Gear_list = [list(map(str, i)) for i in input1]
# rot =input2
# rot_gear=[[1, 1],[2, 1],[3, 1],[4, 1],[1, -1],[2, -1],[3, -1],[4, -1]]
############################################3
# input1 = ["11111111","11111111","11111111","11111111"]
# input2 = 3
# Gear_list = [list(map(str, i)) for i in input1]
# rot =input2
# rot_gear=[[1, 1],[2, 1],[3, 1]]

Gear_list = [list(map(str, input())) for _ in range(4)]

rot = int(input())

rot_gear=[list(map(int, input().split())) for _ in range(rot)]

rp_List = [2 for _ in range(len(Gear_list))]

teeth_len = 8

rp_lp_interval = 4




def rotate_gear(gear_no, direct, rot_d): # direct -1:왼편, 1:오른편
    global rp_List, teeth_len, Gear_list, rp_lp_interval 

    
    other_g = gear_no + direct
    
    if (other_g) < len(Gear_list) and (other_g) >= 0:
        
        if direct == 1:
            
            other_lp = rp_List[other_g] - rp_lp_interval 
            other_lp = other_lp if other_lp > -teeth_len else  other_lp + teeth_len
            
            pre_gear_rp = rp_List[gear_no]
            
            if Gear_list[other_g][other_lp] != Gear_list[gear_no][pre_gear_rp]:
                rotate_gear(other_g, 1, rot_d*-1)

        else:
            
            other_rp = rp_List[other_g]
            pre_gear_lp = rp_List[gear_no] - rp_lp_interval 
            pre_gear_lp = pre_gear_lp if pre_gear_lp > -teeth_len else  pre_gear_lp + teeth_len
            
            if Gear_list[other_g][other_rp] != Gear_list[gear_no][pre_gear_lp]:
                rotate_gear(other_g, -1, rot_d*-1)
                


    rp_List[gear_no] = (rp_List[gear_no] + (rot_d) + teeth_len) % (teeth_len)
    print(direct," :: ",rp_List)

if rot != 0 or len(list(set(list(map(tuple,Gear_list))))) > 1:
    
    for g_no, rot_direct in rot_gear:
        g_no = g_no -1

        check_gear = [ i for i in [-1,1] if (g_no + i) >=0 and (g_no + i)  < len(Gear_list) ]
        print(check_gear)
        for direct in check_gear:
            
            rotate_gear(g_no, direct, rot_direct * -1)
            if len(check_gear) == 2 and direct == -1 :
                rp_List[g_no] = (rp_List[g_no] + (rot_direct) + teeth_len) % (teeth_len)
        

# total_score
answer = 0
for i in range(len(Gear_list)):
    answer += int(Gear_list[i][rp_List[i] - int(rp_lp_interval / 2)]) * (2**i)


print(answer)


'''
00010101
00000101
00101010
10110000
1
3 1
'''