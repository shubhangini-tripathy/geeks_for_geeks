def studentScore(name, *score):
    print("{} got {} in Physics {} in Chemistry {} in Maths".format(
        name, score[0], score[1], score[2]))
    # print(name, "Got", score[0], "In", "Physics", name, "Got",
        #   score[1], "In", "Chem", name, "Got", score[2], "In", "maths")


studentScore("mark", 12, 14, 15)
print("Shubhi")
studentScore("shubhi", 12, 14, 15)
