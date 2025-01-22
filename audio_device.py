import pyaudiowpatch as pyaudio


class AudioDevice:

    def __init__(
        self, device_index, chunk_duration=0.5, sample_rate=None, num_channels=None
    ):
        """A streaming audio device."""
        self.stream = None
        self.audio_buffer = []
        p = pyaudio.PyAudio()

        device = p.get_device_info_by_index(device_index)
        self.sample_rate = (
            int(device["defaultSampleRate"]) if sample_rate is None else sample_rate
        )
        self.chunk_size = int(self.sample_rate * chunk_duration)
        self.num_channels = (
            max(device["maxInputChannels"], device["maxOutputChannels"])
            if num_channels is None
            else num_channels
        )

        self.stream_args = dict(
            format=pyaudio.paFloat32,
            channels=self.num_channels,
            rate=self.sample_rate,
            frames_per_buffer=self.chunk_size,
            input=True,
            input_device_index=device_index,
            stream_callback=self.buffer_chunk,
        )
        self.audio = p

    def retrieve_buffer(self):
        audio_buffer = self.audio_buffer
        self.audio_buffer = []
        return audio_buffer

    def buffer_chunk(self, in_data, frame_count, time_info, status):
        self.audio_buffer.append(in_data)
        return (None, pyaudio.paContinue)

    def start_stream(self):
        if self.stream is None:
            self.stream = self.audio.open(**self.stream_args)

    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
