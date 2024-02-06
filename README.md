This is an implementation of LLM-based language translator API with the following parameters:
- source_file: the file path to translate, either a `docx` or `pdf` file
- source_lang: the language used in the file of filepath specified, e.g. english
- target_file(optional): the translated file path (output), default in same folder as source file.
- target_lang: the language to translate into, e.g. chinese

#### LLM
The model use is [mBART-50 many to many multilingual machine translation]('https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt') of 611M parameters, which support translation between any pair of 52 languages lised below.


Arabic (ar_AR), Czech (cs_CZ), German (de_DE), English (en_XX), Spanish (es_XX), Estonian (et_EE), Finnish (fi_FI), French (fr_XX), Gujarati (gu_IN), Hindi (hi_IN), Italian (it_IT), Japanese (ja_XX), Kazakh (kk_KZ), Korean (ko_KR), Lithuanian (lt_LT), Latvian (lv_LV), Burmese (my_MM), Nepali (ne_NP), Dutch (nl_XX), Romanian (ro_RO), Russian (ru_RU), Sinhala (si_LK), Turkish (tr_TR), Vietnamese (vi_VN), Chinese (zh_CN), Afrikaans (af_ZA), Azerbaijani (az_AZ), Bengali (bn_IN), Persian (fa_IR), Hebrew (he_IL), Croatian (hr_HR), Indonesian (id_ID), Georgian (ka_GE), Khmer (km_KH), Macedonian (mk_MK), Malayalam (ml_IN), Mongolian (mn_MN), Marathi (mr_IN), Polish (pl_PL), Pashto (ps_AF), Portuguese (pt_XX), Swedish (sv_SE), Swahili (sw_KE), Tamil (ta_IN), Telugu (te_IN), Thai (th_TH), Tagalog (tl_XX), Ukrainian (uk_UA), Urdu (ur_PK), Xhosa (xh_ZA), Galician (gl_ES), Slovene (sl_SI)


#### Run
The code automatically runs on GPU if GPU is available, and it run much faster on GPU compared to locally run on CPU.
You are recommended to clone the code in a Google Colab notebook, choose GPU as accelerator, and run the code.
- Local run (CPU)
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 run.py
#sample url with simle sample document 'jd.pdf'
http://127.0.0.1:8000/translate?source_file=samples/jd.pdf&source_lang=english&target_lang=chinese
```
- Google Colab (with GPU)
```
git clone https://github.com/BambooPalace/doc-translator.git
cd doc-translator
pip3 install -r requirements.txt
#run default scripts with complex sample document 'apple.pdf', GPU now enables faster runtime
python3 app/translator.py
```
