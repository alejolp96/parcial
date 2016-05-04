import pyaudio


class Reproo:
    def __init__(self, CHUNK, sampwidth,channels,rate):
        self.CHUNK = CHUNK
        self.sampwidth=sampwidth
        self.channels = channels
        self.framerate=rate

    def iniciosum(self):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.p.get_format_from_width(self.sampwidth),
                        channels=self.channels,
                        rate=self.framerate,
                        output=True)

    def repsum(self,wavearray):
        data = wavearray

        while data != '':
            self.stream.write(data)
            data = wavearray(self.CHUNK)


    def cerrarsum(self):

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

