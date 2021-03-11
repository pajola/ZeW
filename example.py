from hs_evader import HS_evader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#define the ZeW evader
engine = HS_evader()

#define the sentiment analyzer
analyser = SentimentIntensityAnalyzer()

#define the original sentence
sentence = "I wanna kill you"

#generate the malicious sentences
poison1, _ = engine.poisoner(sentence, "mask1")
poison2, _ = engine.poisoner(sentence, "mask2")

#print
print(f"Sentences.\n\tOriginal.\tLenght={len(sentence)}\t{sentence}" +
    f"\n\tMask1.\t\tLenght={len(poison1)}\t{poison1}" +
    f"\n\tMask2.\t\tLenght={len(poison2)}\t{poison2}")

#compute the negativity
original_sent = analyser.polarity_scores(sentence)['neg']
poison1_sent = analyser.polarity_scores(poison1)['neg']
poison2_sent = analyser.polarity_scores(poison2)['neg']

print(f"\nNegative scores:\n\toriginal={original_sent:.2f}\n\t" +
        f"mask1={poison1_sent:.2f}\n\tmask2={poison2_sent:.2f}")
