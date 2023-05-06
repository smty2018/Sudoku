table = Texttable()
table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.HLINES | Texttable.BORDER)
table.add_rows([ ["Name", "Age", "Nickname"],
                     ["Xavier Huon", 32, "Xav'"],
                     ["Baptiste Clement", 1, "Baby"] ])
print table.draw()
