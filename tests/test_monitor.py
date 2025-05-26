# tests/test_monitor.py
from monitoramento import is_site_up

def test_google_is_up():
    assert is_site_up("https://www.google.com") == True

def test_invalid_site_is_down():
    assert is_site_up("http://thisurldoesnotexist.tld") == False
