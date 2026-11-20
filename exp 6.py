import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Student Details
name = "jenish desai"
enrollment_no = "92510133025"

# FIR Low-Pass Filter Parameters
Fs = 10000          # Sampling frequency = 10 kHz
Fc = 3000           # Cutoff frequency = 3 kHz
N = 31              # Number of filter taps

# Design FIR Low-Pass Filter using Hann Window
b = firwin(
    numtaps=N,
    cutoff=Fc,
    window="hann",
    pass_zero="lowpass",
    fs=Fs
)

# Calculate Frequency Response
f, H = freqz(b, worN=2048, fs=Fs)

# Magnitude Response in dB
magnitude_db = 20 * np.log10(
    np.maximum(np.abs(H), 1e-10)
)

# Display Filter Coefficients
print("==========================================")
print("       FIR LOW-PASS FILTER")
print("==========================================")
print("Name           :", name)
print("Enrollment No. :", enrollment_no)
print("Sampling Frequency:", Fs, "Hz")
print("Cutoff Frequency  :", Fc, "Hz")
print("Number of Taps    :", N)
print("\nFilter Coefficients:")
print(b)

# Plot Frequency Response
plt.figure(figsize=(10, 6))
plt.plot(f, magnitude_db)
plt.title("FIR Low-Pass Filter - Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.xlim(0, Fs / 2)
plt.ylim(-100, 5)
plt.tight_layout()
plt.show()











import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Student Details
name = "jenish desai"
enrollment_no = "92510133025"

# FIR High-Pass Filter Parameters
Fs = 10000
Fc = 3000
N = 31

# Design FIR High-Pass Filter using Hann Window
b = firwin(
    numtaps=N,
    cutoff=Fc,
    window="hann",
    pass_zero="highpass",
    fs=Fs
)

# Calculate Frequency Response
f, H = freqz(b, worN=2048, fs=Fs)

# Magnitude Response in dB
magnitude_db = 20 * np.log10(
    np.maximum(np.abs(H), 1e-10)
)

# Display Results
print("==========================================")
print("       FIR HIGH-PASS FILTER")
print("==========================================")
print("Name           :", name)
print("Enrollment No. :", enrollment_no)
print("Sampling Frequency:", Fs, "Hz")
print("Cutoff Frequency  :", Fc, "Hz")
print("Number of Taps    :", N)
print("\nFilter Coefficients:")
print(b)

# Plot Frequency Response
plt.figure(figsize=(10, 6))
plt.plot(f, magnitude_db)
plt.title("FIR High-Pass Filter - Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.xlim(0, Fs / 2)
plt.ylim(-100, 5)
plt.tight_layout()
plt.show()






















import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Student Details
name = "jenish desai"
enrollment_no = "92510133025"

# FIR Band-Pass Filter Parameters
Fs = 20000          # Sampling frequency = 20 kHz
F_low = 3000        # Lower cutoff = 3 kHz
F_high = 6000       # Upper cutoff = 6 kHz
N = 31              # Number of filter taps

# Design FIR Band-Pass Filter using Hann Window
b = firwin(
    numtaps=N,
    cutoff=[F_low, F_high],
    window="hann",
    pass_zero="bandpass",
    fs=Fs
)

# Calculate Frequency Response
f, H = freqz(b, worN=2048, fs=Fs)

# Magnitude Response in dB
magnitude_db = 20 * np.log10(
    np.maximum(np.abs(H), 1e-10)
)

# Display Results
print("==========================================")
print("       FIR BAND-PASS FILTER")
print("==========================================")
print("Name              :", name)
print("Enrollment No.    :", enrollment_no)
print("Sampling Frequency:", Fs, "Hz")
print("Lower Cutoff      :", F_low, "Hz")
print("Upper Cutoff      :", F_high, "Hz")
print("Number of Taps    :", N)
print("\nFilter Coefficients:")
print(b)

# Plot Frequency Response
plt.figure(figsize=(10, 6))
plt.plot(f, magnitude_db)
plt.title("FIR Band-Pass Filter - Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.xlim(0, Fs / 2)
plt.ylim(-100, 5)
plt.tight_layout()
plt.show()
















import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Student Details
name = "jenish desai"
enrollment_no = "92510133025"

# FIR Band-Stop Filter Parameters
Fs = 20000
F_low = 3000
F_high = 6000
N = 31

# Design FIR Band-Stop Filter using Hann Window
b = firwin(
    numtaps=N,
    cutoff=[F_low, F_high],
    window="hann",
    pass_zero="bandstop",
    fs=Fs
)

# Calculate Frequency Response
f, H = freqz(b, worN=2048, fs=Fs)

# Magnitude Response in dB
magnitude_db = 20 * np.log10(
    np.maximum(np.abs(H), 1e-10)
)

# Display Results
print("==========================================")
print("       FIR BAND-STOP FILTER")
print("==========================================")
print("Name              :", name)
print("Enrollment No.    :", enrollment_no)
print("Sampling Frequency:", Fs, "Hz")
print("Lower Cutoff      :", F_low, "Hz")
print("Upper Cutoff      :", F_high, "Hz")
print("Number of Taps    :", N)
print("\nFilter Coefficients:")
print(b)

# Plot Frequency Response
plt.figure(figsize=(10, 6))
plt.plot(f, magnitude_db)
plt.title("FIR Band-Stop Filter - Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.xlim(0, Fs / 2)
plt.ylim(-100, 5)
plt.tight_layout()
plt.show()