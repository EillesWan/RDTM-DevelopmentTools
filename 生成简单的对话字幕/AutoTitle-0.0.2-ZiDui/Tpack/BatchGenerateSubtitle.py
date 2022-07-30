def BatchSubtitle(Selector,Scoreboard_name,Scoreboard_scores,StrS):
    Sopenmcfunction = open('AutoT.mcfunction', 'a')
    Sopenmcfunction.write('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s subtitle " + StrS+"\n")
    print('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s subtitle " + StrS)
    Sopenmcfunction.close()