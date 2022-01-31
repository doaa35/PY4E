text = "X-DSPAM-Confidence:    0.8475"
bbs = text.find('0')
print(float(text[bbs:]))
