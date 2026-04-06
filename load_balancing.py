### 4. Implementasi Python


import heapq

# Data task (durasi)
tasks = [12, 7, 9, 4, 15, 6, 10, 8]

# Jumlah node/server
num_servers = 3

# Inisialisasi heap (beban_awal, id_node)
servers = [(0, i) for i in range(num_servers)]
heapq.heapify(servers)

# Menyimpan hasil pembagian task
assignments = {i: [] for i in range(num_servers)}

print("=== Simulasi Dynamic Load Balancing (Min-Heap) ===")
print("Task       :", tasks)
print("Jumlah node:", num_servers)
print()

# Proses pembagian task
for task_id, duration in enumerate(tasks, start=1):
    current_load, server_id = heapq.heappop(servers)

    start_time = current_load
    finish_time = current_load + duration

    # Simpan hasil
    assignments[server_id].append((task_id, duration, start_time, finish_time))

    # Update heap
    heapq.heappush(servers, (finish_time, server_id))

    print(f"Task-{task_id:02d} ({duration}s) -> Node-{server_id} "
          f"[start={start_time}, finish={finish_time}]")

# Hitung total beban akhir
print("\n=== Ringkasan Beban Akhir ===")
final_loads = sorted(servers, key=lambda x: x[1])

for load, server_id in final_loads:
    print(f"Node-{server_id}: total beban {load}s")

# Makespan
makespan = max(load for load, _ in servers)
print(f"\nMakespan (waktu selesai total) = {makespan}s")

# Detail tiap node
print("\n=== Detail Penugasan per Node ===")
for server_id, tasks_list in assignments.items():
    print(f"Node-{server_id}:")
    for t in tasks_list:
        print(f"  - Task-{t[0]:02d} durasi={t[1]}s "
              f"(start={t[2]}, finish={t[3]})")

