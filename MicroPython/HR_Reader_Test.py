import time
import filefifo

buffer = filefifo.Filefifo('samplecapture03.txt')

fs = 75
is_peak = False
previous_signal = 0

while True:
    current_signal = buffer.get()

    if current_signal > previous_signal:
        is_peak = True

    if is_peak and current_signal < previous_signal:
        print(f"Peak: {previous_signal}")
        is_peak = False

    previous_signal = current_signal

    # print(current_signal)
    time.sleep(1 / fs)
