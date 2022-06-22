import pandas as pd
import statistics

df = pd.read_csv(r"C:\Users\MONSTER\Desktop\output2.csv", sep=",", header=None)

def main():
    word_count_array = []

    for i in range(len(df.values)):
        a_string = df.values[i][0]
        word_list = a_string.split()
        number_of_words = len(word_list)
        word_count_array.append(number_of_words)

    total = 0
    for i in range(len(word_count_array)):
        total = total + word_count_array[i]
    average = total / len(word_count_array)

    print(word_count_array)
    print("Count: ", len(word_count_array))
    print("Std:", int(statistics.stdev(word_count_array)))
    print("Average: ", int(average))



if __name__ == '__main__':
    main()


