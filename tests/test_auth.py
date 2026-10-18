import pytest

from auth import fingerprint, rotate_refresh_token


def test_rotation_revokes_previous_token():
    revoked = set()
    assert rotate_refresh_token("previous", "replacement", revoked) == fingerprint("replacement")
    assert fingerprint("previous") in revoked


def test_reusing_previous_token_is_rejected():
    revoked = {fingerprint("previous")}
    with pytest.raises(ValueError):
        rotate_refresh_token("previous", "another", revoked)
