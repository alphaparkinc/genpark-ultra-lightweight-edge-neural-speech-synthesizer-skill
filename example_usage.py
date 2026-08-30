from client import UltraLightweightEdgeNeuralSpeechSynthesizerClient

def main():
    client = UltraLightweightEdgeNeuralSpeechSynthesizerClient()
    res = client.synthesize_edge_speech('Edge intelligence is compiling local vector weights.', 'en_am_adam')
    print('Kokoro Edge TTS: ' + res['tts_synthesis_id'] + ' (' + str(res['model_parameter_count_million']) + 'M params)')
    print('RTF: ' + str(res['realtime_factor_rtf']) + 'x realtime | RAM: ' + str(res['memory_footprint_ram_mb']) + ' MB')
    print('MOS Naturalness: ' + str(res['naturalness_mos_score']) + ' / 5.0')
    print('Audio URL: ' + res['synthesized_audio_stream_url'])

if __name__ == '__main__':
    main()
