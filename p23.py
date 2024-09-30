n=int(input("Enter no.of players:\n"))
player_dtls={}
for i in range(n):
    plyr_nm=input("Enter playername:\n")
    plyr_scr=input("Enter playerscore:\n")
    player_dtls[plyr_nm]=plyr_scr
print("Player Details:",player_dtls)
