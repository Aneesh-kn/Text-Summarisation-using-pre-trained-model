# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:12:00 2023

@author: aneesh
"""

from flask import Flask, request, render_template, flash
from forms import RegistrationForm
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')

tokenizer = AutoTokenizer.from_pretrained('t5-base')



app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/out')
def out():
    return  render_template("out.html")

@app.route('/', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    
    if form.validate_on_submit():
        flash(f"Done. please wait")
        #print(form.input_text.data)
        text=form.input_text.data
        tokens_input = tokenizer.encode("summarize: "+text, return_tensors='pt', max_length=tokenizer.model_max_length, truncation=True)
        summary_ids = model.generate(tokens_input, min_length=80, max_length=150, length_penalty=20,num_beams=2)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        #print(summary)
        return  render_template("out.html",posts=summary)
    return  render_template("register.html",form=form)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
    
    