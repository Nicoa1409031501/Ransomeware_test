import base64
with open('public.pem', 'rb') as f:
    public = f.read()
print("orgin public-key:")
print(public)
print("encoded with base64:")
print(base64.b64encode(public))