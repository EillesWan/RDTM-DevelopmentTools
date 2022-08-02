def BatchTitle(Selector,Scoreboard_name,Scoreboard_scores,StrT):
    Topenmcfunction=open('AutoT.mcfunction','a')
    Topenmcfunction.write('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s title " + StrT+"\n")
    Topenmcfunction.close()

def BatchSubtitle(Selector,Scoreboard_name,Scoreboard_scores,StrS):
    Sopenmcfunction = open('AutoT.mcfunction', 'a')
    Sopenmcfunction.write('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s subtitle " + StrS+"\n")
    Sopenmcfunction.close()