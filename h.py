import random


for i in range (1,11):

    t = random.randint(1, 10)
    input_1 = str(t) + "\n"
    output_1 = ""

    ip_str = "input"+str(i)+".txt"
    outp_str = "output"+str(i)+".txt"

    for _ in range(t):
        x = random.randint(100, 10000)
        x = x - (x % 100)  # Ensuring x is a multiple of 100
        input_1 += str(x) + "\n"

        disc = (x * 20) // 100
        if disc > 150:
            output_1 += str(disc) + "\n"
        else:
            output_1 += "150\n"

    with open(ip_str, "w") as file1:
        file1.write(input_1)
    with open(outp_str, "w") as file2:
        file2.write(output_1)
