from multiprocessing import Pool, cpu_count
import time

def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if line == '':
                print(f'Reading from file "{name}", ended')
                break
            else:
                all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
print(filenames)

#start_t = time.time()
#for i in filenames:
#    read_info(i)
#stop_t = time.time()
#job_t = round(stop_t - start_t, 5)
#print(job_t)

if __name__ == '__main__':
    with Pool() as pool:
        start_t = time.time()
        pool.map(read_info, filenames)
        stop_t = time.time()
        job_t = round(stop_t - start_t, 5)
        print(job_t)
