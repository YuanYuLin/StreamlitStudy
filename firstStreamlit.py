import streamlit as st
import graphviz

st.title("🏆 垂直式比賽晉級圖")

# 1. 建立 Digraph
# rankdir='TB': 由上往下 (Top to Bottom)
# splines='ortho': 使用折線 (直角線條)，看起來更像傳統樹狀圖
dot = graphviz.Digraph(comment='Tournament Bracket', 
                       graph_attr={'rankdir': 'BT', 'splines': 'ortho', 'nodesep': '0.8'})

# 2. 設定節點樣式 (使用 record 形狀來分割比分)
dot.attr('node', shape='record', style='filled', fillcolor='white', fontname='Arial')

team_default =  {'Id':'TeamDefault', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]}
teams = [
    {'Id':'Team1', 'Name':'輪空', 'WonCount':1, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team2', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team3', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team4', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team5', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team6', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team7', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]},
    {'Id':'Team8', 'Name':'輪空', 'WonCount':0, 'Score':[
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0},
        {"Point":0, "Round":0}
        ]}
]

def pairMatches(level, parent_matches, teams):
    if len(teams) == 1:
        return 
    matches = []
    count = 0
    for i in range(0, len(teams), 2):
        current_match = [[], []]
        matches.append(current_match)

    parent_matches.append(matches)
    pairMatches(level+1, parent_matches, matches)
    return 
    
def fillMatches(level, matches, teams):
    teams_len = len(teams)

    if teams_len == 1:
        return
        
    level_matches_len = len(matches[level])

    if level_matches_len != (int(teams_len/2)) :
        teams_len
        level_matches_len
        return
        
    for team_index in range(0, teams_len):
        match_index = int(team_index / 2)
        matches[level][match_index][team_index % 2] = teams[team_index]
        
    # matches[level]
    new_teams = []
    matches_len = len(matches[level])
    for match_index in range(0, matches_len):
        # match_index, level
        # matches[level][match_index]
        match = matches[level][match_index]
        #new_teams.append([])
        new_teams.append(team_default)
        #match
        for team in match:
            if team["WonCount"] > level :
                new_teams[match_index] = team

    next_level = level + 1
    fillMatches(next_level, matches, new_teams)
        
    return 
def showMatches(level, matches):
    
    
    if level >= len(matches):
        return 
    #level
    #matches[level]    
    for match_index in range(0, len(matches[level])):
        match = matches[level][match_index]
        id1= match[0]['Id']
        name1 = match[0]['Name']
        round1 = match[0]['Score'][0]['Round']
        point1 = match[0]['Score'][0]['Point']
        
        id2= match[1]['Id']
        name2 = match[1]['Name']
        round2 = match[1]['Score'][0]['Round']
        point2 = match[1]['Score'][0]['Point']

        group_name = str(level) + str(match_index) #+ id1 + id2
        dot.node(group_name, label=f"{{ {{ {name1} | {round1} | {point1} }} | {{ {name2} | {round2} | {point2} }} }}")
        #str(level + 1) , str(int(match_index / 2))
        dot.edge(group_name, str(level + 1) + str(int(match_index / 2)))

    showMatches(level+1, matches)
    
# === 第一輪 (8強或4強) ===
# 為了排版好看，可以把同一層級的節點設為相同的 rank (但在簡單樹狀圖中 Graphviz 會自動處理)
matches = []
pairMatches(0, matches, teams)
# matches
fillMatches(0, matches, teams)
#matches
showMatches(0, matches)

# 顯示圖表
st.graphviz_chart(dot)
