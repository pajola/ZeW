from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.stem.snowball import SnowballStemmer
from ZeW import ZeroWidthSPaceAttack

class HS_evader:
    def __init__(self):
        #init the sentiment analyser
        self.analyser = SentimentIntensityAnalyzer()

        #define the stemming parser
        self.stemmer = SnowballStemmer("english")

        #define the class that allow us to perform the attack
        self.attacker = ZeroWidthSPaceAttack()

        #interface parameters
        self.mask = ['mask1', 'mask2']

    #detect negative words inside the sentence and apply to them a masking
    def poisoner(self,sentence, masking = 'mask1', index = 0, random = True):
        '''sentence = sentence to poison
            masking = type of attack. [mask1, mask2]
            index = index of malicious symbols from the given list
            random = a boolean variable that indicates if we randomly sample a
                malicious character. If True, the poisoner does not user the
                ``index'' info. 
        '''

        #control the input
        if masking not in self.mask:
            raise Exception('Invalid Masking')

        #tokenize
        tokens = sentence.split()

        #apply the attack when required
        result = []

        #indicate if the attack has been inserted
        status = False
        for t in tokens:
            #get the stem of the token
            t_stem = self.stemmer.stem(t)

            #calculate the negative score of the word
            score = self.analyser.polarity_scores(t_stem)['neg']

            if score > 0:
                #negative case -- injection
                if masking == 'mask1':
                    result.append(self.attacker.mask1(t, index, random = True))
                elif masking == 'mask2':
                    result.append(self.attacker.mask2(t, index, random = True))

                #
                status = True

            else:
                #positive case
                result.append(t)

        #concatenate the tokens
        final_sentence = ' '.join(result)

        return final_sentence, status
