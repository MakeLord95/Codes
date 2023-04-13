import time
import filefifo


def scale(x):
    y = 2 * x - 46000
    y = max(y, 0)
    y = min(y, 65536)
    return y


buffer = filefifo.Filefifo('samplecapture03.txt')

fs = 75
peak_candidate = False
previous_signal = 0
peaks = []
while True:
    current_signal = scale(buffer.get())

    if current_signal < 0:
        print("End of file!")
        break

    if current_signal > previous_signal:
        peak_candidate = True

    elif peak_candidate and current_signal < previous_signal:
        peaks.append(previous_signal)
        peak_candidate = False

    previous_signal = current_signal

    # print(current_signal)
    time.sleep(1 / fs)
