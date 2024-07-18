beatles = []

# step 1
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    beatles.append(member)
print("Step 3:", beatles)

# step 4
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
