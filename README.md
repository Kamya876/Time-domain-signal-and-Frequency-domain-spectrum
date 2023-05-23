# Time-domain-signal-and-Frequency-domain-spectrum
The code then plots the time-domain signal and the frequency-domain spectrum using plt.subplot and plt.plot from the Matplotlib library. 
We create a time domain signal which is a sine wave of 10Hz,signal is generated with the help of np.sin function and the time vector t which is created using np.linspace.
Next step is to perform Fourier tranform on the signal using 'np.fft.fft' which helps us to compute the Frequency domain sperctrum.
'np.fft.fftfreq' is used to obtain the corresponding frequencies for each point in the spectrum.
Then the code plots the time-domain signal and the frequency-domain spectrum using plt.subplot and plt.plot from the Matplotlib library.
After running this code it will display two plots  one for the time-domain signal and the other is the frequency-domain spectrum.
You can modify the signal generation parameters and customize the plot settings according to your needs.
By comparing the time-domain signal and the frequency-domain spectrum, you can observe the relationship between the original signal and its frequency components.
