from transformers import FSMTForConditionalGeneration, FSMTTokenizer

class WMT19:
    def __init__(self, mname=None):
        if not mname:
            raise AttributeError
        self.tokenizer = FSMTTokenizer.from_pretrained(mname)
        self.model = FSMTForConditionalGeneration.from_pretrained(mname)

    def translate(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        outputs = self.model.generate(input_ids)
        decoded_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return decoded_text
    

# mname = "facebook/wmt19-en-ru"
# tokenizer = FSMTTokenizer.from_pretrained(mname)
# model = FSMTForConditionalGeneration.from_pretrained(mname)

# input = "‘Dictators Do Not Go on Vacation,’ Zelensky Warns Washington and Europe"
# wmt = WMT19("facebook/wmt19-en-ru")
# print(wmt.translate(input))