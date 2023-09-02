import os
import click
from transformers import pipeline
import requests as r
from bs4 import BeautifulSoup


def extract_from_url(url):
    text =  ""
    html  = r.get(url).text
    parser = BeautifulSoup(html, 'html.parser')
    for par in parser.find_all("p"):
        print(par.text)
        text+=par.text
    return text


def process(text):
    summarizer = pipeline("summarization",model='t5-small')
    result = summarizer(text,max_length=180)
    click.echo("Summarization process complete!!!")
    click.secho("="*100,fg='green')
    return result[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url,file):
    if url: text = extract_from_url(url)
    elif file:
        with open(file,'r') as f:
            text = f.read()
    click.secho(f"Summarized text -> {url or file}",fg='yellow')
    click.secho(process(text),fg='green')


