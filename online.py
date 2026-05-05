import multiprocessing
import time
import random

def task(n):
    work_time = random.uniform(0.5, 2)
    print(f"Task {n} dikerjakan selama {work_time:.2f} detik")
    time.sleep(work_time)
    return n * 2

def static_worker(tasks):
    results = []
    for t in tasks:
        results.append(task(t))
    return results


def run_static():
    print("\n=== STATIC DISTRIBUTION ===")
    start = time.time()

    tasks = list(range(1, 11))

    
    worker1_tasks = tasks[:7]
    worker2_tasks = tasks[7:]

    with multiprocessing.Pool(2) as p:
        results = p.map(static_worker, [worker1_tasks, worker2_tasks])

    end = time.time()
    print("Hasil:", results)
    print("Waktu:", round(end - start, 2), "detik")

def dynamic_worker(queue, result):
    while True:
        try:
            task_id = queue.get_nowait()
        except:
            break
        result.put(task(task_id))


def run_dynamic():
    print("\n=== DYNAMIC DISTRIBUTION ===")
    start = time.time()

    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    for i in range(1, 11):
        task_queue.put(i)

    workers = []
    for _ in range(3):
        p = multiprocessing.Process(target=dynamic_worker, args=(task_queue, result_queue))
        workers.append(p)
        p.start()

    for w in workers:
        w.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    end = time.time()
    print("Hasil:", results)
    print("Waktu:", round(end - start, 2), "detik")
if __name__ == "__main__":
    run_static()
    run_dynamic()