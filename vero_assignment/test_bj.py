from vero_assignment.Classes import Card,Hand
"""Test file"""
c=Card(5,"s")
d=Card(6,"d")
hand=Hand()
vhand=[]
vhand.append(c.bjValue())
vhand.append(d.bjValue())
print(vhand)
if sum(vhand)==11 and (vhand[0]==1 or vhand[1]==1):
    print("blackjack")
print(sum(vhand))
b=["h","k","l"]
del b[:]
print(b)
