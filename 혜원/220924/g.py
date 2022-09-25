from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    dead = defaultdict(tuple)

    for term in terms:
        a,b = term.split(' ')
        dead[a] = int(b)
    
    year, month, day = map(int, today.split('.'))
    for idx, priv in enumerate(privacies):
        p_year, p_month, p_day = map(int, priv.split(' ')[0].split('.'))
        p_dead = priv.split(' ')[1]

        p_month += dead[p_dead]
        year_plus, p_month = divmod(p_month, 12)
        p_year += year_plus

        if p_year>year:
            continue
        if p_year==year and p_month>month:
            continue
        if p_year==year and p_month==month and p_day>day:
            continue
        answer.append(idx+1)

    # print(dead)

    return answer



    #----------------------------------------------------------

    def solution(cap, n, deliveries, pickups):
    answer = 0
    next_del, next_pick = n-1, n-1
    for i in range(n-1, -1, -1):
        if deliveries[i]>0:
            next_del = i
            break
    for i in range(n-1, -1, -1):
        if pickups[i]>0:
            next_pick = i
            break

    while sum(deliveries)>0 or sum(pickups)>0:
        dest = max(next_del, next_pick)
        truck = 0
        answer += (dest+1)*2
        for i in range(next_del, -1, -1):
            if truck + deliveries[i] <= cap:
                truck += deliveries[i]
                deliveries[i] = 0
                next_del = i-1 if i>0 else 0
            else:
                deliveries[i] -= cap - truck
                truck = cap
                next_del = i
                break
        truck = 0
        for i in range(next_pick, -1, -1):
            if truck + pickups[i] <= cap:
                truck += pickups[i]
                pickups[i] = 0
                next_pick = i-1 if i>0 else 0
            else:
                pickups[i] -= cap - truck
                truck = cap
                next_pick = i
                break
        
    return answer

    #-----------------------------------------
    from collections import deque

def solution(commands):
    answer = []
    table = [[None]*50 for _ in range(50)]
    # print(table)
    merged = []
    merge_list = []
    merge_value = []

    for command in commands:
        comm = command.split(' ')[0]
        args = len(list(command.split(' ')))-1

        if comm == 'UPDATE':
            if args == 3:
                _,x,y,val = command.split(' ')
                x,y = int(x)-1,int(y)-1
                if (x,y) in merged:
                     merge_value[table[x][y]] = val   
                else:
                    table[x][y] = val
            else:
                _,val1,val2 = command.split(' ')
                for row in range(50):
                    for col in range(50):
                        if (row,col) in merged:
                            if merge_value[table[row][col]] == val1:
                                merge_value[table[row][col]] = val2
                        else:
                            if table[row][col] == val1:
                                table[row][col] = val2
        elif comm == 'MERGE':
            _, r1, c1, r2, c2 = command.split(' ')
            r1, c1, r2, c2 = int(r1)-1, int(c1)-1, int(r2)-1, int(c2)-1
            if (r1,c1) in merged:
                merge_list[table[r1][c1]].append((r2,c2))
                if (r2,c2) in merged:
                    for newr,newc in merge_list[table[r2][c2]]:
                        table[newr][newc] = table[r1][c1]
                        merge_list[table[r1][c1]].append((newr,newc))
                table[r2][c2] = table[r1][c1]
            elif (r2,c2) in merged:
                merge_list[table[r2][c2]].append((r1,c1))
                table[r1][c1] = table[r2][c2]
                merged.append((r1,c1))
        

        #     if (r1,c1) in merged:
        #         base_merged_r, base_merged_c, new_merged_r, new_merged_c = r1, c1, r2, c2 
        #         base_idx = table[base_merged_r][base_merged_c]

        #         que1 = deque((base_merged_r,base_merged_c))
        #         while que1:
        #             new_merged_r, new_merged_c = que1.popleft()
        #             merge_list[base_idx].append((new_merged_r, new_merged_c))
        #             if (new_merged_r, new_merged_c) in merged:
        #                 for news_r, news_c in merge_list[table[new_merged_r][new_merged_c]]:
        #                     if (news_r, news_c) not in merge_list[base_idx]:
        #                         que1.append((news_r,news_c))
        #             table[new_merged_r][new_merged_c] = base_idx
        #     elif (r2,c2) in merged:
        #         base_merged_r, base_merged_c, new_merged_r, new_merged_c = r2, c2, r1, c1 
        #         base_idx = table[base_merged_r][base_merged_c]

        #         que2 = deque((base_merged_r,base_merged_c))
        #         while que2:
        #             new_merged_r, new_merged_c = que2.popleft()
        #             merge_list[base_idx].append((new_merged_r, new_merged_c))
        #             if (new_merged_r, new_merged_c) in merged:
        #                 for news_r, news_c in merge_list[table[new_merged_r][new_merged_c]]:
        #                     if (news_r, news_c) not in merge_list[base_idx]:
        #                         que2.append((news_r,news_c))
        #                 merge_list[table[new_merged_r][new_merged_c]] = []
        #                 merge_value[table[new_merged_r][new_merged_c]] = ''
        #             else:
        #                 merged.append((new_merged_r, new_merged_c))
        #             table[new_merged_r][new_merged_c] = base_idx

            else:
                merged.append((r1, c1))
                merged.append((r2, c2))
                merge_list.append([(r1,c1),(r2,c2)])
                idx = len(merge_list)-1
                value = table[r1][c1] if table[r1][c1] else table[r2][c2]
                merge_value.append(value)
                table[r1][c1] = idx
                table[r2][c2] = idx
        elif comm == 'UNMERGE':
            _, r, c = command.split(' ')
            r,c = int(r)-1,int(c)-1
            idx = table[r][c]
            for tmp_r, tmp_c in merge_list[idx]:
                table[tmp_r][tmp_c] = None
                if (tmp_r,tmp_c) in merged:
                    merged.remove((tmp_r,tmp_c))
            table[r][c] = merge_value[idx]
            merge_list[idx] = []
            merge_value[idx] = ''
            # merged.remove((r,c))
        else:
            _, r, c = command.split(' ')
            r,c = int(r)-1,int(c)-1
            result = ''
            if table[r][c]:
                if (r,c) in merged:
                    result = merge_value[table[r][c]]
                else:
                    result = table[r][c]
            else:
                result = 'EMPTY'
            answer.append(result)
            
    
    return answer