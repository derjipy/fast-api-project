from fastapi import FastAPI
import codecs

app = FastAPI()
"""
@app.get("/00")
def read_root():
    return codecs.encode(this.s, 'rot_13')
"""
text = 'hello, gotlib gotlib'
print(text)