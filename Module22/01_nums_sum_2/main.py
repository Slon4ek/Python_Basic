read_file = open('numbers.txt', 'r')
write_file = open('answer.txt', 'w')

nums = read_file.read().split()
summ = 0

for num in nums:
    summ += int(num)

write_file.write(str(summ))

read_file.close()
write_file.close()
