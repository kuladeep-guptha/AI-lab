#Shyam likes mango
# Seema is a girl
# Bill likes Cindy
# Rose is red
# John owns gold 



import pytholog as pl

new_kb = pl.KnowledgeBase("kuladeep")

new_kb(["likes(shyam,mango)",
        "girl(seema)",
        "likes(bill,cindy)",
        "red(rose)",
        "owns(john,gold)"
        ])


 
print(new_kb.query(pl.Expr("likes(shyam,What)")))