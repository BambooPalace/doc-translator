from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch
import time


model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")


def translate(inputs, in_lang, out_lang, device, verbose=True):
    start = time.time()  
    with torch.no_grad():          
        tokenizer.src_lang = in_lang
        #max content length 1024
        encoded_ar = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True, max_length=1024)    
        encoded_ar.to(device)

        model.eval()
        model.to(device)
        generated_tokens = model.generate(
            **encoded_ar,
            forced_bos_token_id=tokenizer.lang_code_to_id[out_lang]
        )
        outputs = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    if verbose:
        print(f'Time consumed for translating on {device} is {time.time()-start:.2f} s.:\n{outputs}')
    return outputs
