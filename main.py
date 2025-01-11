# Made by Eduard Wojnar 
# 15/7/2024

import machine
import neopixel
import time
import esp
import os
import uasyncio as asyncio
from machine import Pin

# Definice pinů
TRIG1_PIN = 14
ECHO1_PIN = 12

TRIG2_PIN = 17
ECHO2_PIN = 16

LED_PIN = Pin(26, Pin.OUT)
NUM_PIXELS = 300

AUDIO_PIN = 25

# Nastavení ultrazvukových čidel
trig1 = machine.Pin(TRIG1_PIN, machine.Pin.OUT)
echo1 = machine.Pin(ECHO1_PIN, machine.Pin.IN)
trig2 = machine.Pin(TRIG2_PIN, machine.Pin.OUT)
echo2 = machine.Pin(ECHO2_PIN, machine.Pin.IN)

# Nastavení NeoPixel
np = neopixel.NeoPixel(LED_PIN, NUM_PIXELS)


# Nastavení DAC pro zvuk
dac = machine.DAC(machine.Pin(AUDIO_PIN))

# asynchroní získávání dat z čidel

# Optimalizovaná funkce pro měření vzdálenosti, která je asynchroní ☠️
async def get_distance(trig, echo):
    # Rychlejší přepnutí stavu triggeru
    trig.off()
    time.sleep_us(10) 
    trig.on()
    time.sleep_us(10)  # Kratší trvání pulzu, 10 mikrosekund je standard pro senzory jako HC-SR04
    trig.off()

    # Čekáme na náběžnou hranu signálu
    timeout_start = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), timeout_start) > 500:
            return -1  # Nenalezen žádný objekt

    start = time.ticks_us()

    # Čekáme na sestupnou hranu signálu
    timeout_start = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), timeout_start) > 500:
            return -1  # Objekt mimo detekční rozsah

    end = time.ticks_us()

    # Výpočet doby trvání a návrat hodnoty
    duration = time.ticks_diff(end, start)
    return duration  # Vracíme výsledek
    
# tohle bylo cancer najít jak to vůbec funguje a nastavit, ale podařilo se mi to
def play_wav(filename):
    try:
        with open(filename, 'rb') as f:
            # Read and parse WAV file header
            header = f.read(44)
            if header[0:4] != b'RIFF' or header[8:12] != b'WAVE':
                raise ValueError("Invalid WAV file format.")

            # Extract audio format details
            channels = int.from_bytes(header[22:24], 'little')
            sample_rate = int.from_bytes(header[24:28], 'little')
            bit_depth = int.from_bytes(header[34:36], 'little')

            if channels != 1:
                raise ValueError("Only mono WAV files are supported.")
            if bit_depth != 8:
                raise ValueError("Only 8-bit WAV files are supported.")

            print(f"Playing {filename}: {sample_rate} Hz, {bit_depth}-bit, {channels} channel(s)")

            # Calculate delay per sample
            sample_delay = 1 / sample_rate

            # Get file size
            file_size = os.stat(filename)[6]
            audio_data_size = file_size - 44  # Exclude header size

            # Read and play audio samples
            start_time = time.ticks_us()  # Start time in microseconds
            for i in range(audio_data_size):
                sample = f.read(1)  # Read one byte (8-bit sample)
                if not sample:
                    break
                dac.write(sample[0])
                while time.ticks_diff(time.ticks_us(), start_time) < i * sample_delay * 1_000_000:
                    pass  # Wait until the correct time to send the next sample

        print("Playback finished.")

    except Exception as e:
        print(f"Error playing WAV file: {e}")
    
        
async def main():
    play_wav("/come_play.wav")

    # šetříme elektřinou a stejně víc to svítit nemusí
    for i in range(50):
        np[i*4] = ((100,100,100))
        np.write()
    
    while True:
        distance1 = await get_distance(trig1, echo1)  # dostaneme 2 vzdalenosti
        distance2 = await get_distance(trig2, echo2)
        await asyncio.sleep_ms(1)   
        
        if (distance1 < 250) or ( distance2 < 250): # tohle je změřené takže jestli někdo bude šprtovat, že to je špatně, tak si to může předělat
            print("Míček detekován na senzoru!")
            play_wav("/gol_final.wav")
            await asyncio.sleep(1)

              

# Start the event loop
asyncio.run(main())

