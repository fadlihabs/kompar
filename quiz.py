import random
import time
from multiprocessing import Pool
from threading import Thread

# DATA PARALLELISM FUNCTIONS
def process_vehicle_count(data):
    return [d * 2 for d in data]
def process_speed(data):
    return [d + random.randint(1, 10) for d in data]
def process_density(data):
    return [d * random.uniform(0.7, 1.2) for d in data]
def run_process(args):
    func, data = args
    return func(data)

# TASK PARALLELISM FUNCTIONS
def detect_congestion(density):
    print("Deteksi kemacetan...")
    time.sleep(1)
    if max(density) > 70:
        print("Kemacetan tinggi terdeteksi!")
def predict_traffic(speed):
    print("Prediksi kondisi lalu lintas...")
    time.sleep(1)
    avg_speed = sum(speed) / len(speed)
    print("Rata-rata kecepatan:", round(avg_speed, 2))
def route_recommendation():
    print("Menghitung rekomendasi rute...")
    time.sleep(1)
    print("Rekomendasi: Gunakan jalur alternatif.")

# MAIN PROGRAM
if __name__ == "__main__":
    print("=== SMART TRAFFIC ANALYSIS (REAL-TIME SIMULATION) ===\n")
    # Generate data random (simulasi sensor)
    vehicle_data = [random.randint(10, 50) for _ in range(5)]
    speed_data = [random.randint(30, 80) for _ in range(5)]
    density_data = [random.randint(40, 100) for _ in range(5)]
    print("Data Sensor:")
    print("Vehicle:", vehicle_data)
    print("Speed:", speed_data)
    print("Density:", density_data)
    
    # DATA PARALLELISM
    with Pool(3) as p:
        results = p.map(run_process, [
            (process_vehicle_count, vehicle_data),
            (process_speed, speed_data),
            (process_density, density_data)
        ])
    vehicle_result, speed_result, density_result = results
    print("\nHasil Data Parallelism:")
    print("Vehicle:", vehicle_result)
    print("Speed:", speed_result)
    print("Density:", [round(d, 2) for d in density_result])
    
    # TASK PARALLELISM
    print("\nMenjalankan Task Parallelism...\n")
    t1 = Thread(target=detect_congestion, args=(density_result,))
    t2 = Thread(target=predict_traffic, args=(speed_result,))
    t3 = Thread(target=route_recommendation)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("\n PROGRAM SELESAI ")