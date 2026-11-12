"""The main screen's theme: the client keeps the choice, the page paints it (web/v2, DESIGN.md 主题).

  uv run --no-project --with numpy --with soxr --with websockets --with aiohttp --with pytest --with pytest-asyncio \\
      python -m pytest -q tests
"""
import sys
import types

import pytest

sys.modules.setdefault('sounddevice', types.ModuleType('sounddevice'))
sys.modules.setdefault('thinksmart_client.webrtc_apm', types.ModuleType('thinksmart_client.webrtc_apm'))

from thinksmart_client import app, config  # noqa: E402


def test_the_default_is_black():
    assert config.DEFAULTS['theme'] == 'black' and 'black' in app.THEMES


@pytest.mark.asyncio
async def test_set_theme_saves_and_tells_the_page(monkeypatch):
    saved, told = {}, []
    monkeypatch.setattr(config, 'save', lambda **kw: saved.update(kw))
    c = app.Client.__new__(app.Client)
    c.theme, c.state = 'black', 'idle'
    c.set_state = told.append
    for theme in app.THEMES:
        assert await c.set_theme(theme) == theme
        assert c.theme == theme and saved['theme'] == theme
    assert told == ['idle'] * len(app.THEMES)
    for bad in ('pink', '', None, 3):
        with pytest.raises(ValueError):
            await c.set_theme(bad)
    assert c.theme == app.THEMES[-1] and saved['theme'] == app.THEMES[-1]
