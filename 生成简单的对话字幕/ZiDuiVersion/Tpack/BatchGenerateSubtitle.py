def BatchSubtitle(Selector,Scoreboard_name,Scoreboard_scores,StrS):
    Sopenmcfunction=open('AutoT.mcfunction','w')
    Sopenmcfunction.write('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s subtitle " + StrS)
    print('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s subtitle " + StrS)
    Sopenmcfunction.close()