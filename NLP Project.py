# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ckeld5Sn12J6aM8Yv8e_90vG9uRfO-ZQ
"""

! pip3 install transformers
! pip3 install datasets
! pip3 install accelerate





import wave
from transformers import BertTokenizer, BertModel
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset


# Tokenizer and model initialization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")
text = "Hi This is Surya and Its my Internship Assignment"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)


# speech-to-text pipeline using Hugging Face Transformers library
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, use_safetensors=True
)

processor = AutoProcessor.from_pretrained(model_id)


# The pipeline is created
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# Load a dataset for speech recognition
dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
sample = dataset[0]["audio"]
result = pipe(sample)

# Concatenating audio files
infiles = ['/content/common_voice_mr_30605571.wav', '/content/common_voice_mr_30605573.wav', '/content/common_voice_mr_30610947.wav', '/content/common_voice_mr_30610948.wav', '/content/common_voice_mr_30610949.wav', '/content/common_voice_mr_30610950.wav', '/content/common_voice_mr_30590848.wav', '/content/common_voice_mr_30602817.wav', '/content/common_voice_mr_30605566.wav', '/content/common_voice_mr_30605567.wav', '/content/common_voice_mr_30605569.wav', '/content/common_voice_mr_30617104.wav', '/content/common_voice_mr_30617106.wav', '/content/common_voice_mr_30617117.wav', '/content/common_voice_mr_30617119.wav', '/content/common_voice_mr_30617120.wav', '/content/common_voice_mr_30617121.wav', '/content/common_voice_mr_30617123.wav', '/content/common_voice_mr_30610968.wav', '/content/common_voice_mr_30610969.wav', '/content/common_voice_mr_30610951.wav', '/content/common_voice_mr_30610952.wav', '/content/common_voice_mr_30610953.wav', '/content/common_voice_mr_30610955.wav', '/content/common_voice_mr_30893943.wav', '/content/common_voice_mr_30893998.wav', '/content/common_voice_mr_30894007.wav', '/content/common_voice_mr_30894021.wav', '/content/common_voice_mr_30894085.wav', '/content/common_voice_mr_30894088.wav', '/content/common_voice_mr_30894091.wav', '/content/common_voice_mr_30894095.wav', '/content/common_voice_mr_30894193.wav', '/content/common_voice_mr_30894199.wav', '/content/common_voice_mr_30888773.wav', '/content/common_voice_mr_30888776.wav', '/content/common_voice_mr_30893939.wav', '/content/common_voice_mr_30893940.wav', '/content/common_voice_mr_30893941.wav','/content/common_voice_mr_30894236.wav', '/content/common_voice_mr_30894234.wav', '/content/common_voice_mr_30894232.wav', '/content/common_voice_mr_30894200.wav', '/content/common_voice_mr_30897221.wav', '/content/common_voice_mr_30894324.wav', '/content/common_voice_mr_30894322.wav', '/content/common_voice_mr_30894321.wav', '/content/common_voice_mr_30894320.wav', '/content/common_voice_mr_30898878.wav', '/content/common_voice_mr_30898877.wav', '/content/common_voice_mr_30898734.wav', '/content/common_voice_mr_30897226.wav', '/content/common_voice_mr_30897224.wav', '/content/common_voice_mr_30899064.wav', '/content/common_voice_mr_31878674.wav', '/content/common_voice_mr_31878877.wav', '/content/common_voice_mr_31878878.wav', '/content/common_voice_mr_31879447.wav', '/content/common_voice_mr_31879449.wav', '/content/common_voice_mr_31883832.wav', '/content/common_voice_mr_31883836.wav', '/content/common_voice_mr_31883884.wav', '/content/common_voice_mr_31892382.wav', '/content/common_voice_mr_31892821.wav', '/content/common_voice_mr_31893461.wav', '/content/common_voice_mr_31893799.wav', '/content/common_voice_mr_31894133.wav', '/content/common_voice_mr_31886216.wav', '/content/common_voice_mr_31886223.wav', '/content/common_voice_mr_31886175.wav', '/content/common_voice_mr_31886176.wav', '/content/common_voice_mr_31886177.wav', "/content/common_voice_mr_31931304.wav", "/content/common_voice_mr_32022227.wav", "/content/common_voice_mr_32126698.wav", "/content/common_voice_mr_32126825.wav", "/content/common_voice_mr_31913054.wav", "/content/common_voice_mr_31917535.wav", "/content/common_voice_mr_31917739.wav", "/content/common_voice_mr_31917816.wav", "/content/common_voice_mr_31894160.wav", "/content/common_voice_mr_31894161.wav", "/content/common_voice_mr_31894165.wav", "/content/common_voice_mr_31894498.wav", "/content/common_voice_mr_31894499.wav", "/content/common_voice_mr_31901494.wav", '/content/common_voice_mr_32022227.wav', "/content/common_voice_mr_31931304.wav", "/content/common_voice_mr_32126698.wav"]
outfile = "sounds.wav"

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])
output.close()


# speech-to-text pipeline to transcribe a list of audio files
data = []
for i in infiles:
  sample = i
  result = pipe(sample)
  data.append(result["text"])
# print(data)

reference_text = ['कौरव कर्ण हा महाभारतातील कुंतीआणि सूर्य यांचा पुत्र व दुर्योधनाचा मित्र होता', 'पिंड ठेवून आम्ही बाजूला झालो', 'इंग्रज सरकारने त्यांची नियुक्ती कलकत्त्याचे डिस्ट्रिक्ट मॅजिस्ट्रेट म्हणून केली', 'त्या नंतर उत्तरोत्तर या शहराचा विकास होत गेला', 'शरीरातील रक्तभिसरण क्रिया ताकामुळे व्यवस्थित होते', 'पांडवांच्या अज्ञातवासाच्या काळातही दुर्योधनाने गंधर्वांकडून पांडवांना मारण्याचा बेत केला', 'महाराष्ट्रातात रोजगारासाठी आलेले अनेक गरिबांचे वडापाव अन्न आहे', 'याच्या विषारी फुत्कारांमुळे यमुनेचे पाणी विषारी झाले होते', 'नव्या राज्याची मुंबई ही राजधानी व नागपूर उपराजधानी निश्चित झाली', 'तेव्हां मच्छिंद्रनाथाच्या भेटीची निराशा झाल्यामुळें तिच्या डोळ्यांस पाणी आले', 'परीक्षित हा अर्जुनाचा नातू व अभिमन्यू आणि उत्तरा यांचा पुत्र होता', 'कवड्यांचा संबंध पुनरुत्पत्तीशी आहे', 'कीर्तन ज्या स्थानावर उभे राहून करतात ते स्थान म्हणजे देवर्षी नारदांची कीर्तनाची गादी', 'त्यांनी धर्मांतरवर बंदी घातली त्यामुळे मुसलमान आणि ख्रिश्चन त्यांच्यावर नाराज झाला', 'भारतात प्राथमिक शिक्षण हे इयत्ता पहिली ते आठवी पर्यंत आहे', 'गोरक्षनाथांनी योग प्रकार जनमानसात रुजवला', 'सर्वसामान्य मुस्लिम समाजाने या धर्मांध मानसिकतेला साथ दिली नाही', 'या किल्ल्यामध्ये आता तमिळनाडू विधानसभेचे कामकाज चालते', 'मुंबईतील भांडवलदारांना जे मुख्यत अमहाराष्ट्रीय होते त्यांचा मुंबई महाराष्ट्राला द्यायला कडाडून विरोध होता', 'ती त्यास वेगवेगळी गाणी व गोष्टी सांगुन जागे ठेवते', 'त्याविरोधात बँकांची कर्ज प्राधिकरणामार्फत सीबीआयकडे तक्रार', 'पंडू ही पंडुरोगाने पीडित असल्याने त्याच्यापासून मुले होणे उचित नव्हते', 'शिवसेना हा एक भारतातील राजकीय पक्ष आहे', 'सदर पक्ष आर्थिक व राजकीय शक्तीच्या विकेंद्रीकरणाच्या बाजूने उभा असल्याचेही पक्षाच्या घटनेत म्हटले आहे', 'या कार्यक्रमामध्ये सर्वाना अन्न दान केले जाते', 'या रेषेत येणारी सर्व बेटे ही या पर्वतरांगेचा भाग आहे', 'तयार झालेले वादळ ज्या मार्गावरून प्रवास करते त्या मार्गावर वादळे होत रहातात', 'भारताने पहिला उपग्रह आकाशात पाठवला होता त्याला आर्यभट्ट असे नाव दिले आहे', 'सरकारी अनूदानावर या शाळा चालतात', 'ह्या बेटाचा पश्चिम भाग हैती देशाने व्यापला आहे', 'त्यांच्या नावावर एक कसोटी बळीही आहे', 'यमुना ही गंगेची उपनदी स्वतःच एक स्वतंत्र आणि मोठी नदी आहे', 'वेळेपूर्वी मला मरायचे नाही आणि मेल्यावरही जगायचे आहे', 'गाडगेबाबांचे विचार एकदा गाडगेबाबा रस्त्याने जात असताना', 'विजय मांजरेकर याचे वडील होत','म्हणजे आम्हाला अधिक उत्साह वाटेल', 'राष्ट्रीय व धार्मिक सण आणि उत्सव लेखिका करुणा ढापरे', 'राजकीय महामार्ग हे महामार्ग राज्य सरकारच्या अखत्यारीत येतात', 'रचनाकालाच्या अभ्यासासाठी भाषेचे स्वरूप हा पायाभूत आधार आहे', 'हा एक गट आहे आणि तो सर्वांसाठी उपलब्ध आहे', 'नदी जीवनदायी आहे', 'त्यांना रमेश माशेलकर या नावानेही ओळखले जाते', 'नामदेव हे त्यांचेच पूर्वज असावेत', 'दशरथापासून तिला भरत नावाचा पुत्र झाला', 'जीवनदान मिळालेले हे सरदार', 'परिणामी विद्यार्थी नव्यानव्या कॢप्तिपूर्ण व कल्पक उपक्रमांमध्ये रस घेऊ लागले आहेत', 'या टीकेला उत्तर देणे संघाला जमले नाही', 'दारू पिणाऱ्या अनेक व्यक्तींमध्ये एखादा न पिणारा अडचणीचा ठरतो', 'कृष्णा प्रेम द्वारे नियंत्रीत केले जाते कारण हे आहे', 'काश्मीरला भारताचे नंदनवन म्हणतात', 'वैदिक वाङ् मयात इंद्राचा उल्लेख या नावाने होतो', 'परंतु रावणाने लंकेचे राज्य मागितले', '।। भारत माता की जय ।।', 'या क्षेत्राची तीव्रता वाढत गेली तर वादळाचा जन्म होतो', 'किंवा शान्ताकारं भुजगशयनं पद् मनाभं सुरेशम् वृत्तव्योमगंगा हे देवप्रियाचे मूळ वृत्त आहे','माझ्या माहितीनुसार भाजपमध्ये कोणतीही नाराजी नाही', 'गोव्यातील मराठीसाठी काम करण्याच्या उद्देशाने स्थापन झालेल्या काही संस्था आहेत', 'त्याचा संबंध भूकंपाने होणाऱ्या नुकसानीशी निगडित असतो ऊर्जेशी नसतो', 'म्हणून त्याने सूर्याच्या दिशेने झेप घेतली', 'पोळी हा गव्हापासून तयार केलेला खाद्यपदार्थ आहे', 'इंधनरहित वाहने सायकल दुचाकीचा वापर भारतात शतकाआघीपासून होत असावा', 'हिंदूंनी रावणाला खलनायक एक नकारात्मक एक प्रतिस्पर्धी विरोधी भूमिकेमध्ये प्रक्षेपित केले गेले', 'या दिवशी संध्याकाळी दुकानांमध्ये पूजा केली जाते', 'दीड महिन्यापूर्वी पवारच्या संपर्क कार्यालयात तडीपार गुंडाला आश्रय दिल्याचे उघड झाले', 'जिल्ह्यातील हवामान उष्ण व कोरडे आहे', 'संपूर्ण अहमदाबादेत येथील नवरात्राच्या दिवसांत उत्सवाचे वातावरण असते', 'जुन्या मल्याळी भाषेतील शब्दफोडीप्रमाणे केरा नारळाचे झाड व आलम परिसर असा केरळमचा अर्थ होतो', 'त्यामुळे अक्षांशानुसार या किरणांचे प्रमाण बदलत जाते', 'चला आज फिरायला जाऊयात', 'तिचे सूत्रधार शंकरराव देव होते', 'आदरार्थी शब्दांनी केला जात असे लहानपणी गंगेजवळ असताना वसिष्ठांनी त्यांना सर्व वेद शिकविले होते', 'त्यातील एर्देनि हे रत् नाचे व सुबाशिदि हे सुभाषिताचे मंगोलियन भाषारूप होय', 'राजस्थानच्या नावातच राजांची भूमी असा अर्थ आहे', 'त्यांनी शून्य या अंकासठी ख या शब्दाचा वापर केला', 'त्यानुसार कृषी विद्यापीठातील शिक्षणक्रम राबविले जातात', 'थायलंडमध्ये रावणाचे शिल्प आढळते', 'हिच्या पित्याचे नाव भीष्मक असून आईचे नाव शुद्धमती होते', 'भारतीय अमेरिकन युरोपीय व इतरत्रही प्रताधिकार कायदा सर्व प्रकारच्या बेकायदेशीर वापराला मनाई करतो', 'हिंदू व हिंदुस्थान हे शब्द याच नदीवरुन पडले आहेत', 'या मंदिरासमोर सहा टन वजनाची घंटा आहे', 'हे मूळचे चाळीसगावचे रहिवासी त्यांचे आडनाव देशपांडे होते', 'याचे नाव गहिनीनाथ असे ठेव', "तिचे सूत्रधार शंकरराव देव होते", "चला आज फिराईला जाऊयात।", "आदरार्थी शब्दांनी केला जात असे लहानपणी गंगेजवळ असताना वसिष्ठांनी त्यांना सर्व वेद शिकविले होते"]
hypothesis_text = data

# Function to calculate Word Error Rate
def calculate_wer(reference, hypothesis):
    wer_scores = []

    for ref, hyp in zip(reference, hypothesis):
        ref_words = ref.split()
        hyp_words = hyp.split()

        Substitution = 0
        Deletion = 0
        Insertion = 0

        for ref, hyp in zip(ref_words, hyp_words):
            if ref == hyp:
                continue  # If No error move to next
            elif ref in hyp_words:
                Substitution += 1  # Substitution
            elif ref not in hyp_words:
                Deletion += 1  # Deletion
            elif hyp not in ref_words:
                Insertion += 1  # Insertion

        N = len(ref_words)
        wer = (Substitution + Deletion + Insertion) / N
        wer_scores.append(wer)
    return wer_scores


# Calculate WER scores
wer_scores = calculate_wer(reference_text, hypothesis_text)
for i, wer_score in enumerate(wer_scores):
    print(f"Word Error Rate{i + 1}: {wer_score}")