from multiprocessing import Pool
from threading import Thread

# =========================
# DATA PARALLELISM FUNCTIONS
# =========================
def process_vehicle_count(data):
    return [d * 2 for d in data]

def process_speed(data):
    return [d + 5 for d in data]

def process_density(data):
    return [d * 0.8 for d in data]

# Helper function (WAJIB buat multiprocessing)
def run_process(args):
    func, data = args
    return func(data)

# =========================
# TASK PARALLELISM FUNCTIONS
# =========================
def detect_congestion(density):
    print("Deteksi kemacetan...")
    if max(density) > 70:
        print("Kemacetan tinggi terdeteksi!")

def predict_traffic(speed):
    print("Prediksi kondisi lalu lintas...")
    avg_speed = sum(speed) / len(speed)
    print("Rata-rata kecepatan:", avg_speed)

def route_recommendation():
    print("Rekomendasi: Gunakan jalur alternatif.")

# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":
    print("=== SMART TRAFFIC ANALYSIS ===")

    vehicle_data = [10, 20, 30, 40]
    speed_data = [40, 50, 45, 60]
    density_data = [60, 75, 80, 55]

    # =========================
    # DATA PARALLELISM
    # =========================
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
    print("Density:", density_result)

    # =========================
    # TASK PARALLELISM
    # =========================
    print("\nMenjalankan Task Parallelism...")

    t1 = Thread(target=detect_congestion, args=(density_result,))
    t2 = Thread(target=predict_traffic, args=(speed_result,))
    t3 = Thread(target=route_recommendation)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\n=== PROGRAM SELESAI ===")