import spacy

nlp_ner = spacy.load("model-best")

text = """
[K-Choreo 8K] 뉴진스 직캠 'Hype Boy' (NewJeans Choreography) l @MusicBank 220812
[K-Choreo 8K HDR] 르세라핌 직캠 'ANTIFRAGILE' (LE SSERAFIM Choreography) l @MusicBank 221028
[MPD직캠] 르세라핌 직캠 4K 'Blue Flame' (LE SSERAFIM FanCam) | @MCOUNTDOWN_2022.5.5
"""

doc = nlp_ner(text)

spacy.displacy.serve(doc, style="ent", port=6969)
