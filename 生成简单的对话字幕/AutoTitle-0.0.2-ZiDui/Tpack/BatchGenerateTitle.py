def BatchTitle(Selector,Scoreboard_name,Scoreboard_scores,StrT):
    Topenmcfunction=open('AutoT.mcfunction','a')
    Topenmcfunction.write('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s title " + StrT+"\n")
    print('/execute @a' + Selector + " ~ ~ ~ " + "/execute @s[scores={" + Scoreboard_name + "=" + str(
        Scoreboard_scores) + "}] ~ ~ ~ " + "/title @s title " + StrT)
    Topenmcfunction.close()
