import subprocess
import time

while True:
    try:
        # اجرای دستور termux-touch برای دریافت موقعیت موس
        result = subprocess.run(["termux-touch"], capture_output=True, text=True)
        output = result.stdout.strip()

        # جداسازی مختصات x و y از خروجی دستور
        coordinates = output.split()
        if len(coordinates) == 2:
            x, y = map(int, coordinates)
            print(f" x={x}, y={y}")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(1)  # منتظر یک ثانیه بمانید تا موقعیت موس به‌روز شود
