for i in range(2,21):
    with open(f"tables/Multiplication table_of{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
