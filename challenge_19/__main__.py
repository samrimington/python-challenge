import email
import os
import wave

def challenge_19_1() -> None:
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "challenge_19.mbox")
    with open(input_path) as f:
        message = email.message_from_file(f)
    inner = message.get_payload(0)
    with open(f"challenge_19_{inner.get_filename()}", 'wb') as f:
        f.write(inner.get_payload(decode=True))

def challenge_19_2():
    with wave.open('challenge_19_indian.wav', 'rb') as f:
        n = f.getnframes()
        params = f.getparams()
        frames = f.readframes(n)
    with wave.open('challenge_19_indian_shifted.wav', 'wb') as f:
        f.setparams(params)
        f.writeframes(frames[1:])

"""http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html"""
challenge_19_1()

"""
Never mind that.

Have you found my broken zip?

md5: bbb8b499a0eef99b52c7f13f4e78c24b

Can you believe what one mistake can lead to?
"""
challenge_19_2()
