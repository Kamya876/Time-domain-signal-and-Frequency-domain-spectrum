import numpy as np
import matplotlib.pyplot as plt

# Generate a time-domain signal (example: a sine wave)
duration = 5  # Duration of the signal in seconds
sampling_rate = 1000  # Number of samples per second
t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)  # Time vector
frequency = 10  # Frequency of the sine wave
signal = np.sin(2 * np.pi * frequency * t)

# Perform Fourier Transform
frequency_spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1/sampling_rate)

# Plot the time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time Domain Signal')

# Plot the frequency-domain spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(frequency_spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Domain Spectrum')

plt.tight_layout()
plt.show()
