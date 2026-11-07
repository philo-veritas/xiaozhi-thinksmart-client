"""Changing voices prepares a separate local clip and switching back plays it without synthesis."""
import asyncio
import io
import wave

import numpy as np

from test_barge_in import app, make_client


def test_wake_cache_by_voice_and_text(tmp_path, monkeypatch):
    monkeypatch.setattr(app, 'WAKE_CACHE', tmp_path)
    client = make_client()
    client.wake_chime = np.zeros((100, 2), np.float32)
    client.sounds = {}
    voices = ['a' * 64, 'b' * 64]
    requests = []

    async def speech(text, voice_key):
        requests.append((text, voice_key))
        data = io.BytesIO()
        with wave.open(data, 'wb') as w:
            w.setparams((1, 2, 24000, 0, 'NONE', ''))
            w.writeframes(np.full(2400, len(requests) * 500, dtype=np.int16).tobytes())
        return data.getvalue()

    client._speech = speech
    asyncio.run(client.sync_wake_voice(voices[0]))
    first = client.sounds['wake']
    asyncio.run(client.sync_wake_voice(voices[1]))
    assert not np.array_equal(client.sounds['wake'], first)
    asyncio.run(client.sync_wake_voice(voices[0]))
    assert np.array_equal(client.sounds['wake'], first)
    assert (tmp_path / 'current').read_text() == voices[0]
    assert requests == [(app.WAKE_REPLY, v) for v in voices]
    assert app.wake_file(voices[0], '另一句') != app.wake_file(voices[0], app.WAKE_REPLY)
